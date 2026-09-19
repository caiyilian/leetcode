# -*- coding: utf-8 -*-
"""
第 62 题 不同路径 · 记忆化递归版（top-down，用户第一版 AC）

与迭代版（solution.py）m,n=1..19 全量对拍 0 差异。
从终点往回推：fun(i,j) = fun(i+1,j) + fun(i,j+1)（向右 + 向下）。
"""
from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        mem = {(m - 2, n - 1): 1, (m - 1, n - 2): 1}   # 终点左边/上边 = 1
        def fun(i, j):
            if i >= m or j >= n:
                return 0
            if (i, j) not in mem:
                mem[(i, j)] = fun(i + 1, j) + fun(i, j + 1)
            return mem[(i, j)]
        return fun(0, 0)