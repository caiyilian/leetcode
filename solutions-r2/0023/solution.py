"""23. 合并 K 个升序链表（二刷）——分治两两合并 + 原地紧凑（O(N log k)/O(1)）

用户 AC 版（2026-10-22 16:39 提交 756364203，一次通过，8ms/22.3MB）
- merge2 = 21 题哨兵归并（直接复用）
- 分治：每轮两两合并把 k 减半，共 log k 轮 → O(N log k)
- 原地紧凑：合并结果放 lists[i]，奇数个时把最后一条搬到中间位，length 动态收缩
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        length = len(lists)

        def merge2(p1, p2):
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
            if p1:
                curr.next = p1
            else:
                curr.next = p2
            return dummy.next

        while length > 1:
            for i in range((length) // 2):
                lists[i] = merge2(lists[2 * i], lists[2 * i + 1])

            if length % 2 == 1:  # 奇数：最后一条搬到中间位，length = 1 + length//2
                lists[(length) // 2] = lists[length - 1]
                length = 1 + length // 2
            else:
                length = length // 2
        return lists[0]


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

    print(to_list(s.mergeKLists([build([1, 4, 5]), build([1, 3, 4]), build([2, 6])])))  # [1,1,2,3,4,4,5,6]
    print(s.mergeKLists([]))                                                            # None
    print(to_list(s.mergeKLists([build([])])))                                          # []
    print(to_list(s.mergeKLists([build([1, 2, 3])])))                                   # [1,2,3]
    print(to_list(s.mergeKLists([build([1]), build([0])])))                             # [0,1]