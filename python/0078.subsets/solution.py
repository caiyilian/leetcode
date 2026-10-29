# Created by Chono-Hina at 2026/09/16 15:39
# leetgo: 1.4.18
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = [[]]                    # 空集
        length = len(nums)

        def fun(path, start):
            if len(path) == length:      # 满长度结束（边界保护）
                return path
            for i, n in enumerate(nums[start:]):
                path.append(n)
                result.append(path.copy())     # ★ 每进入一个节点就收集（子集=所有路径）
                path = fun(path, start + i + 1)  # 不回头
                path.pop()
            return path

        fun([], 0)
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
