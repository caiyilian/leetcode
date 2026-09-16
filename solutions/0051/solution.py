# Created by Chono-Hina at 2026/09/16 21:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/n-queens/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        # 预生成每列对应的行字符串（"."*j + "Q" + "."*(n-j-1)），避免每次拼接
        temp = ["." * num + "Q" + "." * (n - num - 1) for num in range(n)]

        def fun(path, i, col, diag1, diag2):
            if i == n:                    # 放满 n 行（每行一个皇后，天然不同行）
                result.append(path.copy())
                return
            for j in range(n):
                # 列冲突 / 两条对角线冲突（同一斜线 i+j 或 i-j 相等）
                if j not in col and (i + j) not in diag1 and (i - j) not in diag2:
                    path.append(temp[j])
                    col.add(j)
                    diag1.add(i + j)      # ↘ 对角线编号
                    diag2.add(i - j)      # ↙ 对角线编号
                    fun(path, i + 1, col, diag1, diag2)
                    path.pop()
                    col.remove(j)         # 回溯撤销三集合
                    diag1.remove(i + j)
                    diag2.remove(i - j)

        fun([], 0, set(), set(), set())
        return result
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().solveNQueens(n)
    print("\noutput:", serialize(ans, "string[][]"))
