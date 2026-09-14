# 25. K 个一组翻转链表 · 解析

## 题目简述

给你链表的头节点 `head`，每 **k 个节点一组**进行翻转，返回修改后的链表。k 是正整数；**不足 k 个的尾部保持原样**。进阶要求：O(1) 额外空间。

示例：`[1,2,3,4,5], k=2` → `[2,1,4,3,5]`；`k=3` → `[3,2,1,4,5]`。

## 核心套路：206 局部反转 + dummy + 先判断后处理

这道困难题 = 你已经会的三样东西组合：

1. **206 三指针反转**（整条链 → 截断到一段）；
2. **dummy 哨兵**（统一第一组的前驱，24 题学过）；
3. **先判断后处理**（"够不够 k 个"放循环开头，24 题元知识）。

## 定稿解法（用户版）

```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not (head and head.next and k != 1):
            return head
        dummy = ListNode(0)
        dummy.next = head
        p_prev = dummy        # 上一组末尾（前驱）
        p_now_last = head     # 当前组末尾游标
        while p_now_last and p_now_last.next:
            for _ in range(k - 1):           # ① 定位本组末尾
                if not (p_now_last and p_now_last.next):
                    return dummy.next         #   不足 k 个 → 原样返回
                p_now_last = p_now_last.next
            p_next = p_now_last.next          # ② 记录下一组头
            p_now_last.next = None            # ③ 断开本组
            p_prev.next, p_now_last = self.reverse_list(p_prev.next)  # ④ 反转
            p_now_last.next = p_next          # ⑤ 新尾接下一组
            p_prev = p_now_last               # ⑥ 前驱前进
            p_now_last = p_next               #    游标移到下一组头
        return dummy.next

    def reverse_list(self, head):
        if not (head and head.next):
            return head
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev, head      # 返回 (新头, 原头=新尾) ← 关键设计
```

### 关键设计：`reverse_list` 返回 `(新头, 新尾)`

反转**一段**和反转整条链的区别：光返回新头不够，**还得知道段尾是谁**（它要接下一组）。

- 反转前记录 `head`（原段头）——反转后它恰好就是**段尾**（新尾）；
- 返回 `(prev, head)`：`prev`（反转后的头）接给 `p_prev`，`head`（新尾）接给 `p_next`；
- **一个指针零额外开销拿到两个信息**——这是段间连接的钥匙。

### 为什么"不足 k 个"能在 for 循环里拦下

`for _ in range(k-1)` 每步检查 `p_now_last and p_now_last.next`——走到一半发现 next 为 None（不够 k 个）就 `return dummy.next`（已处理的部分保持，剩余保持原样）。**先判断后处理**，不需要单独数长度。

## 复杂度

- 时间 **O(n)**：每个节点访问常数次（定位 k-1 步 + 反转 k 个，两段不重叠、不重复扫）；
- 空间 **O(1)**：只有指针变量——**满足进阶要求**（递归版 O(n/k) 栈不达标）。

## 考点

- 局部反转 + 段间连接（206 + 24 的组合拳）
- `(新头, 新尾)` 双返回值设计（Python 元组解包的优雅应用）
- dummy 哨兵统一前驱
- 先判断后处理（不足 k 个的提前返回）
- 与 24 题（k=2 特例）、148 排序链表（段分割思想）的联系

## 易错点

1. **断链顺序**：先记录 `p_next` 再断开（`p_now_last.next = None`），否则下一组丢失；
2. 反转的是 `p_prev.next`（本组原头），不是 `p_now_last`；
3. `p_prev = p_now_last` 要在元组解包**之后**（此时 p_now_last 已是新尾）；
4. k=1 不反转（特判 `k != 1`）；k 大于长度时 for 循环中途返回原样；
5. `reverse_list` 单节点分支返回 `head` 而非元组——本组长度 ≥k≥2 保证永远不会走到，逻辑自洽（不用改，但要知道）。