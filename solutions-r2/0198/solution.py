"""198. 打家劫舍（二刷）——DP 选/不选（O(n)/O(1) 滚动最优）

用户 AC 版（2026-11-01 16:33 提交 758045486，一次通过，0ms/19.1MB）
- 递推：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
  - 不偷 i：dp[i-1]
  - 偷 i：dp[i-2] + nums[i]（i-1 不能偷）
- 滚动数组：只依赖前两个状态 → O(1) 空间（70 爬楼梯的"滚动"升级版）
- 基础约定：dp[0]=nums[0], dp[1]=max(nums[0], nums[1])
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp_ip1 = nums[0]          # dp[i-1]
        dp_ip2 = 0                # dp[i-2]（初始 = 偷 nums[0] 前的最优 0）
        for i in range(1, len(nums)):
            dp_ip1, dp_ip2 = max(dp_ip1, dp_ip2 + nums[i]), dp_ip1
        return dp_ip1


# ===== 参考：标准一维 DP（思路更直白，面试先写这个） =====
class SolutionDP:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.rob([1, 2, 3, 1]))        # 4
    print(s.rob([2, 7, 9, 3, 1]))     # 12
    print(s.rob([5]))                 # 5