"""141. 环形链表（二刷）——快慢指针追及（O(n)/O(1) 最优解）

用户 AC 版（2026-10-18 22:55 提交 755603615，一次通过，57ms/22.4MB）
快指针每次 2 步、慢指针 1 步：
- 无环：快指针先走到 None，循环自然结束 → False
- 有环：两指针必然在环内相遇 → True
注意：用 is（指针身份比较）判断相遇，而不是 ==（值比较）
"""

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
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
                # 碰到一起了
                return True
        return False


if __name__ == "__main__":
    s = Solution()

    # 手工用例：无环 / 环在中间 / 自环 / 空链表 / 单节点无环
    def build(vals, pos):
        if not vals:
            return None
        nodes = [ListNode(v) for v in vals]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        if pos >= 0:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    print(s.hasCycle(build([3, 2, 0, -4], 1)))  # True
    print(s.hasCycle(build([1, 2], 0)))         # True
    print(s.hasCycle(build([1], -1)))           # False
    print(s.hasCycle(build([], -1)))            # False
    print(s.hasCycle(build([1, 2, 3], -1)))     # False
