# Created by Chono-Hina at 2026/09/17 22:06
# leetgo: 1.4.18
# https://leetcode.cn/problems/largest-rectangle-in-histogram/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        result = 0
        heights = [0] + heights + [0]   # 双哨兵：开头 0 保左边界；结尾 0 强制全部结算
        length = len(heights)
        stack = []                      # 单调递增栈，存下标
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:   # while：一个矮子顶掉一串
                h = heights[stack.pop()]
                w = i - stack[-1] - 1   # 右边界=i（第一个更矮），左边界=弹后栈顶（第一个更矮）
                result = max(result, h * w)
            stack.append(i)
        return result
        

# @lc code=end

if __name__ == "__main__":
    heights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestRectangleArea(heights)
    print("\noutput:", serialize(ans, "integer"))
