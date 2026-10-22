"""148. 排序链表（二刷）——双解法：递归归并（主）+ 自底向上归并 O(1)（进阶）

用户 AC 版（2026-10-20 21:32 提交 756019973，一次通过，276ms/39.8MB）
- 快慢指针找中点切两半 → 递归排序 → 两有序链合并（merge_node = 21 题哨兵归并）
- 插曲：忘写 if not head: return head → 空链表 AttributeError → 补上后 AC
- 注意：递归栈 O(log n)，严格讲不满足进阶 O(1) 空间

附：自底向上归并 O(1)（力扣进阶）——段长 1→2→4 逐层翻倍，全程迭代无递归栈
① 数长度 n  ② 每层 split 切段断开 + merge 合并 + prev 推进  ③ step*=2 直到 >= n
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ========== 用户 AC 版：自顶向下递归归并（O(n log n)/O(log n)） ==========
class SolutionRecursive:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针，使得慢指针指向右边一半
        """
        if not head:
            return head

        def get_half(p):
            p_slow = p
            p_fast = p
            prev = p
            while p_fast and p_fast.next:
                p_fast = p_fast.next.next
                prev = p_slow
                p_slow = p_slow.next
            prev.next = None          # 切断成两条链 [p..prev] 和 [p_slow..]
            return p, p_slow          # 头和尾（右半头）

        def merge_node(p1, p2):
            # 合并两个升序链表（21 题哨兵归并）
            dummy = ListNode(0)
            curr = dummy
            while p1 and p2:
                if p1.val > p2.val:
                    curr.next = p2
                    p2 = p2.next
                else:
                    curr.next = p1
                    p1 = p1.next
                curr = curr.next
            # 其中一个为None
            if p1:
                curr.next = p1
            else:
                curr.next = p2
            return dummy.next

        def fun(p):
            if p.next is None:        # 单节点天然有序
                return p
            p_head, p_tail = get_half(p)
            p_head = fun(p_head)      # 左半排序
            p_tail = fun(p_tail)      # 右半排序
            return merge_node(p_head, p_tail)

        return fun(head)


# ========== 自底向上归并 O(1)（力扣进阶，一刷标准版） ==========
class SolutionBottomUp:
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
        head.next = None          # 断开！（不切断 merge 会并到整条链尾）
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


# 默认用用户版
Solution = SolutionRecursive


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

    for s in (SolutionRecursive(), SolutionBottomUp()):
        print(to_list(s.sortList(build([4, 2, 1, 3]))))       # [1,2,3,4]
        print(to_list(s.sortList(build([-1, 5, 3, 4, 0]))))   # [-1,0,3,4,5]
        print(to_list(s.sortList(build([]))))                 # []
        print(to_list(s.sortList(build([1]))))                # [1]
        print(to_list(s.sortList(build([2, 1]))))             # [1,2]
