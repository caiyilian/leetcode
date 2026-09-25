# Created by Chono-Hina at 2026/09/25 15:32
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 归位法（数组即哈希）：值 v 应放在下标 v-1
        length = len(nums)
        for i in range(length):
            while nums[i] != (i + 1):          # 当前位置元素没归位
                if nums[i] == nums[nums[i] - 1]:
                    break                      # 目标位置已是正确值 → 重复元素
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]   # 交换归位
        result = []
        for i in range(length):
            if nums[i] != (i + 1):             # 错位的下标 i → 缺失 i+1
                result.append(i + 1)
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDisappearedNumbers(nums)
    print("\noutput:", serialize(ans, "integer[]"))
