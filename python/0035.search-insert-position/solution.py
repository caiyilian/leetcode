# Created by Chono-Hina at 2026/09/17 10:43
# leetgo: 1.4.18
# https://leetcode.cn/problems/search-insert-position/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left                 # ★ 退出时 left 就是插入位置
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchInsert(nums, target)
    print("\noutput:", serialize(ans, "integer"))
