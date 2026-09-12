# Created by Chono-Hina at 2026/09/12 22:56
# leetgo: 1.4.18
# https://leetcode.cn/problems/first-missing-positive/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] < 1:
                continue
            while (nums[i] != (i+1)) and (1 <= nums[i] <= length):
                if nums[nums[i] - 1] == nums[i]:
                    break
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i, now_value in enumerate(nums):
            if now_value != (i+1):
                return i+1
        return length + 1
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstMissingPositive(nums)
    print("\noutput:", serialize(ans, "integer"))
