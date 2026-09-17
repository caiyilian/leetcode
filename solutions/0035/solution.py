# Created by Chono-Hina at 2026/09/17 10:43
# leetgo: 1.4.18
# https://leetcode.cn/problems/search-insert-position/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length
        while left < right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                if right == middle:
                    return right - 1
                right = middle
            else:
                if left == middle:
                    return left + 1
                left = middle
        return 0
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchInsert(nums, target)
    print("\noutput:", serialize(ans, "integer"))
