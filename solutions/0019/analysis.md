# 19. 删除链表的倒数第 N 个结点 · 解析

## 题目简述

给你一个链表，删除链表的**倒数第 n 个结点**，并且返回链表的头结点。进阶要求：**一趟扫描**实现。

示例：`[1,2,3,4,5], n=2` → `[1,2,3,5]`。

## 核心套路：快慢指针（一趟扫描）

**思想**：让快指针先走 n 步，然后快慢指针**同步**走——当快指针到末尾时，慢指针恰好停在"待删节点的前一个"。这样**不用知道链表长度**，一趟搞定。

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        p_fast = head
        p_slow = head
        for _ in range(n):           # ① fast 先走 n 步
            p_fast = p_fast.next
        if p_fast is None:           # ② 删头特判：fast 一步走到 None，说明长度 == n
            return head.next
        while p_fast.next:           # ③ 同步走，fast 到"最后一个节点"时停止
            p_slow = p_slow.next
            p_fast = p_fast.next
        p_slow.next = p_slow.next.next  # ④ 跳过待删节点
        return head
```

### 为什么"fast 先走 n 步"就能定位？

fast 与 slow 的**距离恒为 n 个节点**。当 fast 到末尾时：

```
fast 在末尾（倒数第 1 个）      → slow 在倒数第 n+1 个 = 待删节点的前一个 ✅
```

删头情况（`length == n`）：fast 先走 n 步后直接是 None → 待删节点就是 head → 返回 `head.next`。

### 与标准 dummy 版的差异（用户版 vs 标准版）

| | 用户 v2（无 dummy） | 标准版（dummy 哨兵） |
|--|--------------------|--------------------|
| 删头处理 | `p_fast is None → return head.next` 特判 | dummy 让删头变成普通删除，无特判 |
| 哨兵节点 | 无 | `dummy = ListNode(0, head)` |
| 停点 | `while p_fast.next`（fast 到最后一个节点） | `while fast`（fast 到 None） |
| 复杂度 | O(n)/O(1) | O(n)/O(1) |

**两者等价**。用户 v2 是"删头特判"流派，标准版是"哨兵统一"流派——面试写标准版（少一个分支），理解用用户版（不变量直观）。

## 标准版（dummy 哨兵，面试推荐）

```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
```

**dummy 哨兵**：虚拟头节点指向 head，fast/slow 都从 dummy 出发——删头时 `slow.next = slow.next.next` 天然正确（slow 是 dummy，删除 head），无需特判。这就是"哨兵统一边界"的经典价值（21 合并、25 K 组反转都会用）。

## 复杂度

- 时间 **O(n)**：一趟扫描（v2 满足进阶要求；v1 两遍也 O(n) 但常数更大）；
- 空间 **O(1)**：两个指针（dummy 版多一个哨兵节点，常数级）。

## 考点

- 快慢指针（"超前 n 步"定位倒数第 n 个——本题灵魂）
- dummy 哨兵统一删头边界
- 删头/删尾/单节点三个边界
- 与 206/234/141 的快慢指针家族：找中点、判环、定位倒数——同一个工具不同玩法

## 易错点

1. **删头**：`length == n` 或 `p_fast is None` 时返回 `head.next`（漏了会 IndexError/删错）；
2. **单节点** `[1] n=1`：返回空链表；
3. fast 先走的步数：用户版 n 步 + 特判；dummy 版 n+1 步（因为从 dummy 出发）——**别搞混两种写法的步数**；
4. 删除操作是 `slow.next = slow.next.next`（改前一个的指针），不是删 slow 自己。