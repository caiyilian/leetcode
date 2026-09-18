# Created by Chono-Hina at 2026/09/18 19:53
# leetgo: 1.4.18
# https://leetcode.cn/problems/climbing-stairs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def climbStairs(self, n: int) -> int:
        # 滚动变量：f(i) = f(i-1) + f(i-2)（斐波那契）
        if n <= 2:
            return n
        val_im2 = 1       # f(i-2)，初始 f(1) = 1
        val_im1 = 2       # f(i-1)，初始 f(2) = 2
        for i in range(3, n + 1):
            val_i = val_im1 + val_im2   # f(i) = f(i-1) + f(i-2)
            val_im2 = val_im1           # 滚到下一轮
            val_im1 = val_i
        return val_i
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
