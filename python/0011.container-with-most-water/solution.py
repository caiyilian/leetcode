# Created by Chono-Hina at 2026/09/11 18:27
# leetgo: 1.4.18
# https://leetcode.cn/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] <= height[r]:
                area = max(height[l] * (r - l), area)
                l += 1
            else:
                area = max(height[r] * (r - l), area)
                r -= 1
        return area

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))
