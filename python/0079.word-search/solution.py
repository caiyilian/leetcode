# Created by Chono-Hina at 2026/09/16 19:57
# leetgo: 1.4.18
# https://leetcode.cn/problems/word-search/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        def fun(i, j, index):
            if index == length:                    # ① 匹配完整个单词 → 成功（必须放最前！）
                return True
            if i < 0 or j < 0 or i >= m or j >= n: # ② 越界 → 这条路走不通
                return False
            if board[i][j] != word[index]:         # ③ 字符不符 → 失败
                return False
            ori = board[i][j]
            board[i][j] = ""                       # ④ 标记访问（防止重复踩到）
            if fun(i+1, j, index+1):
                return True
            if fun(i-1, j, index+1):
                return True
            if fun(i, j+1, index+1):
                return True
            if fun(i, j-1, index+1):
                return True
            board[i][j] = ori                      # ⑤ 撤销（回溯）
            return False                           # ⑥ 四方向都失败 → False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    reb = fun(i, j, index=0)
                    if reb:
                        return True
        return False
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().exist(board, word)
    print("\noutput:", serialize(ans, "boolean"))
