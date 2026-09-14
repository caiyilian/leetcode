# 148. 排序链表 · 解析

## 题目简述

给你链表的头结点 `head`，请将其按**升序**排列并返回排序后的链表。进阶要求：**O(n log n) 时间 + O(1) 常数级空间**。

> 为什么不用快排？链表随机访问 O(1) 不成立，快排的 partition 需要反复遍历；**归并排序天然适合链表**（合并只需改指针）。

## ⏰ 待办：去 B 站看这道题的解析

> **用户标记**：到时候去 B 站看这道题的解析——重点看**自底向上归并**（bottom-up）的实现细节（`_split` 切段 + 逐层合并）。

## 解法一：递归归并（用户版）

**思路**：快慢指针找中点 → 断开成两半 → 递归排序两半 → 合并（复用 21 的插入法）。

```python
class Solution:
    def sortList(self, head):
        if not (head and head.next):
            return head
        return self.half_list(head)

    def half_list(self, head):
        if not head.next:
            return head
        p1 = p2 = head
        p0 = ListNode(0)
        p0.next = head
        while p2 and p2.next:        # 快慢指针找中点，p0 是 p1 的前驱
            p1 = p1.next
            p2 = p2.next.next
            p0 = p0.next
        p0.next = None               # 断开成 [head, p0] 和 [p1, ...]
        return self.mergeTwoLists(self.half_list(head), self.half_list(p1))
```

**正确性**：分治骨架标准（3 万组对拍 0 错误）；**缺点**：递归栈 O(log n) 空间（进阶不达标）+ 插入法合并常数大 + 每层新建哨兵节点 → 力扣 227ms/28%。

## 解法二：自底向上归并（标准最优解，O(1) 空间）

**思想**：不递归！先把链表看成 n 个长度 1 的段，**段长翻倍逐层合并**（1→2→4→…→n），每层遍历整条链两两合并。

```python
class Solution:
    def sortList(self, head):
        n = 0
        p = head
        while p:
            n += 1
            p = p.next                       # ① 数长度

        dummy = ListNode(0, head)
        step = 1
        while step < n:                      # ② 段长翻倍
            prev, cur = dummy, dummy.next
            while cur:
                left = cur                   # 第一段
                right = self._split(cur, step)   # 第二段
                cur = self._split(right, step)   # 剩余部分
                prev.next = self._merge(left, right)  # 合并
                while prev.next:
                    prev = prev.next         # prev 移到合并末尾
            step *= 2
        return dummy.next

    def _split(self, head, step):            # 切出前 step 个节点，断开，返回剩余链头
        for _ in range(step - 1):
            if head:
                head = head.next
        if not head:
            return None
        rest = head.next
        head.next = None
        return rest

    def _merge(self, l1, l2):                # 标准双指针归并（21 题标准版）
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
```

**为什么达标**：
- 无递归 → **O(1) 空间** ✅（进阶要求）；
- 每层 O(n) × log n 层 = **O(n log n)** ✅；
- 无递归调用开销、无每层 new 节点 → 常数小，实测比递归版快。

**核心动作** `_split(head, step)`：数 step 个节点后断开，返回后半段——这是自底向上的灵魂（递归版靠"断开一次"，它靠"反复切段"）。

## 复杂度对比

| | 递归版 | 自底向上版 |
|--|--------|-----------|
| 时间 | O(n log n) | O(n log n)（常数更小） |
| 空间 | O(log n) 栈 ❌ | **O(1)** ✅ |

## 考点

- **归并排序是链表排序的正解**（快排/堆排不适合链表的随机访问）
- 递归 vs 自底向上（空间差异 + 常数差异）
- 快慢指针找中点（234 学过的套路复用）
- 21 合并有序链表的复用（两种 merge 风格：插入法 vs 双指针）
- 段切割 `_split`（自底向上的关键动作）

## 易错点

1. 递归版：断开链表必须用**中点的前驱**（p0），否则断错位置；
2. 自底向上版：每层合并后 prev 要移到合并结果末尾（`while prev.next`），否则下一段合并接错；
3. `_split` 切段后必须 `head.next = None`（断开），否则合并时出现环；
4. 段长超过剩余长度时 `_split` 返回 None（`if not head` 兜底）。