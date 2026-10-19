"""19. 删除链表的倒数第 N 个结点（二刷）——快慢指针 + dummy 哨兵（O(n)/O(1) 最优解）

用户 AC 版（2026-10-19 20:46 提交 755788223，WA→AC，0ms/19MB）
- fast 先走 n 步，fast/slow 同速走，fast 到 None 时 slow 停在待删节点，prev(dummy 起步) 是其前驱
- WA 版（20:42）删头节点时 prev=None 直接 return None 把整条链删了 → 加 dummy 哨兵修复
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        快慢指针，但是这里的快慢不是步长，而是快指针先走n步，然后两个指针一起一步一步走
        最终快指针是None的时候，慢指针到达要删除的地方
        """
        dummy = ListNode(0)
        dummy.next = head
        p_fast = head
        p_slow = head
        prev = dummy
        for _ in range(n):
            p_fast = p_fast.next
        while p_fast:
            p_fast = p_fast.next
            prev = prev.next
            p_slow = p_slow.next
        prev.next = p_slow.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    def build(vals):
        d = ListNode(0)
        cur = d
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next

    def to_list(head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    print(to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)))  # [1,2,3,5]
    print(to_list(s.removeNthFromEnd(build([1]), 1)))               # []
    print(to_list(s.removeNthFromEnd(build([1, 2]), 1)))            # [1]
    print(to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 5)))   # [2,3,4,5] 删头
