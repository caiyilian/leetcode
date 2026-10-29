# Created by Chono-Hina at 2026/09/16 14:34
# leetgo: 1.4.18
# https://leetcode.cn/problems/permutations/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []
        result = []
        length = len(nums)

        def fun(path, exist):
            if len(path) == length:
                result.append(path.copy())          # ★ copy：path 共享引用
                return path
            for n in nums:                          # ⚡ 每次都从全部数里选（回头）
                if n in exist:
                    continue                        # 已用过 → 跳过
                exist.add(n)                        # 选
                path.append(n)
                path = fun(path, exist)             # 递归
                path.pop()                          # 撤销
                exist.remove(n)
            return path

        fun([], set())
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().permute(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
