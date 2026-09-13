# Created by Chono-Hina at 2026/09/13 18:54
# leetgo: 1.4.18
# https://leetcode.cn/problems/linked-list-cycle/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p_fast = head
        p_slow = head
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                return True
        return False
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().hasCycle(head)
    print("\noutput:", serialize(ans, "boolean"))
