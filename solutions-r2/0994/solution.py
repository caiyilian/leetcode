"""994. 腐烂的橘子（二刷）——多源 BFS 分层扩散（用户 AC 版）

用户二刷（2026-11-04 16:02 提交 758576710，AC 一次通过，3ms/19MB）
- 多源 BFS：先把所有烂橘子入队（多源），记录新鲜橘子总数 num_one
- while q and num_one：按层扩散（for _ in range(len(q)) 分层），每层 = 1 分钟，result += 1
- 感染成功（grid == 1 → 2）就入队并 num_one -= 1
- 结束：num_one 还剩 = 有新鲜橘子永远烂不到 → -1；否则 result
- ⚡ 分层技巧：for _ in range(len(q)) 固定一层的大小——"每分钟扩散一层"的标准 BFS 模板
"""

from typing import List
from collections import deque


# ===== 用户 AC 版（多源 BFS + 分层 + 计数） =====
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        m, n = len(grid), len(grid[0])
        num_one = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))            # 多源：所有烂橘入队
                elif grid[i][j] == 1:
                    num_one += 1                # 统计新鲜橘子
        result = 0
        while q and num_one:                    # ⚡ 还有鲜橘且还有扩散源才继续
            for _ in range(len(q)):             # ⚡ 分层：当前队列 = 这一分钟要扩散的
                i, j = q.popleft()
                grid[i][j] = 0                  # 已处理，标记掉
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    grid[i - 1][j] = 2
                    q.append((i - 1, j))
                    num_one -= 1
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    grid[i][j - 1] = 2
                    q.append((i, j - 1))
                    num_one -= 1
                if j + 1 < n and grid[i][j + 1] == 1:
                    grid[i][j + 1] = 2
                    q.append((i, j + 1))
                    num_one -= 1
                if i + 1 < m and grid[i + 1][j] == 1:
                    grid[i + 1][j] = 2
                    q.append((i + 1, j))
                    num_one -= 1
            result += 1                         # 一层 = 一分钟
        if num_one:
            return -1                           # 还有鲜橘烂不到
        return result


# ===== 参考：标准多源 BFS（方向数组版，更紧凑） =====
class SolutionStd:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        minutes = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            minutes += 1
            if fresh == 0:
                return minutes
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))    # 4
    print(s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))    # -1
    print(s.orangesRotting([[0, 2]]))                             # 0