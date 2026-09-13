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
        if not head:
            return head
        p_fast = head
        p_slow = head
        for _ in range(n):
            p_fast = p_fast.next
        if p_fast is None:
            # 要删除的就是当前节点
            return head.next
        while p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next
        # 此时，p_slow的下一个节点就是要删除的
        p_slow.next = p_slow.next.next
        return head
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().removeNthFromEnd(head, n)
    print("\noutput:", serialize(ans, "ListNode"))
