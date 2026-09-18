# Created by Chono-Hina at 2026/09/18 18:32
# leetgo: 1.4.18
# https://leetcode.cn/problems/jump-game-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def jump(self, nums: list[int]) -> int:
        # 双 far 贪心：curr_far=当前这跳的边界，next_far=下一跳能到的最远
        curr_far = 0
        next_far = 0
        step = 0
        length = len(nums)
        for i, n in enumerate(nums):
            next_far = max(next_far, n + i)          # 试探：这范围内能跳最远到哪
            if i == curr_far and i != length - 1:    # 走到当前段尽头（且没到终点）
                step += 1                            # 必须再跳一次
                curr_far = next_far                  # 下一跳范围 = 试探出的最远
        return step
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().jump(nums)
    print("\noutput:", serialize(ans, "integer"))
