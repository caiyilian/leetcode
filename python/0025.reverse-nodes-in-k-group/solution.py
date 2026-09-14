# Created by Chono-Hina at 2026/09/14 11:57
# leetgo: 1.4.18
# https://leetcode.cn/problems/reverse-nodes-in-k-group/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next and k != 1):
            return head
        dummy = ListNode(0)
        dummy.next = head
        p_prev = dummy
        p_now_last = head
        while p_now_last and p_now_last.next:
            for _ in range(k - 1):
                if not (p_now_last and p_now_last.next):
                    return dummy.next
                p_now_last = p_now_last.next

            p_next = p_now_last.next
            p_now_last.next = None

            p_prev.next, p_now_last = self.reverse_list(p_prev.next)
            p_now_last.next = p_next

            p_prev = p_now_last
            p_now_last = p_next
        return dummy.next

    def reverse_list(self, head):
        if not (head and head.next):
            return head
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 返回 (反转后新头, 反转后新尾=原头)
        return prev, head
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().reverseKGroup(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
