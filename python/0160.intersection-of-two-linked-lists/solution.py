# Created by Chono-Hina at 2026/09/13 16:33
# leetgo: 1.4.18
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    intersectVal: int = deserialize("int", read_line())
    listA: ListNode = deserialize("ListNode", read_line())
    listB: ListNode = deserialize("ListNode", read_line())
    skipA: int = deserialize("int", read_line())
    skipB: int = deserialize("int", read_line())
    ans = Solution().getIntersectionNode(listA, listB)
    print("\noutput:", serialize(ans, "ListNode"))
