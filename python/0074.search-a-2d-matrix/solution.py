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
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // n, mid % n           # 一维 → 二维换算（除以列数 n）
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
