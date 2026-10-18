"""206. 反转链表（二刷）——三指针迭代反转（O(n)/O(1) 最优解）

用户 AC 版（2026-10-18 22:05 提交 755594180，一次通过）
核心：p1 当前节点、p2 已反转链头、p3 暂存 p1 的后继；每次把 p1.next 指回 p2。
"""

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = None              # 已反转部分的头（初始 None）
        while p1:
            p3 = p1.next       # ① 暂存后继（否则断了找不回）
            p1.next = p2       # ② 当前节点反向指向前一个
            p2 = p1            # ③ 已反转头前移
            p1 = p3            # ④ p1 前进到原后继
        return p2              # 遍历完 p2 指向原链尾 = 新链头


if __name__ == "__main__":
    s = Solution()

    def build(vals):
        d = ListNode(0)
        cur = d
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next

    def to_list(h):
        res = []
        while h:
            res.append(h.val)
            h = h.next
        return res

    print(to_list(s.reverseList(build([1, 2, 3, 4, 5]))))  # [5,4,3,2,1]
    print(to_list(s.reverseList(build([]))))                # []
    print(to_list(s.reverseList(build([1]))))               # [1]