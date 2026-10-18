"""160. 相交链表（二刷）——双指针换边法（O(m+n)/O(1) 最优解）

用户 AC 版（2026-10-18 21:34 提交 755587554，WA→AC）
核心：两个指针各走"本链+他链"，路程相等 → 相交必相遇、不相交必同时到 None。
改进：先判空 + while pA is not pB（消除空链表隐藏 bug，更稳）
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# ========== 用户 AC 版（力扣数据范围内正确）==========
class SolutionUser:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA or pB:
            if pA is None:
                pA = headB          # 走到头 → 换到另一条链
            if pB is None:
                pB = headA
            if pA is pB:            # ★ 先判断再移动（WA 教训：先移动会跳过头部交点）
                return pA
            pA = pA.next
            pB = pB.next
        return None


# ========== 标准写法（更稳，推荐）==========
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:      # 任一为空 → 不可能相交
            return None
        pA, pB = headA, headB
        while pA is not pB:             # 不相遇就一直走（条件换边天然处理空链表）
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA                       # 交点 or 同时 None（不相交）


if __name__ == "__main__":
    s = Solution()
    shared = ListNode(8)
    shared.next = ListNode(4)
    shared.next.next = ListNode(5)
    a = ListNode(4); a.next = ListNode(1); a.next.next = shared
    b = ListNode(5); b.next = ListNode(0); b.next.next = ListNode(1); b.next.next.next = shared
    print('相交案例 →', s.getIntersectionNode(a, b).val, '(期望 8)')
    a2 = ListNode(2); a2.next = ListNode(6); a2.next.next = ListNode(4)
    b2 = ListNode(1); b2.next = ListNode(5)
    print('不相交 →', s.getIntersectionNode(a2, b2), '(期望 None)')
    print('空链表 →', s.getIntersectionNode(None, b2), '(期望 None)')