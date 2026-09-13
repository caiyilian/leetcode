# -*- coding: utf-8 -*-
"""
第 24 题 两两交换链表中的节点 · 标准版（先判断后处理，while 条件直接表达退出条件）
与用户原版（while True + break，先处理后判断）完全等价（5 万组对拍 0 差异）。
关键差异：判断挪到循环开头 + 指针循环内现取 + 只推进 p1 —— 条件就能写进 while。
"""
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = dummy
        while p1.next and p1.next.next:   # 先判断：还剩 ≥2 个节点？
            p2 = p1.next
            p3 = p2.next
            p2.next = p3.next
            p3.next = p2
            p1.next = p3
            p1 = p2                        # 交换后 p2 是下一组的前驱
        return dummy.next