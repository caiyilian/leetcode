# Created by Chono-Hina at 2026/09/11 20:59
# leetgo: 1.4.18
# https://leetcode.cn/problems/3sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 2):
            target = nums[i]
            if target > 0:                        # 剪枝：最小的数都 > 0
                break
            if i > 0 and target == nums[i - 1]:   # i 侧去重
                continue
            j, k = i + 1, n - 1
            while j < k:
                left, right = nums[j], nums[k]
                s = target + left + right
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    res.append([target, left, right])
                    j += 1
                    k -= 1
                    # 两侧值同时不变才是重复（Δj = Δk = 0），同步跳过
                    while j < k and nums[j] == left and nums[k] == right:
                        j += 1
                        k -= 1
        return res

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
