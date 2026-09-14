# Created by Chono-Hina at 2026/09/14 10:35
# leetgo: 1.4.18
# https://leetcode.cn/problems/sort-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return head
        return self.half_list(head)

    def half_list(self, head):
        if not head.next:
            return head
        p1 = head
        p2 = head
        p0 = ListNode(0)
        p0.next = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            p0 = p0.next
        p0.next = None
        return self.mergeTwoLists(self.half_list(head), self.half_list(p1))

    def mergeTwoLists(self, list1, list2):
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
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
