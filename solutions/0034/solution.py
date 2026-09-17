# Created by Chono-Hina at 2026/09/17 11:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        if not nums:
            return [-1, -1]
        left, right = 0, length - 1
        while left < right:                     # 第一次二分：找第一个 >= target
            middle = (left + right) // 2
            if nums[middle] >= target:
                right = middle
            else:
                left = middle + 1
        if nums[left] != target:                # 不存在
            return [-1, -1]
        min_val = left
        right = length - 1
        while left < right:                     # 第二次二分：找第一个 >= target+1
            middle = (left + right) // 2
            if nums[middle] >= target + 1:
                right = middle
            else:
                left = middle + 1
        # 补丁（闭区间二分找不到时 left 卡在 length-1）：
        # target 是最大值 → 右边界 = left；否则 = left - 1
        return [min_val, left if nums[-1] == target else (left - 1)]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchRange(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
