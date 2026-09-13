# -*- coding: utf-8 -*-
"""
第 21 题 合并两个有序链表 · 标准双指针归并版（面试推荐写法）
与用户原版（list2 逐个插入 list1）结果完全一致，但代码更短、更易口述：
用 dummy 哨兵处理"结果头是谁"，谁小接谁，剩的直接接尾巴。
"""
from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)          # 哨兵节点：避免处理"结果头是谁"的分支
        cur = dummy
        while list1 and list2:       # 谁小接谁（双指针归并）
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2    # 剩余部分直接接上（至少一个为 None）
        return dummy.next
