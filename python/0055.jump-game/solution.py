# Created by Chono-Hina at 2026/09/18 17:21
# leetgo: 1.4.18
# https://leetcode.cn/problems/jump-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = 0
        length = len(nums)
        for i in range(length - 1):          # ⚡ 只到 length-1（末尾 0 不算死路）
            if far == i and nums[i] == 0:    # 当前位置无法越过 → 死路
                return False
            far = max(far, i + nums[i])
        return True
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canJump(nums)
    print("\noutput:", serialize(ans, "boolean"))
