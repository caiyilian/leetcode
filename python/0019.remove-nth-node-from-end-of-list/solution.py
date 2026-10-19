# Created by Chono-Hina at 2026/09/13 21:24
# leetgo: 1.4.18
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().removeNthFromEnd(head, n)
    print("\noutput:", serialize(ans, "ListNode"))
