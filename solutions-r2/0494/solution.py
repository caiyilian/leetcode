"""494. 目标和（二刷）——记忆化递归（用户 AC 版）+ 背包变形/哈希 DP 参考

用户二刷（2026-11-02 20:31 提交 758262188，AC，195ms/70.3MB）
- 记忆化递归：fun(i, target) = 用前 i 个数、当前还需凑出某和的方案数；每步 ±nums[i] 两条路
- 递归的优点是直译题意（不用想数学变形）；缺点是空间 O(n·target)（70MB 因元组 key 哈希）
- 迭代法核心：把 ± 翻译成集合划分 → sum(P) = (target+total)/2 → 0-1 背包计数（416 的计数版）
"""

from typing import List


# ===== 用户 AC 版（记忆化递归） =====
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}

        def fun(i, target):
            if i < 0:                          # 数用完了
                return target == 0             # 恰好凑出目标才算 1 种
            if (i, target) not in mem:
                mem[(i, target)] = fun(i - 1, target - nums[i]) \
                    + fun(i - 1, target + nums[i])   # 第 i 个数取 + 或 -
            return mem[(i, target)]

        return fun(len(nums) - 1, target)


# ===== 参考 1：背包变形（迭代，推荐掌握） =====
class SolutionKnapsack:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 数学变形：设 P = 取正号的数，sum(P) - sum(其余) = target
        #   sum(P) + sum(其余) = total → 2·sum(P) = target + total
        if (target + total) % 2 != 0 or target + total < 0:
            return 0                            # 不可能：偶数/非负约束
        s = (target + total) // 2               # 需要选出的正号子集和
        dp = [0] * (s + 1)
        dp[0] = 1                               # 凑出 0 有 1 种（什么都不选）
        for x in nums:
            for j in range(s, x - 1, -1):       # ⚡ 倒序：0-1 背包计数（416 的计数版）
                dp[j] += dp[j - x]
        return dp[s]


# ===== 参考 2：哈希表迭代 DP（直译递归、免变形） =====
from collections import defaultdict


class SolutionHash:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1                               # 和为 0 的方案数 = 1
        for x in nums:
            new = defaultdict(int)
            for cur, cnt in dp.items():
                new[cur + x] += cnt             # 取 +
                new[cur - x] += cnt             # 取 -
            dp = new
        return dp[target]


if __name__ == "__main__":
    s = Solution()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))    # 5
    print(s.findTargetSumWays([1], 1))                # 1
    print(s.findTargetSumWays([1], 2))                # 0