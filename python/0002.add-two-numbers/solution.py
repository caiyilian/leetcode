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
        if not l1:
            return l2
        if not l2:
            return l1
        flag = 0
        p = l1
        while l1 and l2:
            l1.val += l2.val + flag
            if l1.val > 9:
                flag = 1
                l1.val = l1.val % 10
            else:
                flag = 0
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            prev.next = l2
            l1 = l2
        while l1:
            l1.val += flag
            if l1.val > 9:
                flag = 1
                l1.val = l1.val % 10
            else:
                flag = 0
            prev = l1
            l1 = l1.next
        if flag:
            prev.next = ListNode(1)
        return p
        

# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)
    print("\noutput:", serialize(ans, "ListNode"))
