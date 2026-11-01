# Created by Chono-Hina at 2026/09/19 13:55
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-increasing-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 进阶 O(n log n)：tails[k] = 长度 k+1 递增子序列的最小末尾（严格递增 → 可二分）
        # 新数 x：比所有尾巴大 → 追加（新长度）；否则二分替换"第一个 >= x"的位置（尾巴变小留空间）
        length = len(nums)
        tails = [nums[0]]
        for i in range(1, length):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                left, right = 0, len(tails)
                while left <= right:
                    mid = (left + right) // 2
                    if tails[mid] == nums[i]:
                        break
                    if tails[mid] > nums[i]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    tails[left] = nums[i]
        return len(tails)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
