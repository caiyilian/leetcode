# 21. 合并两个有序链表 · 解析

## 题目简述

将两个升序链表合并为一个新的升序链表并返回。新链表通过拼接给定的两个链表的所有节点组成。

示例：`1→2→4` + `1→3→4` → `1→1→2→3→4→4`。

## 解法一：标准双指针归并（面试推荐写法）

**思路**：用 dummy 哨兵解决"结果头是谁"的问题，两个指针各指一条链，**谁小接谁**；一条走完，另一条剩余部分直接接上。

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next
```

**dummy 哨兵**：虚拟头节点，`cur` 从它开始逐个拼接，最后返回 `dummy.next` 就是结果头——省掉"第一个节点从哪来"的分支判断（链表题常用技巧）。

## 解法二：交换头 + 插入法（用户原版）

**思路**：先把较小组头部的链表作为主链（`list1`），然后把 `list2` 的节点**逐个插入** `list1` 的合适位置。

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val > list2.val:        # 交换：保证结果头是整体最小
            list1, list2 = list2, list1
        p1 = list1
        p2 = list2
        while p2:
            if p1.next is None:          # p1 到尾 → 剩余 p2 直接接上
                p1.next = p2
                return list1
            if p1.next.val >= p2.val:    # p2 该插在 p1 和 p1.next 之间
                p3 = p2.next
                p4 = p1.next
                p1.next = p2
                p2.next = p4
                p2 = p3
            else:
                p1 = p1.next             # p2 还应该往后找位置
        return list1
```

**关键不变量**：`p1.val <= p2.val` 全程成立——初始由交换保证；`p1 = p1.next` 只在 `p1.next.val < p2.val` 时发生（前进后 p1.val 仍 < p2.val）。所以 p2 的插入位置一定在 p1 之后、p1.next 之前，无需回头看。

## 两版对比

| | 标准归并版 | 插入法（用户版） |
|--|-----------|----------------|
| 额外节点 | dummy 哨兵（1 个） | 无 |
| 核心操作 | `cur.next = 较小者` | 四指针插入（p1/p2/p3/p4） |
| 复杂度 | O(m+n)/O(1) | O(m+n)/O(1) |
| 口述难度 | 简单 | 需要解释不变量 |
| 理解价值 | 归并思想 | 插入 + 交换头 + 不变量推理 |

**建议**：提交用你的版本（已 0ms/100% 通过）；面试口述用标准版（代码短、好讲）。两者等价，对拍 5 万组 0 差异。

## 复杂度

- 时间 **O(m+n)**；
- 空间 **O(1)**（两版都是指针操作，无新建节点）。

## 考点

- 归并思想（归并排序的合并步骤，21 是它的链表版）
- dummy 哨兵技巧（处理头节点分支）
- 链表插入（断链/重接的顺序：先备份后继再改指针）
- 与 23 合并 K 个升序链表的关系：23 是本题的多路版本（用优先队列/分治）

## 易错点

1. 空链表特判（任一为空直接返回另一个）；
2. 插入/拼接时**先备份后继再改指针**（防断链，206 题的教训）；
3. `cur.next = list1 or list2`：Python 里 `or` 返回第一个真值对象，正好接剩余链（至少一个为 None）；
4. 相等值用 `<=`（稳定性：list1 优先，顺序不影响正确性）。