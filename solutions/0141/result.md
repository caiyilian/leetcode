# 141. 环形链表 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 141. 环形链表（Linked List Cycle）· 简单 |
| 链接 | https://leetcode.cn/problems/linked-list-cycle/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 29/29 用例通过** |
| 运行时间 | 60 ms（leetgo 提交，击败 57%） |
| 内存 | 22.2 MB（击败 58%） |

## 解法

用户独立的**快慢指针追及**：

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        p_fast = head
        p_slow = head
        while p_fast and p_fast.next:
            p_fast = p_fast.next.next
            p_slow = p_slow.next
            if p_fast == p_slow:
                return True
        return False
```

- 快指针每次 2 步、慢指针每次 1 步——**有环时相对速度 1 步/轮，快指针必然追上慢指针**（环内追及）；无环时快指针走到 None；
- 时间 **O(n)**（无环 O(n)，有环 ≤ O(n+k) 相遇）、空间 **O(1)**——双最优，优于 set 记节点（O(n) 空间）。

## 踩坑记录（leetgo manual question）

- 模板 `__main__` 多了 `pos` 参数（力扣实际签名只有 `head`），需修正；
- **本地测试 Case 2 报错属正常**：leetgo 本地反序列化不会真正按 `pos` 构建环（节点不闭环），严格比对失败；**在线测试 true/true/false 全对、提交 29/29 通过——以在线为准**（manual question 的生成测试代码本来就标了 incorrect）。

对拍 3 万组（无环 + 各种环入口 pos）0 错误，边界（单节点自环等）全过。