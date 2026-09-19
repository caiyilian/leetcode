# 64. 最小路径和 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 64. 最小路径和（Minimum Path Sum）· 中等（路径 DP） |
| 链接 | https://leetcode.cn/problems/minimum-path-sum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 66/66 用例通过**（leetgo 复提交） |
| 运行时间 | 19 ms |
| 内存 | 21.4 MB |

## 解法（用户两版演进，干净版定稿）

**初版**（if 判断越界）：

```python
road1 = dp[m-i][n-j-1] if i >= 1 else float("inf")   # 右方
road2 = dp[m-i-1][n-j] if j >= 1 else float("inf")   # 下方
dp[m-i-1][n-j-1] = (min(road1, road2) if not isinf else 0) + grid[..]
```

**干净版**（补一圈 inf 边界，省掉 if）：

```python
def minPathSum(self, grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]   # 多一圈 inf
    dp[m][n - 1] = 0    # 终点右方 = 0
    dp[m - 1][n] = 0    # 终点下方 = 0
    for i in range(m):
        for j in range(n):
            dp[m-i-1][n-j-1] = min(dp[m-i][n-j-1], dp[m-i-1][n-j]) + grid[m-i-1][n-j-1]
    return dp[0][0]
```

**干净版亮点**：`(m+1)×(n+1)` 数组多一圈 inf，转移统一 `min(下方, 右方) + grid`，不用 if 判越界——这是"补边界"技巧（与 118 杨辉三角补零法同源，只是这里补 inf）。

## 62 → 64：路径 DP 的进化

```
62 不同路径：dp[i][j] = dp[i+1][j] + dp[i][j+1]        ← 求和，边界 0
64 最小路径和：dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + grid[i][j]  ← 取 min，边界 inf
```

**关键差异**：62 边界 0（越界 = 0 条路径），64 边界 inf（min 运算里缺失边不能选 0，否则"白嫖"）。

## 验证

- 对拍 **3 万组随机网格 0 不一致**；
- 官方样例：`[[1,3,1],[1,5,1],[4,2,1]]→7`、`[[1,2,3],[4,5,6]]→12`。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)（可滚动到 O(n)）。