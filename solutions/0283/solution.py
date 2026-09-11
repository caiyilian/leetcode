# Created by Chono-Hina at 2026/09/11 16:15
# leetgo: 1.4.18
# https://leetcode.cn/problems/move-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index_first_zero = length
        for i in range(length):
            if nums[i] == 0:
                if index_first_zero > i:
                    index_first_zero = i
            else:
                if i > index_first_zero:
                    nums[index_first_zero], nums[i] = nums[i], 0
                    index_first_zero += 1
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().moveZeroes(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
