# 309. 买卖股票的最佳时机含冷冻期 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 309. 买卖股票的最佳时机含冷冻期（Best Time to Buy and Sell Stock with Cooldown）· 中等（v2 新增题 · 状态机 DP） |
| 链接 | https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-21 |
| 最终提交 | ✅ **ACCEPTED - 210/210 用例通过**（leetgo 复提交） |
| 运行时间 | 3 ms |
| 内存 | 19.7 MB |

## 解法（用户状态机 DP，三状态）

```python
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        dp = [[0] * 3 for _ in range(length + 1)]
        dp[0][0] = -prices[0]        # 持有 = 买入成本
        for i in range(1, length + 1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i-1])  # 持有：继续/空仓买入
            dp[i][1] = dp[i-1][0] + prices[i-1]                   # 卖出：昨天持有+今价
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])                # 休息：冷冻结束/继续空仓
        return max(dp[length][1], dp[length][2])
```

## ⚠️ 调试记录（用户卡点：初始化列错位）

| 问题 | 说明 |
|------|------|
| `dp[0][1] = -prices[0]` | ❌ 把"买入成本"放进了"卖出"列 |
| `dp[0][0] = -prices[0]` | ✅ 持有列才是买入成本 |

**关键**：`-price`（买入成本）属于**持有**；`+price`（卖出收益）属于**卖出**。初始化别放反列。

三个状态（持有/冷冻/休息）分别记录，一维 dp 装不下。

## 三状态转移（状态机）

```
持有 hold ← max(昨天持有, 昨天休息 - 今天价)   ← 买入只能从休息来
卖出 sold ← 昨天持有 + 今天价                 ← 卖出只能从持有来
休息 rest ← max(昨天卖出, 昨天休息)           ← 卖出后一天冷冻
```

## 验证

- 样例：`[1,2,3,0,2]→3`、`[1]→0`；
- 边界：`[1,2,3,0,2,5,6]→7`（买0卖2+买3卖6）。

## 复杂度

- 时间 **O(n)**；空间 O(n)（可滚动到 O(1) 三个变量）。