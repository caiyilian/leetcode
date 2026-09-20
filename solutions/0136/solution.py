# Created by Chono-Hina at 2026/09/20 13:49
# leetgo: 1.4.18
# https://leetcode.cn/problems/single-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或：a^a=0, a^0=a，成对的抵消，剩下单身数字
        result = 0
        for n in nums:
            result ^= n
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)
    print("\noutput:", serialize(ans, "integer"))
