# 287. 寻找重复数 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 287. 寻找重复数（Find the Duplicate Number）· 中等（快慢指针/Floyd 判圈） |
| 链接 | https://leetcode.cn/problems/find-the-duplicate-number/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 59/59 用例通过**（leetgo 复提交） |
| 运行时间 | 34 ms |
| 内存 | 33.1 MB |

## 解法（用户快慢指针，Floyd 判圈）

```python
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:              # 第一阶段：找相遇点
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0                         # 第二阶段：slow 回起点
        while slow != fast:              # 同速走，再次相遇点 = 环入口 = 重复数
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

## 核心：数组 → 链表的转化

把 `nums[i]` 看成"节点 i 指向节点 nums[i]"，数组就变成一张带环的图：
- 有重复数 → 两个不同节点指向同一个节点 → **成环**；
- 环入口就是那个被指向两次的数 = **重复数**。

**这正是 142 环形链表 II 的数组版**（用户已 AC 142）——快慢指针两阶段：找相遇点 → slow 回起点同速走，再次相遇即环入口。

## 复杂度与进阶要求

- 时间 **O(n)**；空间 **O(1)** —— 满足 287 的"不用额外空间、不修改数组"进阶要求（哈希表 O(n) 空间不达标）。

## 验证

- 对拍 **5 万组随机数组 vs 哈希 0 不一致**；
- 样例：`[1,3,4,2,2]→2`、`[3,1,3,4,2]→3`、`[3,3,3,3,3]→3`（全重复边界）。

## 复杂度

- 时间 **O(n)**；空间 O(1)。