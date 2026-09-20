# 1143. 最长公共子序列 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 1143. 最长公共子序列（Longest Common Subsequence）· 中等（字符串 DP 双经典之一） |
| 链接 | https://leetcode.cn/problems/longest-common-subsequence/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 49/49 用例通过**（leetgo 复提交） |
| 运行时间 | 351 ms（击败 61%） |
| 内存 | 43.4 MB |

## 解法（用户标准 LCS DP，教科书式）

```python
class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1          # 相等：左上 +1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 不等：上/左取 max
        return dp[m][n]
```

## 为什么是 DP（最后一步分析）

```
看 text1 第 i 个字符 vs text2 第 j 个字符：
  相等 → 这对字符必进 LCS，答案 = 前 i-1、j-1 的 LCS + 1   （左上 +1）
  不等 → 这对字符不能同时进，至少丢一个                  （max 上/左）
```

## 二维 DP 全家桶对照

| 题 | 转移式 | 形态 |
|----|--------|------|
| 62 不同路径 | `dp[i-1][j] + dp[i][j-1]` | 两来源都加 |
| 64 最小路径和 | `min(上, 左) + grid` | 两来源取小 |
| 1143 LCS | `相等?左上+1 : max(上,左)` | 按字符相等分支 |

## 验证

- 对拍 **2 万组随机串 vs 记忆化递归 0 不一致**；
- 样例：`abcde/ace→3`、`abc/abc→3`、`abc/def→0`。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)（可滚动到 O(n)）。