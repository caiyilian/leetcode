# Created by Chono-Hina at 2026/09/10 23:52
# leetgo: 1.4.18
# https://leetcode.cn/problems/add-two-numbers/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        add_one = 0
        p1 = l1
        p2 = l2
        # 第一阶段：处理两链共有的位数（谁先走完谁触发拼接/退出）
        while True:
            p1.val += p2.val + add_one
            if p1.val > 9:
                add_one = 1
                p1.val = p1.val % 10
            else:
                add_one = 0
            if p2.next is None:
                break
            if p1.next is None:
                p1.next = p2.next
                break
            p1 = p1.next
            p2 = p2.next

        # 第二阶段：剩余位数继续传播进位
        while True:
            if p1.next is None:
                break
            p1 = p1.next
            p1.val += add_one
            if p1.val > 9:
                add_one = 1
                p1.val = p1.val % 10
            else:
                add_one = 0

        # 最终进位：补一个最高位节点
        if add_one:
            p1.next = ListNode(1)
        return l1
        

# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)
    print("\noutput:", serialize(ans, "ListNode"))
