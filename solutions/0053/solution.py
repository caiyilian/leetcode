# Created by Chono-Hina at 2026/09/12 19:19
# leetgo: 1.4.18
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        curr_sum = nums[0]
        max_sum = curr_sum
        for i in range(1, length):
            if curr_sum < 0:
                curr_sum = nums[i]
            else:
                curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))
