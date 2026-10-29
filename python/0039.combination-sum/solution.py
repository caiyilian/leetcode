# Created by Chono-Hina at 2026/09/16 16:45
# leetgo: 1.4.18
# https://leetcode.cn/problems/combination-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def fun(path, now_sum=0, start=0):
            if now_sum == target:
                result.append(path.copy())          # ★ copy：path 后续还会被修改
                return path
            if now_sum > target:
                return path
            for n in candidates[start:]:            # 从 start 开始（不回头）
                if now_sum + n > target:
                    break                            # 已排序：后面更大，剪枝
                path.append(n)
                path = fun(path, now_sum + n, start)  # 传 start：可重复选当前数
                path.pop()
                start += 1                            # 本层循环自增：下一个数才可选
            return path

        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
