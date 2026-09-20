# Created by Chono-Hina at 2026/09/20 14:13
# leetgo: 1.4.18
# https://leetcode.cn/problems/majority-element/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票：相同 +1、不同 -1、归零换人
        count = 0
        for n in nums:
            if count == 0:
                now = n
                count += 1
            else:
                if now != n:
                    count -= 1
                else:
                    count += 1      # ★ 相同元素计数 +1（易漏）
        return now
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().majorityElement(nums)
    print("\noutput:", serialize(ans, "integer"))
