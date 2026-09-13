# Created by Chono-Hina at 2026/09/13 22:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/swap-nodes-in-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = p1.next
        p3 = p2.next
        p4 = p3.next
        while True:
            # 交换p2,p3
            p2.next = p4
            p3.next = p2
            p1.next = p3
            if not (p4 and p4.next):
                break
            p1 = p3.next # p1向后移动两个格子
            p2 = p4
            p3 = p4.next
            p4 = p3.next
        return dummy.next
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().swapPairs(head)
    print("\noutput:", serialize(ans, "ListNode"))
