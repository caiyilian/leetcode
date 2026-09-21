# Created by Chono-Hina at 2026/09/21 19:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/maximal-square/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] = 以 (i-1,j-1) 为右下角的最大正方形边长
        # 转移：dp[i][j] = 1 + min(左上, 上, 左)
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]   # 多一圈 0 边界，免越界判断
        now_max = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '0':
                    continue
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                now_max = max(dp[i][j], now_max)
        return now_max ** 2
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalSquare(matrix)
    print("\noutput:", serialize(ans, "integer"))
