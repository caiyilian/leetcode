"""25. K 个一组翻转链表（二刷）——分离反转拼接（O(n)/O(1) 最优解）

用户 AC 版（2026-10-20 19:57 提交 755995302，一次通过，0ms/20.1MB）
- 本地先写错一版（漏 prev.next = 新头，每轮丢一个节点），修复后 AC
- 思路：每轮定位本组 [p1..p_last] → 断链反转 → prev.next 接新头 → 新尾接下一组 → prev 前进
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        def reverse_node(head):
            result = None
            p = head
            while p:
                next_node = p.next
                p.next = result
                result = p
                p = next_node
            return result, head  # 头和尾

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        """
        需要有一个prev, p1, p_last, p_next
        prev一开始就是dummy
        """
        while prev.next:
            p1 = prev.next  # prev.next不能为None
            p_last = p1
            for _ in range(k - 1):
                p_last = p_last.next
                if p_last is None:
                    break
            else:  # 没有发生break
                p_next = p_last.next
                # 把p_last的next设置为None
                p_last.next = None
                p1, p_last = reverse_node(p1)
                prev.next = p1          # ★ 关键：prev 接反转后的新头
                p_last.next = p_next    # 新尾接下一组
                prev = p_last           # prev 前进到新尾
                continue
            break
        return dummy.next


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

    print(to_list(s.reverseKGroup(build([1, 2, 3, 4, 5]), 2)))  # [2,1,4,3,5]
    print(to_list(s.reverseKGroup(build([1, 2, 3, 4, 5]), 3)))  # [3,2,1,4,5]
    print(to_list(s.reverseKGroup(build([1, 2, 3, 4, 5]), 1)))  # [1,2,3,4,5]
    print(to_list(s.reverseKGroup(build([1]), 1)))              # [1]
    print(to_list(s.reverseKGroup(build([1, 2, 3, 4]), 3)))     # [3,2,1,4] 尾组不足 k 不动
    print(to_list(s.reverseKGroup(build([1, 2]), 2)))           # [2,1]
    print(to_list(s.reverseKGroup(build([]), 3)))               # []
