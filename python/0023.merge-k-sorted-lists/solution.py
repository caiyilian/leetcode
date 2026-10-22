# Created by Chono-Hina at 2026/09/14 15:11
# leetgo: 1.4.18
# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        length = len(lists)

        def merge2(p1, p2):
            dummy = ListNode(0)
            curr = dummy
            while p1 and p2:
                if p1.val > p2.val:
                    curr.next = p2
                    p2 = p2.next
                else:
                    curr.next = p1
                    p1 = p1.next
                curr = curr.next
            if p1:
                curr.next = p1
            else:
                curr.next = p2
            return dummy.next

        while length > 1:
            for i in range((length) // 2):
                lists[i] = merge2(lists[2 * i], lists[2 * i + 1])

            if length % 2 == 1:  # 奇数：最后一条搬到中间位，length = 1 + length//2
                lists[(length) // 2] = lists[length - 1]
                length = 1 + length // 2
            else:
                length = length // 2
        return lists[0]
        

# @lc code=end

if __name__ == "__main__":
    lists: List[ListNode] = deserialize("List[ListNode]", read_line())
    ans = Solution().mergeKLists(lists)
    print("\noutput:", serialize(ans, "ListNode"))
