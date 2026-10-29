# Created by Chono-Hina at 2026/09/16 21:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/n-queens/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        """
        按行摆放
        首先，不在同一列就是j不相同
        不在对角线
        斜率为正的对角线：i j, i-1,j+1 所以就是 i+j 不变
        斜率为负的对角线：i j, i-j 不变
        """
        ban_j = set()      # 已占用的列
        ban_ipj = set()    # 已占用的副对角线（i+j 恒定）
        ban_idj = set()    # 已占用的主对角线（i-j 恒定）
        result = []

        def fun(path, i=0):
            if len(path) == n:
                result.append(path.copy())
                return
            for j in range(n):
                if (j in ban_j) or (i - j in ban_idj) or (i + j in ban_ipj):
                    continue
                ban_j.add(j)
                ban_ipj.add(i + j)
                ban_idj.add(i - j)
                path.append("." * j + "Q" + "." * (n - j - 1))
                fun(path, i + 1)
                ban_j.remove(j)
                ban_ipj.remove(i + j)
                ban_idj.remove(i - j)
                path.pop()

        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().solveNQueens(n)
    print("\noutput:", serialize(ans, "string[][]"))
