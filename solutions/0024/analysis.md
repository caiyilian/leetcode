# 24. 两两交换链表中的节点 · 解析

## 题目简述

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。**不能修改节点内部的值**，只能进行节点交换。

示例：`1→2→3→4` → `2→1→4→3`；`1→2→3` → `2→1→3`（奇数尾部剩一个不动）。

## 核心套路：dummy 哨兵 + 局部指针交换

交换一对节点需要知道它的**前驱**（改前驱的 next 指向新头）。dummy 哨兵让第一对也有前驱，交换逻辑统一。

一对交换（前驱 p1，两个节点 p2、p3）的三个指针操作：

```python
p2.next = p3.next   # ① 第一个节点指向下一组的起点（防断链）
p3.next = p2        # ② 第二个节点指向第一个（完成本对反转）
p1.next = p3        # ③ 前驱指向第二个（接入已处理部分）
```

## 解法一：用户原版（四指针预初始化 + while True）

```python
class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = p1.next
        p3 = p2.next
        p4 = p3.next          # p4 = 下一组起点
        while True:
            p2.next = p4
            p3.next = p2
            p1.next = p3
            if not (p4 and p4.next):
                break         # 剩余不足 2 个 → 结束
            p1 = p3.next      # 推进到下一组
            p2 = p4
            p3 = p4.next
            p4 = p3.next
        return dummy.next
```

**特点**：p2/p3/p4 循环外初始化，每轮末尾整体推进——"先干再问"，用 `while True + break` 承载退出条件。完全正确（对拍 0 错误）。

## 解法二：标准版（判断进 while，指针现取）

```python
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        p1 = dummy
        while p1.next and p1.next.next:   # 还有 ≥2 个节点就继续
            p2 = p1.next
            p3 = p2.next
            p2.next = p3.next
            p3.next = p2
            p1.next = p3
            p1 = p2                        # 交换后 p2 是下一组的前驱
        return dummy.next
```

**三个配合让它不需要 while True**：

1. **判断在开头**：`while p1.next and p1.next.next` 先确认"至少还有一对"；
2. **指针现取**：p2/p3 循环体内从 p1 现取，无需预初始化（条件已保证它们存在）；
3. **只推进 p1**：交换后 `p1 = p2`（p2 变为下一组前驱），下一轮判断自动处理"下一组起点在哪"——**p4 都被省了**。

## 元知识：两种循环组织模式（本题最值得带走的东西）

| | 先处理后判断 | 先判断后处理 |
|--|-------------|-------------|
| 代码形式 | `while True: ... if 结束: break` | `while 条件: ...` |
| 适用 | 必须执行一轮才能知道状况 | 条件可提前判断 |
| 可读性 | 稍差（break 藏在中部） | 更好（退出条件一眼可见） |

**记忆**：**"先问再干"写 while，"先干再问"用 break**。

链表题 90% 都能组织成"条件可提前判断"，所以标准答案几乎都是 `while 条件` 形式。如果你发现自己写成了 `while True + break`，试着把"结束条件"翻译成循环开头可检查的布尔表达式（本题：`p1.next and p1.next.next`），通常都能搬进 while——这也是"重构"的常见手法。

## 复杂度

- 时间 **O(n)**；空间 **O(1)**。

## 考点

- dummy 哨兵（统一第一对的前驱）
- 局部交换三连（防断链顺序：先接后组、再转本对、最后接前驱）
- **循环组织模式**（while 条件 vs while True + break）
- 奇数长度尾部剩一个不动（剩 0/1 个节点都直接退出）

## 与 25 题 K 个一组反转的关系

24 是 K=2 的特例；25 用"先数够 k 个 → 反转这一段 → 接回"的套路（内部反转是 206 的局部版）。24 吃透后，25 的"段反转 + dummy 接入"就好理解了。