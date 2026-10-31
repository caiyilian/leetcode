"""121. 买卖股票的最佳时机（二刷）——一次遍历维护最低买入价（O(n)/O(1) 标准解）

用户 AC 版（2026-10-31 22:10 提交 757959585，一次通过，51ms/28.1MB）
- 贪心思想：只允许一次买卖 → 卖出当天利润 = 当天价 - 历史最低买入价
- min_val 维护"到今天为止的最低价"，result 维护"到今天为止的最大利润"
- 若今天比历史最低还低 → 更新最低价（更优的买入点）；否则计算今天利润更新 result
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]          # 历史最低买入价
        result = 0                   # 最大利润
        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]  # 出现更低的买入点
            else:
                result = max(prices[i] - min_val, result)  # 今天卖出能赚多少
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))    # 5
    print(s.maxProfit([7, 6, 4, 3, 1]))       # 0
    print(s.maxProfit([1, 2, 3, 4]))          # 3
    print(s.maxProfit([5]))                   # 0