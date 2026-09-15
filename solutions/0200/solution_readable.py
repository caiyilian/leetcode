# -*- coding: utf-8 -*-
"""
第 200 题 岛屿数量 · BFS 参照版（与用户 DFS 沉没法独立实现，5 万组对拍一致）
网格题第二个武器：队列 BFS（994 腐烂的橘子、102 层序的网格版）。
用 visited 二维数组标记（不原地修改网格）。
"""
from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    q = deque([(i, j)])
                    visited[i][j] = True
                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < m and 0 <= ny < n
                                    and grid[nx][ny] == '1' and not visited[nx][ny]):
                                visited[nx][ny] = True
                                q.append((nx, ny))
        return count