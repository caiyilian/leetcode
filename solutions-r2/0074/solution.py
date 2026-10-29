"""74. 搜索二维矩阵（二刷）——二维拍平 + 标准二分（O(log(m×n))/O(1) 标准解）

用户 AC 版（2026-10-29 22:48 提交 757692948，一次通过，0ms/19.3MB）
- 矩阵每行从左到右递增、每行第一个数 > 上一行最后一个数 → 整体可视为一个递增的一维数组
- 一维下标 mid → 二维 (mid//n, mid%n)，直接套 35 的左闭右闭二分模板
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = mid // n, mid % n           # 一维 → 二维换算
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    m1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(s.searchMatrix(m1, 3))    # True
    print(s.searchMatrix(m1, 13))   # False
    print(s.searchMatrix([[1]], 1))  # True
    print(s.searchMatrix([[1]], 2))  # False