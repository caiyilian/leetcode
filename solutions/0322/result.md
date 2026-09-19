# 322. 零钱兑换 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 322. 零钱兑换（Coin Change）· 中等（动态规划分类第 5 题） |
| 链接 | https://leetcode.cn/problems/coin-change/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 189/189 用例通过**（leetgo 复提交） |
| 运行时间 | 965 ms（记忆化递归开销 + 力扣噪声） |
| 内存 | 69.2 MB |

## ⚠️ 失败记录（用户要求）

| 提交 | 结果 | 问题 |
|------|------|------|
| 750142905 | **WA** | `if n < coins[0]`——假设 coins 已排序，但题目没保证 |
| 750143377 | **AC** | `if n < min(coins)`——用最小面值 |

**反例**：coins=[5,1,2], amount=3 → WA 版 `3 < coins[0]=5` 误判凑不出返回 -1，实际 3=1+1+1。**教训：需要最小面值就用 `min(coins)`，别偷懒用 `coins[0]`（除非主动排序）。**

## 解法（用户记忆化 DP + 标准迭代 DP）

**用户版**（"最后一块硬币"分析，记忆化）：

```python
def coinChange(self, coins, amount):
    mem = {0: 0}
    min_money = min(coins)
    def fun(n):
        if n not in mem:
            if n < min_money: return float("inf")
            min_count = float("inf")
            for c in coins:
                min_count = min(min_count, 1 + fun(n-c))
            mem[n] = min_count
        return mem[n]
    result = fun(amount)
    return -1 if isinf(result) else result
```

**标准版**（solution_readable.py，迭代）：

```python
def coinChange(self, coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return -1 if dp[amount] == float('inf') else dp[amount]
```

## 279 → 322：数学定理失效，DP 唯一正解

```
279 完全平方数：x 是平方数 → 有 Lagrange/Legendre 定理（O(√n) 数学外挂）
322 零钱兑换：x 是任意硬币 → 定理失效，只剩 DP（O(amount×len(coins))）
```

**转移式完全同构**：`dp[i] = min(dp[i-x] + 1)`，只是 x 从"平方数"变成"任意硬币"。

## 验证

- 对拍 **1 万组随机硬币+金额 vs 迭代 DP 0 不一致**；
- 官方样例：`[1,2,5]→11 得 3`、`[2]→3 得 -1`、`[1]→0 得 0`、`[3,4]→5 得 -1`。

## 复杂度

- 时间 **O(amount × len(coins))**；空间 O(amount)——满足要求。