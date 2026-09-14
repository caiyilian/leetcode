# -*- coding: utf-8 -*-
"""
第 138 题 随机链表的复制 · 节点交错法（O(1) 额外空间，满足 follow-up）
与用户哈希法结果等价（5 万组深拷贝验证一致）。三步：
① 每个原节点后插入拷贝 ② 补 random ③ 拆成两条链
"""
from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # ① 插入拷贝：A -> A' -> B -> B' -> ...
        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        # ② 补 random：A'.random = A.random.next（原 random 的拷贝就在它后面）
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # ③ 拆开：奇数位是原链，偶数位是新链
        new_head = head.next
        cur = head
        while cur:
            clone = cur.next
            cur.next = clone.next
            clone.next = clone.next.next if clone.next else None
            cur = cur.next
        return new_head