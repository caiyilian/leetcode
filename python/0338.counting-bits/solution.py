# Created by Chono-Hina at 2026/09/24 15:58
# leetgo: 1.4.18
# https://leetcode.cn/problems/counting-bits/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countBits(self, n: int) -> list[int]:
        # 位运算 + DP：i 的二进制 = (i>>1) 的二进制 追加最低位
        # 所以 dp[i] = dp[i>>1] + (i&1)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countBits(n)
    print("\noutput:", serialize(ans, "integer[]"))
