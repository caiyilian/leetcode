# Created by Chono-Hina at 2026/09/25 15:54
# leetgo: 1.4.18
# https://leetcode.cn/problems/hamming-distance/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 异或：不同位 = 1；bit_count()：Python 内建数 1（C 实现，最快）
        return (x ^ y).bit_count()
        

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().hammingDistance(x, y)
    print("\noutput:", serialize(ans, "integer"))
