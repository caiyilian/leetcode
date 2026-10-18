"""142. 环形链表 II（二刷）——快慢指针 + 二次相遇求入口（O(n)/O(1) 最优解）

用户 AC 版（2026-10-18 22:59 提交 755604363，一次通过，59ms/22.2MB）
① 快慢指针追及：无环快指针到 None → None；有环必然相遇
② 相遇后 slow 重置回 head，两指针同速（各 1 步）再走 → 再次相遇点 = 环入口
推导：设 head 到入口 a 步、入口到相遇点 b 步、环长 L，
slow 走 a+b，fast 走 2(a+b)=a+b+kL → a+b=kL → a=kL-b
即：从相遇点出发走 kL-b 步 = 从 head 出发走 a 步，两者在入口汇合
"""

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针
        如果没有环，快指针会到None
        如果有，快慢指针先会和，然后其中一个指针到起点，然后两个指针同时一次走一步，再次相交
        就是相交点
        """
        p_fast = head
        p_slow = head

        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
            if p_slow is p_fast:
                # 碰到一起了，现在找环形起点
                p_slow = head
                while p_slow is not p_fast:  # 循环直到两个相等
                    p_slow = p_slow.next
                    p_fast = p_fast.next
                return p_slow
        return None


if __name__ == "__main__":
    s = Solution()

    def build(vals, pos):
        if not vals:
            return None
        nodes = [ListNode(v) for v in vals]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    def idx(res, head):
        """辅助：返回结果节点在链表中的位置（0 起）"""
        i, cur = 0, head
        while cur:
            if cur is res:
                return i
            cur = cur.next
            i += 1
        return -1

    h = build([3, 2, 0, -4], 1)
    print(idx(s.detectCycle(h), h))   # 1
    h = build([1, 2], 0)
    print(idx(s.detectCycle(h), h))   # 0
    h = build([1], -1)
    print(s.detectCycle(h))           # None
    h = build([], -1)
    print(s.detectCycle(h))           # None
    h = build([1, 2, 3, 4, 5], 2)     # 环入口在 index 2
    print(idx(s.detectCycle(h), h))   # 2
