# 142. 环形链表 II · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 142. 环形链表 II（Linked List Cycle II）· 中等 |
| 链接 | https://leetcode.cn/problems/linked-list-cycle-ii/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 18/18 用例通过** |
| 运行时间 | 62 ms（leetgo 提交，击败 39%） |
| 内存 | 22 MB（击败 54%） |

## 解法

用户独立的**快慢指针 + 二次相遇**（141 的进阶版）：

```python
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        p_fast = head
        p_slow = head
        p_start = head
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                while True:
                    if p_slow == p_start:   # ⚠️ 必须先判断再移动！
                        return p_slow
                    p_slow = p_slow.next
                    p_start = p_start.next
        return None
```

- 时间 **O(n)**、空间 **O(1)**——双最优；
- 对拍 3 万组（无环 + 各种 pos）0 错误。

## ⚡ 重点标记：步数可以是 0（用户要求面试前重点看）

**"相遇后两个指针各走 a 步到入口，而 a 可以是 0"**——当 head 本身就在环入口（如 `[1,2] pos=0`，`1→2→1`）时：

- **先判断后移动**：`p_slow == p_start` 一开始就成立 → 直接返回入口 ✅（正确）；
- **先移动后判断**：先走一步都到节点 2 → 返回 2 ❌（错，漏了"走 0 步"的情况）。

**结论：必须"先判断再移动"**（或写成 `while p_slow != p_start: 移动`——while 条件本身就是先判断）。相遇点可能就是入口，**"走 0 步"也是答案**。

## 踩坑记录

- leetgo manual question（第二次）：`__main__` 多了 `pos` 参数需修正；本地 Skipped 正常，以在线为准。