"""416. 分割等和子集（二刷）——0-1 背包一维滚动 bool 版（用户 AC 版）

用户二刷（2026-11-02 两版演进）：
- 18:29/18:31 AC 二维 DP（758238546/758238815，2457ms/49MB）——正确但慢
- 19:26 AC 一维滚动 bool 版（758247279，587ms/19MB）——快 4.2 倍、省 2.6 倍内存（本文件主解）
- ⚡ 关键：0-1 背包内层 t 必须从大到小遍历（防同一个数被复用多次）；完全背包才是正序
- 本质：能否选出若干数和 = sum/2 → 容量 target 的 0-1 背包，dp[t] = 能否凑出 t
"""

from typing import List


# ===== 用户一维滚动 AC 版（O(n·target)/O(target)） =====
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:              # 奇数总和必不可能平分
            return False
        target = nums_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True                       # 凑出 0 恒成立（一个都不选）
        for x in nums:
            for j in range(target, x - 1, -1):   # ⚡ 倒序：0-1 背包防重复使用
                dp[j] = dp[j] or dp[j - x]      # 不选 or 选
        return dp[target]


# ===== 参考：二维 DP 版（用户首版，标准解法一，便于理解状态） =====
class Solution2D:
    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        nums_sum = sum(nums)
        if nums_sum % 2 != 0:
            return False
        target = nums_sum // 2
        dp = [[0] * (target + 1) for _ in range(length + 1)]
        for i in range(1, length):
            for j in range(target + 1):
                if j - nums[i] < 0:
                    dp[i][j] = dp[i - 1][j]                 # 放不下 → 只能不放
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
        return dp[length - 1][target] == target


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))    # True
    print(s.canPartition([1, 2, 3, 5]))     # False
    print(s.canPartition([1, 1]))           # True
    print(s.canPartition([1]))              # False