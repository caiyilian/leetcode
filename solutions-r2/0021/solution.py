"""21. 合并两个有序链表（二刷）——哨兵 + 循环逐个接（O(n+m)/O(1) 最优解）

用户 AC 版（2026-10-19 11:30 提交 755659539，一次通过，0ms/19.3MB）
- 哨兵节点 result 统一"第一个插谁"的讨论（无需特判空头）
- while list1 or list2：任一为空就整个接另一个，都不为空就比 val 小的接上
- 与一刷"交换头+插入法"不同：本版是标准哨兵归并，更通用（23 题分治也用它）
"""

from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # 哨兵
        result = ListNode(0)
        p = result
        """
        对比list1和list2的值，小的，result.next = list
        list = list.next
        然后继续，如果某一个为None，那就只看另一个
        """
        while list1 or list2:
            if list1 is None:
                result.next = list2
                list2 = list2.next
            elif list2 is None:
                result.next = list1
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    result.next = list1
                    list1 = list1.next
                else:
                    result.next = list2
                    list2 = list2.next
            result = result.next
        return p.next


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

    # 手工用例：等长 / 一空 / 全空 / 全小在前 / 全大在后 / 重复值
    print(to_list(s.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))  # [1,1,2,3,4,4]
    print(to_list(s.mergeTwoLists(build([]), build([0]))))                # [0]
    print(to_list(s.mergeTwoLists(build([]), build([]))))                 # []
    print(to_list(s.mergeTwoLists(build([1, 2, 3]), build([4, 5]))))     # [1,2,3,4,5]
    print(to_list(s.mergeTwoLists(build([4, 5]), build([1, 2, 3]))))     # [1,2,3,4,5]