# 62. 不同路径 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 62. 不同路径（Unique Paths）· 中等（路径 DP） |
| 链接 | https://leetcode.cn/problems/unique-paths/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 64/64 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.1 MB |

## ⚠️ 失败记录（两次）

| 提交 | 结果 | 根因 |
|------|------|------|
| 750272384 | **WA** | 缺 `m=1,n=1` 边界：`i+j==m+n-3` 恒不成立（=-1），返回 0，但答案 1 |
| 750272534 | **TLE** | 纯递归无记忆化：二叉递归树 2^(m+n) 指数级 |
| 750274075 | AC | 记忆化递归 + m=1,n=1 边界 |
| 750275330 | AC | 迭代 DP（从终点回填） |

**又是"递归 → 记忆化 → 迭代"的完整路径**（70/198 后第 3 次走通）。

## 解法（两个版本）

**迭代版（solution.py，主解，0ms/100%）**：

```python
def uniquePaths(self, m, n):
    dp = [[1] * n for _ in range(m)]      # 全 1：第一行/列都是 1
    for i in range(1, m):
        for j in range(1, n):
            dp[m-i-1][n-j-1] = dp[m-i][n-j-1] + dp[m-i-1][n-j]  # 从终点回填
    return dp[0][0]
```

**记忆化递归版（solution_readable.py，top-down）**：

```python
def uniquePaths(self, m, n):
    mem = {(m-2, n-1): 1, (m-1, n-2): 1}
    def fun(i, j):
        if i >= m or j >= n: return 0
        if (i, j) not in mem:
            mem[(i, j)] = fun(i+1, j) + fun(i, j+1)   # 向右 + 向下
        return mem[(i, j)]
    return fun(0, 0)
```

## 两个版本的镜像关系

- **记忆化版**：从 (0,0) 递归推到终点（自顶向下 + mem）；
- **迭代版**：从终点回填到 (0,0)（自底向上填表）；
- 转移式同构：`dp[i][j] = dp[i+1][j] + dp[i][j+1]`（下方+右方）= 标准 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`（上方+左方）的镜像。

## 验证

- 对拍 **m,n=1..19 全量 vs 组合数 C(m+n-2, m-1) 0 不一致**；
- 样例：(3,7)=28、(3,3)=6、(23,12)=193536720、(1,1)=1。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)（可滚动到 O(n)）。

## 补充：数学解法

答案 = C(m+n-2, m-1)（组合数，走 m+n-2 步，选 m-1 步向下）。面试可作 bonus 提。