# 234. 回文链表 · 解析

## 题目简述

给你一个单链表的头节点 `head`，请你判断该链表是否为回文链表（正着读、倒着读一样）。进阶要求：O(n) 时间 + **O(1) 额外空间**。

示例：`1→2→2→1` → true；`1→2` → false。

## 核心套路：三段式组合拳（O(1) 空间最优解）

链表没法像数组一样直接从两端往中间比，所以思路是**把后半段反转，再和前半段比**：

```
① 找中点（快慢指针）
② 反转后半段（206 的三指针反转）
③ 前半段 vs 反转后的后半段，逐节点比较
```

## 定稿解法

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p_fast = head
        p_slow = head
        while (p_fast and p_fast.next):      # ① 快慢指针找中点
            p_fast = p_fast.next.next
            p_slow = p_slow.next
        p_slow = self.reverse_list(p_slow)   # ② 反转后半段
        p_fast = head
        while p_slow:                        # ③ 前半段 vs 反转后半段
            if p_fast.val != p_slow.val:
                return False
            p_fast = p_fast.next
            p_slow = p_slow.next
        return True

    def reverse_list(self, head):            # 206 的三指针反转
        if not head:
            return head
        p1 = head
        p2 = p1.next
        p3 = None
        while True:
            p1.next = p3
            if p2 is None:
                break
            p3 = p1
            p1 = p2
            p2 = p2.next
        return p1
```

## 关键细节：快慢指针的奇偶行为（本题最大的坑）

```python
while (p_fast and p_fast.next):
    p_fast = p_fast.next.next
    p_slow = p_slow.next
```

| 链表长度 | 快指针终点 | 慢指针位置 |
|---------|-----------|-----------|
| 偶数（如 4） | 走到 **None**（`p_fast` 为 None 退出） | 后半段起点（第 3 个节点） |
| 奇数（如 5） | 走到**最后一个节点**（`p_fast.next` 为 None 退出） | 正中节点 |

- **为什么奇数时不能继续走**：再走一步 `p_fast.next.next` 会越界崩溃——所以条件必须同时检查 `p_fast` 和 `p_fast.next`；
- **奇数时中间节点自比无害**：反转后半段后中间节点在末尾，和它自己比较永远相等，不影响判断（`1→2→1`：反转 `2→1` 得 `1→2`，比较 `1==1`、`2==2` ✅）。

## 复杂度

- 时间 **O(n)**：找中点 O(n/2) + 反转 O(n/2) + 比较 O(n/2)；
- 空间 **O(1)**：三个指针——满足进阶要求（比"转成数组再比"的 O(n) 空间高一档）。

## 考点

- **快慢指针找中点**（链表双指针经典套路，141/142 环形链表也用）
- 反转链表（206）的复用
- 奇数/偶数长度的统一处理（`while p_fast and p_fast.next` 一个条件覆盖两种）
- 空间进阶：O(1) vs "数组复制" O(n)
- 破坏性问题：反转后半段修改了原链表结构（本题允许；面试可提"不修改链表"的变体思路——递归/栈）

## 易错点

1. 快慢指针条件写错（只写 `while p_fast` 或 `while p_fast.next`）→ 奇数越界或偶数提前停；
2. 反转后忘记重新让 p_fast 从头开始（要用 `p_fast = head` 复位）；
3. 反转的是 `p_slow` 而不是 `p_slow.next`（要连中间节点一起反转，奇数才正确）；
4. 空链表特判（力扣约束非空，但 `if not head` 是链表题习惯）。