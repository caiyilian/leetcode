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
        """
        快慢指针，使得慢指针指向右边一半
        """
        if not head:
            return head

        def get_half(p):
            p_slow = p
            p_fast = p
            prev = p
            while p_fast and p_fast.next:
                p_fast = p_fast.next.next
                prev = p_slow
                p_slow = p_slow.next
            prev.next = None          # 切断成两条链 [p..prev] 和 [p_slow..]
            return p, p_slow          # 头和尾（右半头）

        def merge_node(p1, p2):
            # 合并两个升序链表（21 题哨兵归并）
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
            # 其中一个为None
            if p1:
                curr.next = p1
            else:
                curr.next = p2
            return dummy.next

        def fun(p):
            if p.next is None:        # 单节点天然有序
                return p
            p_head, p_tail = get_half(p)
            p_head = fun(p_head)      # 左半排序
            p_tail = fun(p_tail)      # 右半排序
            return merge_node(p_head, p_tail)

        return fun(head)
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
