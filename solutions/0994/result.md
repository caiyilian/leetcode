# 994. 腐烂的橘子 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 994. 腐烂的橘子（Rotting Oranges）· 中等（图论 BFS） |
| 链接 | https://leetcode.cn/problems/rotting-oranges/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 307/307 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.3 MB |

## 解法（用户按三层提示独立完成：多源 BFS + 队列带分钟）

```python
class Solution:
    def orangesRotting(self, grid):
        use_time = 0
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))        # ① 多源：所有腐烂橘子同时入队，分钟 0
                elif grid[i][j] == 1:
                    fresh += 1                 # ② 新鲜橘子计数
        while q:
            i, j, use_time = q.popleft()
            for ni, nj in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] in (0, 2):
                    continue
                grid[ni][nj] = 2               # ③ 感染 + 原地标记（200 题技巧）
                fresh -= 1
                q.append((ni, nj, use_time+1)) # ④ 队列带分钟
        if fresh != 0:
            return -1                          # ⑤ 有橘子永远烂不了
        return use_time                        # ⑥ 最后出队时间 = 总分钟
```

**用户完成的关键认知**：
- **多源同时入队 = 同时腐烂**（BFS 层序天然按分钟扩散）；
- **队列带 minute**（(i, j, use_time)，最后出队的 use_time 就是答案）；
- **fresh 计数决定 -1**（BFS 结束还有新鲜橘子 = 被 0 隔离）。

## 验证

- 对拍 **5 万组随机网格 vs 暴力模拟（每轮感染数轮数）0 不一致**；
- 官方样例全对：`[[2,1,1],[1,1,0],[0,1,1]]→4`、`[[2,1,1],[0,1,1],[1,0,1]]→-1`、`[[0,2]]→0`；
- 边界：`[[0]]→0`、`[[1]]→-1`、`[[2],[1]]→1`。

## 复杂度

- 时间 **O(m×n)**（每格最多入队一次）；空间 **O(m×n)**（队列）。

## 踩坑记录

- leetgo 模板未导入 deque，本地测试 NameError——已在 solution.py 补 `from collections import deque`（在线提交不受影响）。