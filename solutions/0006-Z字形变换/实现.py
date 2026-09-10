# Created by Chono-Hina at 2026/09/10 23:53
# leetgo: 1.4.18
# https://leetcode.cn/problems/zigzag-conversion/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        row, dir = 0, 1
        for ch in s:
            rows[row] += ch
            row += dir
            if row == 0 or row == numRows - 1:
                dir = -dir
        return "".join(rows)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    numRows: int = deserialize("int", read_line())
    ans = Solution().convert(s, numRows)
    print("\noutput:", serialize(ans, "string"))
