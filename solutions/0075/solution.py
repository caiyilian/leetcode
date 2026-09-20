# Created by Chono-Hina at 2026/09/20 14:55
# leetgo: 1.4.18
# https://leetcode.cn/problems/sort-colors/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        # 荷兰国旗三指针：low=0区右界, curr=扫描, high=2区左界
        length = len(nums)
        low = 0
        curr = 0
        high = length - 1
        while curr <= high:
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                curr += 1
                low += 1
            elif nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1          # curr 不动（换来的还没检查）
            else:
                curr += 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().sortColors(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
