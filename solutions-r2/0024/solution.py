"""24. 两两交换链表中的节点（二刷）——三指针 + dummy（O(n)/O(1) 最优解）

用户 AC 版 + 微优化（2026-10-19 21:00 提交 755792205，一次通过，0ms/19.1MB）
- 原版：while prev and prev.next + 循环内 `if p2 is None: break`
- 优化：把 break 并进 while 条件 `while prev.next and prev.next.next`（用户的直觉是对的），
  同时 prev 永不为 None 不用检查；逻辑等价、代码更干净
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ========== 用户 AC 版（优化 break 后）==========
class SolutionUser:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:  # 有 p1 且 p2 才交换（break 并入条件）
            p1 = prev.next
            p2 = p1.next
            prev.next = p2
            p1.next = p2.next
            p2.next = p1
            prev = p1
        return dummy.next


# ========== 递归版（官方另一种范式，空间 O(n)）==========
class SolutionRecursive:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        nxt = head.next
        head.next = self.swapPairs(nxt.next)  # 递归交换后面的
        nxt.next = head
        return nxt


Solution = SolutionUser

if __name__ == "__main__":
    def build(vals):
        d = ListNode(0)
        cur = d
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next

    def to_list(head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res

    for s in (SolutionUser(), SolutionRecursive()):
        print(to_list(s.swapPairs(build([1, 2, 3, 4]))))   # [2,1,4,3]
        print(to_list(s.swapPairs(build([]))))              # []
        print(to_list(s.swapPairs(build([1]))))             # [1]
        print(to_list(s.swapPairs(build([1, 2, 3]))))       # [2,1,3] 奇数