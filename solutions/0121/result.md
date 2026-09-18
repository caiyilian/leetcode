# 121. 买卖股票的最佳时机 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 121. 买卖股票的最佳时机（Best Time to Buy and Sell Stock）· 简单（贪心分类第 1 题 / DP 入门） |
| 链接 | https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 213/213 用例通过**（leetgo 复提交） |
| 运行时间 | 34 ms（击败 91%） |
| 内存 | 28.6 MB |

## ⚠️ 失败记录（用户要求）

| 提交 | 结果 | 问题 |
|------|------|------|
| 750005416 | **TLE** | 暴力两层循环 O(n²)：`for i: for j: max(prices[j]-prices[i])` |
| 750009869 | **AC** | 一次遍历 O(n)：历史最低价 + 最大利润 |

**教训**：买入点 × 卖出点的全组合是 O(n²)，但只需记住"到目前为止的最低买入价"，就能 O(n) 一路扫完——**把两个自由度的全枚举，降成一个全局最优状态 + 一次扫描**。

## 解法（用户版 solution.py + 标准版 solution_readable.py）

**用户版**（min_val 历史最低 + all_min 最大利润，冗余 max_val）：

```python
min_val, max_val = prices[0], prices[0]
for p in prices[1:]:
    if p < min_val: min_val = p; max_val = p
    elif p > max_val:
        max_val = p
        all_min = max(all_min, p - min_val)
```

**标准版**（DP 滚动变量，两变量极简）：

```python
min_price = float('inf'); max_profit = 0
for p in prices:
    min_price = min(min_price, p)
    max_profit = max(max_profit, p - min_price)
return max_profit
```

## 🎓 用户疑问解答：DP 标签"用到了吗"？——用到了，只是不知道

用户的代码**就是 DP 的滚动变量版**：
- `min_val` = 转移公式里的"历史最低价"；
- `all_min` = `dp[i]`（前 i 天最大利润），循环 = 从 dp[0] 推到 dp[n-1]。

**DP 三要素对应**：状态 `dp[i]` = 前 i 天最大利润 → 转移 `dp[i] = max(dp[i-1], prices[i]-min_price)` → 滚动优化（只依赖 dp[i-1] + 一个 min，两变量足够）。**"动态规划 = 当前最优解 = 之前最优解 + 当前一步决策"，用户无意识写出了转移，只是不知道它叫这个名字。**

## 验证

- 对拍 **5 万组随机价格序列 vs 标准版 0 不一致**；
- 官方样例：`[7,1,5,3,6,4]→5`、`[7,6,4,3,1]→0`（一直跌无利润）、`[2,4,1]→2`。

## 复杂度

- 时间 **O(n)**（一次遍历，最优）；空间 O(1)。