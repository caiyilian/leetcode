# 206. 反转链表 · 解析

## 题目简述

给你单链表的头节点 `head`，请你反转链表，并返回反转后的链表头。

示例：`1→2→3→4→5` → `5→4→3→2→1`。

## 核心套路：三指针迭代反转（O(1) 空间）

链表反转的本质是**逐个把每个节点的 `next` 指向前一个节点**。需要三个指针：

```
p1 = 当前节点（正在改 next）
p2 = 下一个节点（保存后继，防止断链后丢失）
p3 = 前一个节点（当前节点的 next 应该指向它）
```

每一步：

```python
p1.next = p3     # 当前节点指向前一个（完成反转这一步）
p3 = p1          # 前一个指针前进
p1 = p2          # 当前指针前进
p2 = p2.next     # 下一个指针前进（这里注意 p2 可能为 None → 循环终止）
```

**为什么需要 p2**：`p1.next = p3` 会切断 p1 与后面的连接，如果不先用 p2 记住后继，链表就断了——这是链表题的第一原则：**改指针前先备份后继**。

## 定稿解法

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head                      # 空链表特判（必须！）
        p1 = head
        p2 = p1.next
        p3 = None

        while True:
            p1.next = p3                     # 反转当前指针
            if p2 is None:
                break                        # p1 已是原链表末尾（新链表头）
            p3 = p1
            p1 = p2
            p2 = p2.next
        return p1
```

### 边界处理

| 场景 | 行为 | 说明 |
|------|------|------|
| 空链表 `[]` | `return head`（None） | **必须特判**——没有特判时 `p1.next` 会 AttributeError（本项目实战踩坑） |
| 单节点 `[1]` | `p2 = None` → 循环第一次 `p1.next = None` 后 `p2 is None` break → 返回 p1 | 天然正确 |
| 多节点 | 正常三指针推进 | — |

**链表题的第一习惯：动手前先检查 head 是否为空。**

## 复杂度

- 时间 **O(n)**：每个节点恰好一次；
- 空间 **O(1)**：三个指针（迭代版）。

## 递归版（面试常问的对比）

```python
def reverseList(self, head):
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)  # 先反转后面的
    head.next.next = head                    # 让后继指向自己
    head.next = None                         # 自己指向 None
    return new_head
```

- 时间 O(n)，空间 **O(n)**（递归栈）——面试时通常要求两个版本都会，迭代优先（空间更优）；
- 递归的思想：**假设后面已经反转好了，只需让 head 的下一个节点指回 head**。

## 考点

- 改指针前备份后继（防断链）
- 空链表/单节点边界（链表题默认习惯）
- 迭代 vs 递归（空间对比）
- 206 是链表地基：234 回文链表、25 K 组反转、92 反转区间都建立在它的基础上

## 易错点

1. **漏空链表特判** → AttributeError（本项目真实踩过）；
2. `p2 = p2.next` 放在 `p1 = p2` 之后，用的是 p2 的旧值——顺序不能反；
3. 忘记 `p1.next = p3` 在 p2 为 None 的那一步也要执行（当前代码 while True 结构天然覆盖）；
4. 返回的是 `p1`（原链表末尾 = 新链表头），不是 p3/p2。