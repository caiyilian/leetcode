# Created by Chono-Hina at 2026/09/19 14:50
# leetgo: 1.4.18
# https://leetcode.cn/problems/maximum-product-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # 双状态 DP：dp_po=最大乘积，dp_ne=最小乘积（负负得正的关键）
        n = len(nums)
        dp_po = [1] * (n + 1)    # 以 nums[i-1] 结尾的最大乘积
        dp_ne = [1] * (n + 1)    # 以 nums[i-1] 结尾的最小乘积
        best = float("-inf")
        for i in range(n):
            dp_po[i + 1] = max(nums[i] * dp_po[i], nums[i] * dp_ne[i], nums[i])
            dp_ne[i + 1] = min(nums[i] * dp_po[i], nums[i] * dp_ne[i], nums[i])
            best = max(dp_po[i + 1], best)
        return best
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProduct(nums)
    print("\noutput:", serialize(ans, "integer"))
