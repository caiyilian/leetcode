# Created by Chono-Hina at 2026/09/14 14:07
# leetgo: 1.4.18
# https://leetcode.cn/problems/copy-list-with-random-pointer/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}
        p = head
        dummy = Node(0)
        prev = dummy
        while p:
            new = Node(p.val)
            prev.next = new
            prev = new
            hash_map[p] = new
            p = p.next
        p = head
        new = dummy.next
        while p:
            new.random = hash_map[p.random]
            new = new.next
            p = p.next
        return dummy.next
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().copyRandomList(head)
    print("\noutput:", serialize(ans, "ListNode"))
