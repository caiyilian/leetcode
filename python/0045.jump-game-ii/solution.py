# Created by Chono-Hina at 2026/09/18 18:32
# leetgo: 1.4.18
# https://leetcode.cn/problems/jump-game-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def jump(self, nums: list[int]) -> int:
        length = len(nums)
        step = 0
        far = 0
        end = 0
        for i in range(length - 1):        # 只到倒数第 2 个（终点不参与起跳）
            far = max(far, nums[i] + i)    # ① 每步更新最远可达
            if i == end:                   # ② 踩到当前层的墙 → 结算一步
                step += 1
                end = far                  #    墙推到 far（下一层的边界）
        return step
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jump(nums)
    print("\noutput:", serialize(ans, "integer"))
