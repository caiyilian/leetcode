# Created by Chono-Hina at 2026/09/12 12:47
# leetgo: 1.4.18
# https://leetcode.cn/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        water_count = 0
        max_left = 0
        max_right = 0
        i, j = 1, length - 2
        while i <= j:
            max_left = max(max_left, height[i-1])
            max_right = max(max_right, height[j + 1])
            if i == j:
                water_count += max(0, min(max_left, max_right) - height[i])
                break
            if max_left < max_right:
                water_count += max(0, max_left - height[i])
                i += 1
            elif max_right < max_left:
                water_count += max(0, max_right - height[j])
                j -= 1
            else:
                water_count += max(0, max_left - height[i]) + max(0, max_right - height[j])
                i += 1
                j -= 1
        return water_count

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))
