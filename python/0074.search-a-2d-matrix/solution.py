# Created by Chono-Hina at 2026/09/17 11:17
# leetgo: 1.4.18
# https://leetcode.cn/problems/search-a-2d-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            middle = (left + right) // 2

            i, j = middle // n, middle % n   # ★ 除以"列数" n（不是行数 m！）

            if matrix[i][j] >= target:
                right = middle
            else:
                left = middle + 1

        return matrix[left // n][left % n] == target
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
