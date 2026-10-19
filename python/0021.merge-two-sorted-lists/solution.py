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
        # 哨兵
        result = ListNode(0)
        p = result
        """
        对比list1和list2的值，小的，result.next = list
        list = list.next
        然后继续，如果某一个为None，那就只看另一个
        """
        while list1 or list2:
            if list1 is None:
                result.next = list2
                list2 = list2.next
            elif list2 is None:
                result.next = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    result.next = list1
                    list1 = list1.next
                else:
                    result.next = list2
                    list2 = list2.next
            result = result.next
        return p.next
        

# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)
    print("\noutput:", serialize(ans, "ListNode"))
