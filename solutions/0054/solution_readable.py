# -*- coding: utf-8 -*-
"""
第 54 题 螺旋矩阵 · 可读性优化版
逻辑与用户原版一致：方向轮转 + 四边界收缩（无 visited 数组，O(1) 额外空间）
改进：变量名清晰（right_b/bottom_b/left_b/top_b），去掉原版 dir_max[-1] 负索引写法，
      用 len(result) < m*n 替代 count 计数变量
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        right_b, bottom_b, left_b, top_b = n, m, 0, 0  # 四个方向的边界
        result = [matrix[0][0]]
        i = j = 0
        direction = 0  # 0→右 1→下 2→左 3→上
        while len(result) < m * n:
            if direction == 0:      # 向右：走到 right_b-1 处转向
                if j < right_b - 1:
                    j += 1
                    result.append(matrix[i][j])
                else:
                    top_b += 1      # 上边界下移一行
                    direction = 1
            elif direction == 1:    # 向下：走到 bottom_b-1 处转向
                if i < bottom_b - 1:
                    i += 1
                    result.append(matrix[i][j])
                else:
                    right_b -= 1    # 右边界左移一列
                    direction = 2
            elif direction == 2:    # 向左：走到 left_b 处转向
                if j > left_b:
                    j -= 1
                    result.append(matrix[i][j])
                else:
                    bottom_b -= 1   # 下边界上移一行
                    direction = 3
            else:                   # 向上：走到 top_b 处转向
                if i > top_b:
                    i -= 1
                    result.append(matrix[i][j])
                else:
                    left_b += 1     # 左边界右移一列
                    direction = 0
        return result
