"""312. 戳气球（二刷·困难）——区间 DP（用户 AC 版）

用户二刷（2026-11-01 22:52 提交 758107307，AC，1743ms/21.6MB）
- 卡点复盘：递推公式一次写对，但①循环顺序错（先大区间后小区间→全是0）②return 误写 dp[0][length]
- 修正：外层按"区间长度"枚举（小区间先算）+ 开区间端点 (0, n-1) 恰为左右哨兵 → 一次 AC
- 核心：dp[i][j] = 开区间 (i, j) 内全戳破的最大分；枚举"最后戳破的气球 k"，
        此时 k 左右邻居恰为哨兵 i/j（中间已戳光）→ 得分 nums[i]*nums[k]*nums[j] + 左右子问题独立
- 复杂度：O(n³) 时间 / O(n²) 空间
"""

from typing import List


# ===== 用户 AC 版（递推法，O(n³)） =====
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]            # 两端补哨兵（值 1，不戳）
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for each_len in range(2, length):  # 区间宽度（哨兵间距），从小到大先算小区间
            for i in range(0, length - each_len):
                j = i + each_len
                dp[i][j] = max(
                    (dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                    for k in range(i + 1, j)          # 最后戳破的气球 k 在开区间内
                )
        return dp[0][length - 1]           # 开区间 (0, n-1)，两端恰好是左右哨兵


# ===== 参考：DFS 记忆化（自顶向下，同一递推） =====
from functools import lru_cache


class SolutionMemo:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def f(i: int, j: int) -> int:      # 开区间 (i, j) 内全戳破的最大分
            if j - i <= 1:                 # 区间内没有气球
                return 0
            best = 0
            for k in range(i + 1, j):
                best = max(best, f(i, k) + f(k, j) + nums[i] * nums[k] * nums[j])
            return best

        return f(0, n - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))    # 167
    print(s.maxCoins([1, 5]))          # 10
    print(s.maxCoins([1]))             # 1