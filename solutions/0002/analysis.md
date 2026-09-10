# 2. 两数相加 · 解题解析

## 一句话思路

链表是**逆序**存储数字（个位在头节点），所以两个链表头对齐正好是个位对齐——像竖式加法一样，**同位相加 + 处理进位**，逐节点推进。

## 核心洞察

三个"尾巴"要同时照顾：`l1` 还没走完、`l2` 还没走完、**进位还没清零**。所以循环条件写成 `while l1 or l2 or carry`，三者任一存在就继续建节点，保证最高位的进位（如 999+1=1000 的多出一个 1）不被丢掉。

## 实现

```python
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, val = divmod(total, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next
```

- **时间复杂度**：O(max(m, n))，遍历较长链表
- **空间复杂度**：O(1)（不含返回结果），只用了 dummy + 游标 + 进位
- **易错点**：
  1. 循环条件漏掉 `or carry` —— 最后一位进位（如 5+5=10）会丢失
  2. `divmod(total, 10)` 一步拿到「进位」和「本位值」，别手写 `%` `/` 忘了顺序
  3. 用 `dummy` 哨兵节点，避免头节点特殊处理；返回 `dummy.next`

## 本题考点

| 考点 | 内容 |
|------|------|
| 链表遍历 | 同步推进两个链表，允许不等长 |
| 进位处理 | carry 参与每轮求和，并作为循环继续条件 |
| 哨兵节点 | dummy 简化头节点创建逻辑 |

## 提交记录

- 本地测试：3/3 通过
- 服务器提交：**1569/1569 通过**（隐藏用例全部通过）
- 性能：Runtime 4 ms（击败 44%）、Memory 19.3 MB（击败 7%）