# Created by Chono-Hina at 2026/09/12 22:04
# leetgo: 1.4.18
# https://leetcode.cn/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_reverse = [1] + [0] * (length)
        for i in range(length):
            if nums[length-i-1] == 0:
                break
            prefix_reverse[i+1] = prefix_reverse[i] * nums[length-i-1]
        prefix = nums[0]
        for i in range(1, length):
            prefix_reverse[length-i-1] = prefix * prefix_reverse[length-i-1]
            prefix *= nums[i]
        prefix_reverse.reverse()
        return prefix_reverse[1:]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
