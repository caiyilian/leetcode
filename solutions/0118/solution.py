# Created by Chono-Hina at 2026/09/18 20:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/pascals-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 二维 DP：val[i][j] = val[i-1][j-1] + val[i-1][j]（左上 + 正上）
        result = [[1]]
        for i in range(1, numRows):
            result.append([])
            for j in range(i + 1):
                v_im1_jm1 = result[i-1][j-1] if j-1 >= 0 else 0   # 左上邻居（越界补 0）
                v_im1_j   = result[i-1][j]   if j < i   else 0   # 正上邻居（越界补 0）
                val_i_j = v_im1_jm1 + v_im1_j
                result[-1].append(val_i_j)
        return result
        

# @lc code=end

if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)
    print("\noutput:", serialize(ans, "integer[][]"))
