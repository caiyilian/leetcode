"""53. 最大子数组和（二刷）——Kadane / 动态规划（双写法）

解法一：用户凭记忆写的滚动变量版（Kadane，2026-10-15 16:17 提交 755000686，AC）
解法二：DP 数组版——展示完整状态定义，证明"滚动 = 空间压缩"
"""

from typing import List


# ========== 解法一：用户 AC 版（滚动变量 = DP 空间压缩）==========
class SolutionUser:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        acc = 0                     # acc 扮演 dp[i-1]（上一个状态）
        for i in range(len(nums)):
            if acc <= 0:            # dp[i-1] <= 0 → max 必取 nums[i]（单干）
                acc = nums[i]
            else:                   # dp[i-1] > 0 → 接力
                acc += nums[i]
            result = max(acc, result)
        return result


# ========== 解法二：DP 数组版（完整状态定义，面试讲法）==========
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]                       # 第一个数只能自己
        for i in range(1, n):
            # 状态转移：单干 or 接力，取 max
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        return max(dp)


if __name__ == "__main__":
    s = Solution()
    su = SolutionUser()
    for nums in ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8], [-1, -2, -3]):
        print(nums, '→ dp版:', s.maxSubArray(nums), ' 滚动版:', su.maxSubArray(nums))