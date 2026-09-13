# Created by Chono-Hina at 2026/09/13 19:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p_fast = head
        p_slow = head
        p_start = head
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                while True:
                    if p_slow == p_start:
                        return p_slow
                    p_slow = p_slow.next
                    p_start = p_start.next
        return None
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head)
    print("\noutput:", serialize(ans, "ListNode"))
