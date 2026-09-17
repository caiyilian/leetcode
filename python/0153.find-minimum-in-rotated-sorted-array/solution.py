# Created by Chono-Hina at 2026/09/17 14:36
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMin(self, nums: list[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1          # mid 在大段 → 最小值必在右边，mid 可排除
            else:
                right = mid             # ★ mid 在小段 → 最小值可能是 mid 本身，必须保留（别写 mid-1！）
        return nums[left]
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMin(nums)
    print("\noutput:", serialize(ans, "integer"))
