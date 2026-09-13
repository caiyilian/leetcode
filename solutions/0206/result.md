# 206. 反转链表 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 206. 反转链表（Reverse Linked List）· 简单 |
| 链接 | https://leetcode.cn/problems/reverse-linked-list/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 28/28 用例通过** |
| 运行时间 | **0 ms（击败 100%）**，网页提交与 leetgo 提交均复现 |
| 内存 | 20.3 MB |

## 解法

用户独立的**三指针迭代反转**（p1 当前 / p2 下一个 / p3 前一个）：

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

- 时间 **O(n)**：每个节点恰好处理一次；
- 空间 **O(1)**：三个指针变量（迭代版，无递归栈）。

## 踩坑记录（本次的宝贵教训）

**第一版提交 AttributeError**：`p2 = p1.next` 在**空链表**（`head = None`）时崩溃——力扣测试用例含空链表。修复只需一行空链表特判 `if not head: return head`（单节点天然正确：`p2=None` 进循环后立即 break 返回 p1）。

教训：**链表题第一件事永远是检查 head 为 None**（以及单节点场景），这是链表题的默认边界习惯。

## 复杂度

- 时间 **O(n)**；空间 **O(1)**（迭代版，不适用递归的 O(n) 栈）。