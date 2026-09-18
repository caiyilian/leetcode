# Created by Chono-Hina at 2026/09/18 17:21
# leetgo: 1.4.18
# https://leetcode.cn/problems/jump-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        nums.pop()                       # 去掉终点（最后一个元素）
        last_max = float("-inf")
        last_index = -1
        for i, num in enumerate(nums):
            if num == 0 and last_max - i + last_index == 0:   # 跳不过去的坑
                return False
            if (num >= last_max) or (num + (i - last_index) > last_max):
                last_max = num
                last_index = i
        return True
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canJump(nums)
    print("\noutput:", serialize(ans, "boolean"))
