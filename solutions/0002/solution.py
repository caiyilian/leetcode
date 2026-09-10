# Created by Chono-Hina at 2026/09/10 23:52
# leetgo: 1.4.18
# https://leetcode.cn/problems/add-two-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, val = divmod(total, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
        

# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)
    print("\noutput:", serialize(ans, "ListNode"))
