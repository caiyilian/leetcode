# -*- coding: utf-8 -*-
"""
第 19 题 删除链表的倒数第 N 个结点 · 标准版（dummy 哨兵 + 快慢指针）
与用户 v2（无 dummy 快慢指针版）逻辑等价，但用 dummy 统一处理"删头"，无特判。
"""
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)      # 哨兵：让"删头"也变成普通删除（无需特判）
        fast = slow = dummy
        for _ in range(n + 1):         # fast 先走 n+1 步（比 slow 超前 n+1 个位置）
            fast = fast.next
        while fast:                    # fast 到 None 时，slow 停在待删节点的前一个
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next     # 跳过待删节点
        return dummy.next