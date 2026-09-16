# Created by Chono-Hina at 2026/09/16 14:34
# leetgo: 1.4.18
# https://leetcode.cn/problems/permutations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        length = len(nums)
        result = []
        def fun(path):
            if len(path) == length:
                # 如果不复制的话，后面 path.pop，也会影响到 result 的列表，因为就类似指针
                result.append(path.copy())
                return
            for n in nums:
                if n in path:      # 已用过的数字不能再选
                    continue
                path.append(n)     # ① 选
                fun(path)          # ② 递归
                path.pop()         # ③ 撤销（回溯的灵魂）
        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().permute(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
