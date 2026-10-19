"""2. 两数相加（二刷）——原地相加 + 前驱接尾（O(n)/O(1) 最优解，主版）

用户 AC 版（2026-10-19 20:21 提交 755780264，一次通过，0ms/19.2MB）
- 修 bug 前：测试用例3（9999999+9999）少最高位 1 → 加 prev 前驱修复；
- 对拍又抓到一个力扣没测出的隐藏 bug：l1 为空时 prev 未定义 → UnboundLocalError。
  本归档版补了空链表守卫（if not l1 / if not l2），3 万组对拍 0 不一致。
- 思路：两个 while 分别处理"共有位数"和"剩余位数"，prev 记录前驱用于拼接/接最终进位
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ========== 用户 AC 版（补空链表守卫）==========
class SolutionUser:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        flag = 0
        p = l1
        while l1 and l2:
            l1.val += l2.val + flag
            if l1.val > 9:
                flag = 1
                l1.val = l1.val % 10
            else:
                flag = 0
            prev = l1
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            prev.next = l2
            l1 = l2
        while l1:
            l1.val += flag
            if l1.val > 9:
                flag = 1
                l1.val = l1.val % 10
            else:
                flag = 0
            prev = l1
            l1 = l1.next
        if flag:
            prev.next = ListNode(1)
        return p


# ========== 标准哨兵版（官方范式，力扣主推）==========
class SolutionStandard:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            v = carry
            if l1:
                v += l1.val
                l1 = l1.next
            if l2:
                v += l2.val
                l2 = l2.next
            cur.next = ListNode(v % 10)
            cur = cur.next
            carry = v // 10
        return dummy.next


# 测试用别名
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

    for s in (SolutionUser(), SolutionStandard()):
        print(to_list(s.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))))     # [7,0,8]
        print(to_list(s.addTwoNumbers(build([0]), build([0]))))                  # [0]
        print(to_list(s.addTwoNumbers(build([9, 9, 9, 9, 9, 9, 9]), build([9, 9, 9, 9]))))  # [8,9,9,9,0,0,0,1]
        print(to_list(s.addTwoNumbers(build([1, 2, 3]), build([4, 5, 6, 7, 8]))))  # [5,7,9,7,8]
        print(to_list(s.addTwoNumbers(build([]), build([5]))))                  # [5]
        print(to_list(s.addTwoNumbers(build([]), build([]))))                   # []
