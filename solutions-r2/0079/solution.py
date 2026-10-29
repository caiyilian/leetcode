"""79. 单词搜索（二刷）——网格 DFS 回溯（O(m×n×4^L)/O(L) 标准解）

用户 AC 版（2026-10-29 18:58 提交 757649806，WA×2 → AC，3030ms/19.2MB）
- 从每个起点 DFS：当前格匹配 word[index] 就继续四方向，不匹配回退
- 防止走回头路：匹配时把 board[i][j] 置 '0'（标记已用），回溯恢复
- ⚡ AC 关键：成功判定用 index == length-1（当前格已匹配到最后一个字符直接 True）
  ——避免"提前 return 跳过棋盘恢复"导致后续搜索被污染（WA v2 的坑）
- ⚡ WA v1 坑：c = board[i][i] 列标写成 i（手误），恢复时存错字符
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)

        def fun(index, i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[index]:
                return False
            if index == length - 1:      # ★ 当前格已匹配到最后一位 → 直接成功
                return True

            c = board[i][j]              # 备份（★ 别写错下标！WA v1 的坑）
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


if __name__ == "__main__":
    s = Solution()
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    print(s.exist([r[:] for r in b], "ABCCED"))   # True
    print(s.exist([r[:] for r in b], "SEE"))      # True
    print(s.exist([r[:] for r in b], "ABCB"))     # False
    print(s.exist([["A"]], "A"))                  # True
    print(s.exist([["A", "B"], ["B", "A"]], "ABAB"))  # True（蛇形）