# Created by Chono-Hina at 2026/09/17 20:38
# leetgo: 1.4.18
# https://leetcode.cn/problems/daily-temperatures/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        index_stack = []              # ★ 存下标（距离 = i - idx）
        result = [0] * length         # 全 0：没被顶掉的（后面无更高温）= 0

        for i in range(length):
            while index_stack and temperatures[index_stack[-1]] < temperatures[i]:
                result[index_stack[-1]] = i - index_stack[-1]   # 定点填（弹出谁给谁）
                index_stack.pop()
            index_stack.append(i)
        return result
        

# @lc code=end

if __name__ == "__main__":
    temperatures: List[int] = deserialize("List[int]", read_line())
    ans = Solution().dailyTemperatures(temperatures)
    print("\noutput:", serialize(ans, "integer[]"))
