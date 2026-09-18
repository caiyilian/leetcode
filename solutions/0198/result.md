# 198. 打家劫舍 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 198. 打家劫舍（House Robber）· 中等（动态规划分类第 3 题） |
| 链接 | https://leetcode.cn/problems/house-robber/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 70/70 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.2 MB |

## ⚠️ 失败记录（用户要求）

| 提交 | 结果 | 问题 |
|------|------|------|
| 750091058 | **TLE** | 纯递归无记忆化：`max_money(n-2)/max_money(n-3)` 被重复算指数次 → O(2ⁿ) |
| 750092536 | **AC** | 加 `mem` dict 记忆化 → O(n) |

**这是 70 爬楼梯"递归 → 记忆化"的实战应验**——用户几小时前学的技巧在 198 自动用出。

## 解法（用户记忆化递归版 + 标准滚动变量版）

**用户版**（top-down，枚举"最后偷哪家"）：

```python
def rob(self, nums):
    length = len(nums)
    if length == 1: return nums[0]
    mem = {1: nums[0], 2: max(nums[:2])}
    def max_money(n):
        if n == 0: return 0
        if n <= 2: return mem[n]
        if n not in mem:
            max_n = max(nums[n-1] + max_money(n-2), nums[n-2] + max_money(n-3))
            mem[n] = max_n
        return mem[n]
    return max_money(length)
```

**标准版**（bottom-up 滚动变量，solution_readable.py）：

```python
def rob(self, nums):
    prev2 = prev1 = 0
    for n in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + n)   # 不偷 vs 偷
    return prev1
```

## 两个视角的等价性

- **用户视角**："枚举最后偷的房子"（偷 n-1 或偷 n-2，不能偷相邻）
- **标准视角**："偷/不偷最后一家" `f(n) = max(f(n-1), nums[n-1]+f(n-2))`

两者等价（金额非负时 `nums[n-1]+f(n-2) ≥ f(n-2)`，标准式的不偷分支被用户的偷 n-2 分支覆盖）。

## 验证

- 对拍 **10 万组随机 vs 标准 DP 0 不一致**；
- 官方样例：`[1,2,3,1]→4`、`[2,7,9,3,1]→12`、`[1]→1`、`[2,1,1,2]→4`。

## 复杂度

- 时间 **O(n)**；空间 O(n)（用户版记忆化）/ O(1)（标准版滚动）——满足要求。