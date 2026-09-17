# Created by Chono-Hina at 2026/09/17 13:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/search-in-rotated-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:        # 左半段递增
                if nums[left] <= target < nums[mid]:
                    right = mid - 1            # target 在左段内 → 左走
                else:
                    left = mid + 1             # 否则去断裂处（右）
            else:                               # 右半段递增
                if nums[mid] < target <= nums[right]:
                    left = mid + 1             # target 在右段内 → 右走
                else:
                    right = mid - 1            # 否则去断裂处（左）
        return -1
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)
    print("\noutput:", serialize(ans, "integer"))
