# 300. 最长递增子序列 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 300. 最长递增子序列（Longest Increasing Subsequence）· 中等（动态规划分类第 7 题） |
| 链接 | https://leetcode.cn/problems/longest-increasing-subsequence/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 57/57 用例通过**（leetgo 复提交） |
| 运行时间 | 1291 ms（O(n²) DP 正常开销） |
| 内存 | 19.4 MB |

## 解法（用户标准 DP，O(n²)）

```python
class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        best = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            best = max(best, dp[i])
        return best
```

## 用户疑问解答

- **是否 DP**：是，标准 DP（dp[i] = 以 nums[i] 结尾的 LIS 长度）；
- **是否符合要求**：符合，O(n²) 是标准解；
- **速度慢是不标准吗**：不是——O(n²) 是标准 DP，但存在 **O(n log n) 的"耐心排序"（贪心 + 二分）**优化，力扣快的人用它，复杂度差一个 log 量级。

## ⚡ 关键认知：依赖前面所有 → 不能用滚动变量

`dp[i] = max(dp[j]+1) for j<i`——依赖**前面所有** j，不是固定前 1/2 个，所以**必须保留整个 dp 数组**（不能滚动）。这是 70 爬楼梯学的"依赖固定几个才滚动"判断标准的兑现。

## O(n log n) 优化（耐心排序，仅提及）

维护 `tails` 数组，`tails[k]` = 长度为 k+1 的递增子序列的最小可能末尾。遍历 x，二分找第一个 `>= x` 的位置替换（或追加），最后 tails 长度即答案。贪心 + 二分，面试加分项。

## 验证

- 对拍 **2 万组随机数组 vs 暴力回溯 0 不一致**；
- 官方样例：`[10,9,2,5,3,7,101,18]→4`、`[0,1,0,3,2,3]→4`、全相等 `[7,7,7,7,7,7,7]→1`。

## 复杂度

- 时间 **O(n²)**（DP）/ O(n log n)（耐心排序优化）；空间 O(n)。