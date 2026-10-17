"""73. 矩阵置零（二刷）——第一行/第一列标记法（O(m×n)/O(1) 最优解）

用户 AC 版（2026-10-17 21:57 提交 755418559，一次通过）
核心：用矩阵自身的第一行/第一列当"标记区"，记录哪些行/列要置零；
      先抓拍第一行/第一列本身是否有 0（flag），最后再恢复它们。
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # ① 抓拍：第一行/第一列本身是否有 0（后面会被当标记覆盖，必须先记录）
        flag_row = any(x == 0 for x in matrix[0])
        flag_col = any(matrix[i][0] == 0 for i in range(m))
        # ② 遍历内部：遇到 0 → 在标记区（第一行/第一列）打标
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0      # 第 j 列要置零
                    matrix[i][0] = 0      # 第 i 行要置零
        # ③ 按标记把内部格子置零
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        # ④ 恢复第一行/第一列本身（按抓拍结果）
        if flag_row:
            for j in range(n):
                matrix[0][j] = 0
        if flag_col:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    s = Solution()
    for mtx, exp in [([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
                     ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
                     ([[0, 1], [1, 1]], [[0, 0], [0, 1]]),
                     ([[1, 1], [1, 0]], [[1, 0], [0, 0]])]:
        s.setZeroes(mtx)
        print(mtx, '✓' if mtx == exp else '✗')