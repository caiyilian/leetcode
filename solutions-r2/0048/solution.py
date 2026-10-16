"""48. 旋转图像（二刷）——逐层旋转 + 四元素轮换（O(n²)/O(1) 最优解）

用户 AC 版（2026-10-16 10:59 提交 755137606，一次通过）
核心：一层层"剥洋葱"，每层对每一列做一次"上→右→下→左"四元素轮换。
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while (n - 2 * i) >= 2:              # 逐层：最外层 n，往里一层 n-2，边长 <2 停止
            for j in range(i, n - 1 - i):    # 本层每一列做一次四元素轮换
                # 上 → 右 → 下 → 左，三轮交换完成一个环
                matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]
                matrix[i][j], matrix[n - 1 - i][n - j - 1] = matrix[n - 1 - i][n - j - 1], matrix[i][j]
                matrix[i][j], matrix[n - j - 1][i] = matrix[n - j - 1][i], matrix[i][j]
            i += 1


# ========== 可读版：临时变量表达"四元素轮换"（语义更直白）==========
class SolutionReadable:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):                      # 层
            for j in range(i, n - 1 - i):            # 本层列
                tmp = matrix[i][j]                   # 上
                matrix[i][j] = matrix[n - j - 1][i]         # 上 ← 左
                matrix[n - j - 1][i] = matrix[n - 1 - i][n - j - 1]   # 左 ← 下
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 - i]  # 下 ← 右
                matrix[j][n - 1 - i] = tmp           # 右 ← 上


if __name__ == "__main__":
    s = Solution()
    for m, exp in [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
                   ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                    [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])]:
        s.rotate(m)
        print(m, '✓' if m == exp else '✗')