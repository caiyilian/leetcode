# Created by Chono-Hina at 2026/09/15 23:12
# leetgo: 1.4.18
# https://leetcode.cn/problems/rotting-oranges/

from typing import *
from leetgo_py import *
from collections import deque

# @lc code=begin

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        腐蚀，每一个新鲜果子，记录一下，自身被腐蚀的时间，初始化是inf
        每一次腐蚀，记录时间，但是如果比上次的短，那就把腐蚀时间根上次取Min
        """
        use_time = 0
        m, n = len(grid), len(grid[0])
        q = deque()  # 初始化一个队列
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:  # 腐烂果子
                    q.append((i, j, 0))  # 记录位置以及当前处于0分钟，因为是自身
                elif grid[i][j] == 1:
                    fresh += 1  # 记录新鲜果的数量
        while q:
            # 遍历所有腐烂果子，都走一次
            i, j, use_time = q.popleft()
            for ni, nj in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] in (0, 2):
                    continue
                grid[ni][nj] = 2
                fresh -= 1
                q.append((ni, nj, use_time+1))
        if fresh != 0:
            return -1
        return use_time
        

# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().orangesRotting(grid)
    print("\noutput:", serialize(ans, "integer"))
