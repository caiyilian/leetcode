"""240. 搜索二维矩阵 II（二刷）——右上角阶梯搜索（O(m+n) 最优解）

用户 AC 版（2026-10-18 20:50 提交 755577703，一次通过）
核心：从右上角出发，每比较一次必排除一整行或一整列（最多 m+n 步）。
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top = 0
        right = n - 1                      # 从右上角出发
        while top < m and right >= 0:
            if matrix[top][right] == target:
                return True
            if matrix[top][right] > target:
                right -= 1                 # 右上角太大 → 整列都比 target 大，排除整列
            else:
                top += 1                   # 右上角太小 → 整行都比 target 小，排除整行
        return False


if __name__ == "__main__":
    s = Solution()
    m = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
         [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(s.searchMatrix(m, 5))    # True
    print(s.searchMatrix(m, 20))   # False