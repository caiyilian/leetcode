# 221. 最大正方形 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 221. 最大正方形（Maximal Square）· 中等（v2 新增题 · 矩阵 DP） |
| 链接 | https://leetcode.cn/problems/maximal-square/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-21 |
| 最终提交 | ✅ **ACCEPTED - 81/81 用例通过**（leetgo 复提交） |
| 运行时间 | 74 ms（击败 73%） |
| 内存 | 32.4 MB |

## 解法（用户二维 DP，标准）

```python
class Solution:
    def maximalSquare(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]   # 多一圈 0 边界
        now_max = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i-1][j-1] == '0':
                    continue
                dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                now_max = max(dp[i][j], now_max)
        return now_max ** 2
```

## 核心：dp[i][j] = 以 (i,j) 为右下角的最大正方形边长

- 若 `matrix[i-1][j-1] == '0'` → dp = 0；
- 否则 `dp[i][j] = 1 + min(左上, 上, 左)`——**三个方向的最小值 + 1**（能被三个方向同时"托住"的最大边长）；
- 答案是 `max(dp)²`（面积）。

## 💡 可优化点（用户询问）

**空间 O(mn) → O(n)**：`dp[i][j]` 只依赖上一行和当前行左边，可用一维滚动 + `prev` 变量（见 `solution_readable.py`）：

```python
def maximalSquare(self, matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)
    now_max = 0
    for i in range(1, m + 1):
        prev = 0                       # dp[i-1][j-1]
        for j in range(1, n + 1):
            temp = dp[j]               # 保存 dp[i-1][j]
            if matrix[i-1][j-1] == '1':
                dp[j] = 1 + min(prev, dp[j], dp[j-1])
                now_max = max(now_max, dp[j])
            else:
                dp[j] = 0
            prev = temp
    return now_max ** 2
```

- 时间不变 O(mn)，空间从 **O(mn) 降到 O(n)**；
- 注意用 `temp` 保存"上一行同列"的旧值，`prev` 传递"左上"。

## 验证

- 对拍 **2 万组随机矩阵 vs 暴力 0 不一致**（用户版 + 优化版都验证）；
- 样例：`[["1","0","1","0","0"],...] → 4`。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)（二维）/ **O(n)**（滚动优化）。