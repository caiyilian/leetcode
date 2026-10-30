# Created by Chono-Hina at 2026/09/17 11:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:                     # ① 确认存在
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return [-1, -1]                      # 不存在

        # ② 左边界：找第一个 >= target（假想 target-0.5 的插入位置）
        left, right = 0, length - 1
        target1 = target - 0.5
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target1:
                left = mid + 1
            else:
                right = mid - 1
        start = left

        # ③ 右边界：找第一个 > target（假想 target+0.5 的插入位置）
        right = length - 1
        target2 = target + 0.5
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target2:
                left = mid + 1
            else:
                right = mid - 1
        end = left

        return [start, end - 1]                  # end 是第一个 > target 的 → -1
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchRange(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
