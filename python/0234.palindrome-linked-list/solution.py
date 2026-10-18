# Created by Chono-Hina at 2026/09/13 17:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/palindrome-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        p_fast = head
        p_slow = self.reverseList(p_slow)
        while p_slow:
            if p_slow.val != p_fast.val:
                return False
            p_slow = p_slow.next
            p_fast = p_fast.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = None
        while p1:
            p3 = p1.next
            p1.next = p2
            p2 = p1
            p1 = p3
        return p2

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().isPalindrome(head)
    print("\noutput:", serialize(ans, "boolean"))
