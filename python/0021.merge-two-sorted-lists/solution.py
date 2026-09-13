# Created by Chono-Hina at 2026/09/13 20:04
# leetgo: 1.4.18
# https://leetcode.cn/problems/merge-two-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        p1 = list1
        p2 = list2
        p3 = p2
        p4 = None

        while p2:
            if p1.val <= p2.val:
                if p1.next is None:
                    p1.next = p2
                    return list1
                if p1.next.val >= p2.val:
                    # 把p2当前值插到p1之后
                    p3 = p2.next
                    p4 = p1.next
                    p1.next = p2
                    p2.next = p4
                    p2 = p3
                else:
                    p1 = p1.next
        
        return list1
        

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)
    print("\noutput:", serialize(ans, "ListNode"))
