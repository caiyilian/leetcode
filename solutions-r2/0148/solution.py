"""148. 排序链表（二刷）——归并排序（自顶向下递归版）

用户 AC 版（2026-10-20 21:32 提交 756019973，一次通过，276ms/39.8MB）
- 快慢指针找中点切两半 → 递归排序 → 两有序链合并（merge_node = 21 题哨兵归并）
- 插曲：忘写 if not head: return head → 空链表 AttributeError → 补上后 AC
- 注意：递归栈 O(log n)，严格讲不满足进阶 O(1) 空间（一刷归档有自底向上归并 O(1) 版）
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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


if __name__ == "__main__":
    s = Solution()

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

    print(to_list(s.sortList(build([4, 2, 1, 3]))))       # [1,2,3,4]
    print(to_list(s.sortList(build([-1, 5, 3, 4, 0]))))   # [-1,0,3,4,5]
    print(to_list(s.sortList(build([]))))                 # []
    print(to_list(s.sortList(build([1]))))                # [1]
    print(to_list(s.sortList(build([2, 1]))))             # [1,2]
