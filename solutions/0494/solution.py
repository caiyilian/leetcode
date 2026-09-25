# Created by Chono-Hina at 2026/09/25 16:31
# leetgo: 1.4.18
# https://leetcode.cn/problems/target-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # 记忆化搜索（自顶向下 DP）：每个数选 + 或 -
        # fun(index, target)：前 index+1 个数组成 target 的方案数
        mem = {}

        def fun(index, target):
            if index < 0:
                return target == 0                       # 用完所有数，恰好归零
            if (index, target) not in mem:
                mem[(index, target)] = fun(index - 1, target + nums[index]) + \
                                       fun(index - 1, target - nums[index])
            return mem[(index, target)]

        return fun(len(nums) - 1, target)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findTargetSumWays(nums, target)
    print("\noutput:", serialize(ans, "integer"))
