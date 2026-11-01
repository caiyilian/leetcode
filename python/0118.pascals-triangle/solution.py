# Created by Chono-Hina at 2026/09/18 20:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/pascals-triangle/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 逐行构造：首尾补 1，中间元素 = 上一行相邻两数之和
        result = [[1]]
        for layer in range(1, numRows):
            each_list = [1]                                   # 首 1
            for i in range(1, layer):
                each_list.append(result[-1][i - 1] + result[-1][i])  # 上邻和
            each_list.append(1)                               # 尾 1
            result.append(each_list)
        return result
        

# @lc code=end

if __name__ == "__main__":
    numRows: int = deserialize("int", read_line())
    ans = Solution().generate(numRows)
    print("\noutput:", serialize(ans, "integer[][]"))
