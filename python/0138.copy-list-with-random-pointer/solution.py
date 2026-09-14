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
        if not head:
            return None
        dummy = Node(0)
        p_d = dummy
        p = head
        hash_dict = {}
        while p:
            p_d.next = Node(p.val)
            p_d = p_d.next
            hash_dict[p] = p_d
            p = p.next
        for key, value in hash_dict.items():
            value.random = hash_dict.get(key.random, None)
        return dummy.next
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().copyRandomList(head)
    print("\noutput:", serialize(ans, "ListNode"))
