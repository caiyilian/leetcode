# -*- coding: utf-8 -*-
"""
第 2 题 两数相加 · 标准简洁版（dummy + carry 循环）
与用户 v2（原地改 l1 两阶段版）数值完全一致（5 万组对拍 0 差异）。
优势：10 行、无分支爆炸、一个 while 条件覆盖长度不同/最终进位。
代价：新建结果链表（O(max(m,n)) 空间 vs 用户版的 O(1) 额外空间）。
"""
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:                      # 一个条件覆盖所有情况
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = v // 10
            cur.next = ListNode(v % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
