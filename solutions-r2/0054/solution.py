"""54. 螺旋矩阵（二刷）——四边界收缩法（O(m×n)/O(1) 最优解）

用户 AC 版（2026-10-17 21:26 提交 755412584，一次通过）
核心：top/bottom/left/right 圈住未遍历区域，按 右→下→左→上 收割，每收一条边边界缩一格。
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, top, bottom, right = 0, 0, m - 1, n - 1
        result = []
        while right >= left and bottom >= top:          # 区域还活着才进
            # ① 上边（左→右）
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            # ② 右边（上→下）——步间检查：收完上边后可能已空
            if bottom >= top and right >= left:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
            # ③ 下边（右→左）
            if right >= left and bottom >= top:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            # ④ 左边（下→上）
            if bottom >= top and right >= left:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))          # [1,2,3,6,9,8,7,4,5]
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(s.spiralOrder([[1, 2, 3, 4]]))                             # [1,2,3,4]
    print(s.spiralOrder([[1], [2], [3]]))                            # [1,2,3]