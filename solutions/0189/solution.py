# Created by Chono-Hina at 2026/09/12 20:51
# leetgo: 1.4.18
# https://leetcode.cn/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:k], nums[k:] = nums[-k:], nums[:length-k]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
