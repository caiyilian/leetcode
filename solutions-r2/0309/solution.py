"""309. 买卖股票的最佳时机含冷冻期（二刷）——四状态 DP（用户 AC 版）

用户二刷（2026-11-01 22:06 提交 758099896，AC 一次通过，0ms/19.9MB）
- 股票系列第二题：121 单次 → 这里无限次 + 冷冻期（卖出的第二天不能买）
- 四状态拆分：持有 / 保持卖出（非冷冻）/ 当天卖出 / 冷冻——把"卖出"和"冷冻"拆开更直白
- 与标准三状态（持有/冷冻/空仓非冷冻）等价，但转移逻辑更清晰：买入只能从"保持卖出"或"冷冻"来

状态转移：
- 持有  dp[i][0] = max(前一天持有, 前一天保持卖出后今天买, 前一天冷冻今天买)
- 保持卖出(非冷冻) dp[i][1] = max(前一天保持卖出, 前一天冷冻)
- 当天卖出 dp[i][2] = 前一天持有 + prices[i]（必须从持有来）
- 冷冻   dp[i][3] = 前一天卖出（必须前一天刚卖）
"""

from typing import List


# ===== 用户 AC 版（四状态） =====
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[0, 0, 0, 0] for _ in range(length + 1)]
        # 0 持有股票，1 保持卖出，2 卖出，3 冷冻
        dp[0][0] = -prices[0]
        for i in range(1, length):
            # 持有
            dp[i][0] = max(
                dp[i - 1][0],                 # 前一天持有，保持持有
                dp[i - 1][1] - prices[i],     # 前一天保持卖出，现在买入
                dp[i - 1][3] - prices[i]      # 前一天冷冻，现在可以买入
            )
            # 保持卖出（不是冷冻期）
            dp[i][1] = max(
                dp[i - 1][1],                 # 前一天也是保持卖出
                dp[i - 1][3]                  # 前一天是冷冻
            )
            # 卖出
            dp[i][2] = dp[i - 1][0] + prices[i]   # 前一天是持有股票
            # 冷冻
            dp[i][3] = dp[i - 1][2]               # 必须是前一天卖出
        return max(dp[length - 1])


# ===== 参考：标准三状态（滚动变量 O(1) 空间） =====
class Solution3State:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0   # 持有 / 刚卖(冷冻) / 空仓非冷冻
        for i in range(1, n):
            new_f0 = max(f0, f2 - prices[i])  # 继续持有 或 从空仓买入
            new_f1 = f0 + prices[i]           # 持有 → 今天卖出（明天进入冷冻）
            new_f2 = max(f2, f1)              # 继续空仓 或 冷冻结束进入空仓
            f0, f1, f2 = new_f0, new_f1, new_f2
        return max(f0, f1, f2)


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([1, 2, 3, 0, 2]))    # 3
    print(s.maxProfit([1]))                # 0
    print(s.maxProfit([1, 2, 1, 2, 1, 2])) # 2（冷冻冻结连续小波段）