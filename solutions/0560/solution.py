# Created by Chono-Hina at 2026/09/12 16:50
# leetgo: 1.4.18
# https://leetcode.cn/problems/subarray-sum-equals-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = {0: 1}
        cur = 0
        count = 0
        for x in nums:
            cur += x
            count += cnt.get(cur - k, 0)
            cnt[cur] = cnt.get(cur, 0) + 1
        return count
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
