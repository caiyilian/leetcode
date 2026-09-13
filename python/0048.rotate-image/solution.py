# Created by Chono-Hina at 2026/09/13 12:38
# leetgo: 1.4.18
# https://leetcode.cn/problems/rotate-image/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        layer = 0
        for _ in range(n//2):
            for i in range(n-1-2*layer):
                matrix[layer][i+layer], matrix[i+layer][n-1-layer] = matrix[i+layer][n-1-layer], matrix[layer][i+layer]
                matrix[layer][i+layer], matrix[n-1-layer][n-1-i-layer] = matrix[n-1-layer][n-1-i-layer], matrix[layer][i+layer]
                matrix[layer][i+layer], matrix[n-1-i-layer][layer] = matrix[n-1-i-layer][layer], matrix[layer][i+layer]
            layer += 1
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
