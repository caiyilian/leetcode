# 279. 完全平方数 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 279. 完全平方数（Perfect Squares）· 中等（动态规划分类第 4 题） |
| 链接 | https://leetcode.cn/problems/perfect-squares/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 589/589 用例通过**（leetgo 复提交） |
| 运行时间 | 1691 ms（DP 填表正常开销 + 力扣噪声） |
| 内存 | 19.2 MB |

## 解法（迭代 DP：最后一个平方数分析）

```python
class Solution:
    def numSquares(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            final_count = float("inf")
            j = 1
            while j * j <= i:
                final_count = min(final_count, 1 + dp[i - j * j])
                j += 1
            dp[i] = final_count
        return dp[-1]
```

## 用户两版演进

1. **错误思路（拆两半 + max）**：`fun(i)` + `fun(n-i)` 取 `max(count1, count2)`——max 应为 +（拆分后个数相加），且"拆两半"绕远；
2. **记忆化递归**（正确但慢）：`fun(n) = min(1 + fun(n-i²))`，递归栈开销 + n 大时深度风险；
3. **迭代 DP**（定稿）：消除递归开销，O(n√n)。

## 关键认知：最后一步分析法

```
组成 i，最后一个平方数是 j² → dp[i] = min(dp[i-j²] + 1)
```

与 70（最后一步跨 1/2）、198（最后一家偷不偷）同骨架。

## 关于"速度慢"的真相

- 迭代 DP 复杂度 **O(n√n)** 已是 DP 范畴最优；
- 力扣上存在**四平方和定理（Lagrange）**的 O(√n) 数学外挂，DP 天然比它慢——不是 DP 写得差；
- 数学定理只对"平方数"有效，换硬币面值（322）就失效，**DP 才是通用硬通货**。

## 验证

- 对拍 n=1..1000 全量 vs 迭代 DP 0 不一致；
- n=12→3（4+4+4）、n=13→2（4+9）。

## 复杂度

- 时间 **O(n√n)**；空间 O(n)。

## 数学定理（纯好奇，非面试要求）

四平方和定理：答案 ∈ {1,2,3,4}。逐个排除：完全平方→1；`4^a(8b+7)` 形式→4（Legendre 三平方定理）；两平方和→2；否则→3。O(√n)。