# Created by Chono-Hina at 2026/09/11 15:18
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-consecutive-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        max_length = 1
        for n in num_set:
            if n - 1 in num_set:
                continue
            count = 1
            while True:
                if n + count in num_set:
                    count += 1
                else:
                    break
            max_length = max(max_length, count)
        return max_length

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestConsecutive(nums)
    print("\noutput:", serialize(ans, "integer"))
