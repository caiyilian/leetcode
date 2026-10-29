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

        def fun(index, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[index]:
                return False
            if index == length - 1:      # ★ 当前格已匹配到最后一位 → 直接成功
                return True

            c = board[i][j]              # 备份（★ 别写错下标！）
            board[i][j] = '0'            # 标记已用（防回头）
            if fun(index + 1, i - 1, j):
                return True
            if fun(index + 1, i, j - 1):
                return True
            if fun(index + 1, i + 1, j):
                return True
            if fun(index + 1, i, j + 1):
                return True
            board[i][j] = c              # 恢复
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if fun(0, i, j):
                        return True
        return False
        

# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().exist(board, word)
    print("\noutput:", serialize(ans, "boolean"))
