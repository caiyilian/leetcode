# Created by Chono-Hina at 2026/09/16 15:39
# leetgo: 1.4.18
# https://leetcode.cn/problems/subsets/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        result = [[]]
        def fun(path):
            if len(path) == length:
                return
            for n in nums:
                if n in path:
                    continue
                # 如果path是空，那就直接加，如果path不是空，加进去的必须是大于列表最后一个值
                if len(path) >= 1 and path[-1] > n:
                    continue
                path.append(n)
                result.append(path.copy())
                fun(path)
                path.pop()
        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
