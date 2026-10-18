"""234. 回文链表（二刷）——三段式组合拳（O(n)/O(1) 最优解）

用户 AC 版（2026-10-18 22:39 提交 755600761，一次通过）
① 快慢指针找中点 → ② 反转后半段（复用 206）→ ③ 前半后半逐节点比较
"""

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # ① 快慢指针找中点（慢指针最终在右半段头）
        p_slow = head
        p_fast = head
        while p_fast and p_fast.next:
            p_slow = p_slow.next
            p_fast = p_fast.next.next
        # ② 反转后半段（复用 206 的 reverseList）
        p_fast = head
        p_slow = self.reverseList(p_slow)
        # ③ 前半 vs 反转后的后半，逐节点比较
        while p_slow:
            if p_slow.val != p_fast.val:
                return False
            p_slow = p_slow.next
            p_fast = p_fast.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = None
        while p1:
            p3 = p1.next
            p1.next = p2
            p2 = p1
            p1 = p3
        return p2


if __name__ == "__main__":
    s = Solution()

    def build(vals):
        d = ListNode(0)
        cur = d
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return d.next

    print(s.isPalindrome(build([1, 2, 2, 1])))     # True
    print(s.isPalindrome(build([1, 2, 3, 2, 1])))  # True
    print(s.isPalindrome(build([1, 2])))           # False
    print(s.isPalindrome(build([])))               # True