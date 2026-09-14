# -*- coding: utf-8 -*-
"""
第 148 题 排序链表 · 标准版（自底向上归并，O(n log n) + O(1) 空间，满足进阶要求）
用户递归版思路正确但空间 O(log n)（递归栈）且常数较大；本版无递归，段长逐层翻倍合并。
"""
from typing import Optional


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ① 数长度
        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        # ② 自底向上：段长 step = 1, 2, 4, ... 逐层两两合并
        dummy = ListNode(0, head)
        step = 1
        while step < n:
            prev, cur = dummy, dummy.next
            while cur:
                left = cur                                   # 第一段
                right = self._split(cur, step)               # 第二段（切出 step 个，断开）
                cur = self._split(right, step)               # 剩余部分
                prev.next = self._merge(left, right)         # 合并两段
                while prev.next:                             # prev 移到合并结果末尾
                    prev = prev.next
            step *= 2
        return dummy.next

    def _split(self, head: Optional[ListNode], step: int) -> Optional[ListNode]:
        """切出前 step 个节点并断开，返回剩余链头"""
        for _ in range(step - 1):
            if head:
                head = head.next
        if not head:
            return None
        rest = head.next
        head.next = None
        return rest

    def _merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """标准双指针归并（21 题标准版）"""
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
