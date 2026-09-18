# Created by Chono-Hina at 2026/09/18 22:24
# leetgo: 1.4.18
# https://leetcode.cn/problems/house-robber/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rob(self, nums: List[int]) -> int:
        # 记忆化递归（top-down DP）：枚举"最后一个偷的房子"
        # f(n) = max(nums[n-1] + f(n-2), nums[n-2] + f(n-3))
        length = len(nums)
        if length == 1:
            return nums[0]
        mem = {1: nums[0], 2: max(nums[:2])}
        def max_money(n):
            if n == 0:
                return 0
            if n <= 2:
                return mem[n]
            if n not in mem:
                # 偷最后一家（剩 n-2）或偷倒数第二家（剩 n-3）
                max_n = max(nums[n-1] + max_money(n-2), nums[n-2] + max_money(n-3))
                mem[n] = max_n
            return mem[n]
        return max_money(length)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)
    print("\noutput:", serialize(ans, "integer"))
