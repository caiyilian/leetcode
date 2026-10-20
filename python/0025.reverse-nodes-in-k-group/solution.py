# Created by Chono-Hina at 2026/09/14 11:57
# leetgo: 1.4.18
# https://leetcode.cn/problems/reverse-nodes-in-k-group/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse_node(head):
            result = None
            p = head
            while p:
                next_node = p.next
                p.next = result
                result = p
                p = next_node
            return result, head  # 头和尾

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        """
        需要有一个prev, p1, p_last, p_next
        prev一开始就是dummy
        """
        while prev.next:
            p1 = prev.next  # prev.next不能为None
            p_last = p1
            for _ in range(k - 1):
                p_last = p_last.next
                if p_last is None:
                    break
            else:  # 没有发生break
                p_next = p_last.next
                # 把p_last的next设置为None
                p_last.next = None
                p1, p_last = reverse_node(p1)
                prev.next = p1          # ★ 关键：prev 接反转后的新头
                p_last.next = p_next    # 新尾接下一组
                prev = p_last           # prev 前进到新尾
                continue
            break
        return dummy.next
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().reverseKGroup(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
