# Created by Chono-Hina at 2026/09/13 17:13
# leetgo: 1.4.18
# https://leetcode.cn/problems/reverse-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p1 = head
        p2 = p1.next
        p3 = None

        while True:
            p1.next = p3
            if p2 is None:
                break
            p3 = p1
            p1 = p2
            p2 = p2.next
        return p1
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)
    print("\noutput:", serialize(ans, "ListNode"))
