# Created by Chono-Hina at 2026/09/16 16:45
# leetgo: 1.4.18
# https://leetcode.cn/problems/combination-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        length = len(candidates)
        candidates.sort()
        def fun(path, index=0, now_sum=0):
            if now_sum > target:
                return
            if now_sum == target:
                result.append(path.copy())
            for i in range(index, length):
                n = candidates[i]
                if now_sum + n > target:
                    break              # 排序后后面更大，全部超 → break 剪枝
                path.append(n)
                fun(path, i, now_sum+n)  # 以 i 为节点，只用 i 之后的（防重复组合）+ 可重复用 i
                path.pop()
        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
