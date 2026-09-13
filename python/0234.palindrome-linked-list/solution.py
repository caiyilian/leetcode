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
        if not head:
            return False
        p_fast = head
        p_slow = head
        while (p_fast and p_fast.next):
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        p_slow = self.reverse_list(p_slow)
        p_fast = head
        while p_slow:
            if p_fast.val != p_slow.val:
                return False
            p_fast = p_fast.next
            p_slow = p_slow.next
        return True

    def reverse_list(self, head):
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
    ans = Solution().isPalindrome(head)
    print("\noutput:", serialize(ans, "boolean"))
