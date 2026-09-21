# Created by Chono-Hina at 2026/09/21 14:53
# leetgo: 1.4.18
# https://leetcode.cn/problems/maximal-rectangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        # 85 = 84 的二维扩展：逐行累加"柱高"，每行转成柱状图最大矩形（单调栈）
        def largestRectangleArea(heights: list[int]) -> int:
            heights = [0] + heights + [0]        # 左右哨兵
            length = len(heights)
            stack = [0, 1]
            area = 0
            for i in range(2, length):            # 要包括右边哨兵才能计算每个柱子
                while heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    right = i
                    left = stack[-1]
                    w = right - left - 1
                    h = heights[mid]
                    area = max(area, h * w)
                stack.append(i)
            return area

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        area = 0
        for i in range(m):                        # 遍历每一行
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1               # 连续 '1' 累加柱高
                else:
                    heights[j] = 0                # 遇到 '0' 清零
            area = max(largestRectangleArea(heights), area)
        return area
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalRectangle(matrix)
    print("\noutput:", serialize(ans, "integer"))
