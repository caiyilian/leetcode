# -*- coding: utf-8 -*-
"""
第 48 题 旋转图像 · 可读性优化版
逻辑与用户原版一致：逐层旋转 + 四元素轮换（三次交换实现环），原地 O(1) 空间
改进：为每个位置的坐标标注含义，四元素环的走向一目了然
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for layer in range(n // 2):          # 逐层处理（外圈 → 内圈）
            # 当前层的四个角：
            #   上边起始 (layer, layer)   右边起始 (layer, n-1-layer)
            #   下边起始 (n-1-layer, n-1-layer)   左边起始 (n-1-layer, layer)
            for i in range(n - 1 - 2 * layer):  # 每层每边要轮换的位置数
                # 四个目标位置：
                top    = (layer, i + layer)                 # 上边第 i 格
                right  = (i + layer, n - 1 - layer)         # 右边第 i 格
                bottom = (n - 1 - layer, n - 1 - i - layer) # 下边第 i 格
                left   = (n - 1 - i - layer, layer)         # 左边第 i 格

                # 顺时针 90°：left → top → right → bottom → left
                # 用三次交换把环转起来（先备份 top 于 right，逐步覆盖）
                matrix[top[0]][top[1]], matrix[right[0]][right[1]] = \
                    matrix[right[0]][right[1]], matrix[top[0]][top[1]]
                matrix[top[0]][top[1]], matrix[bottom[0]][bottom[1]] = \
                    matrix[bottom[0]][bottom[1]], matrix[top[0]][top[1]]
                matrix[top[0]][top[1]], matrix[left[0]][left[1]] = \
                    matrix[left[0]][left[1]], matrix[top[0]][top[1]]