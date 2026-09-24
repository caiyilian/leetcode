# 399. 除法求值 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 399. 除法求值（Evaluate Division）· 中等（v2 新增题 · **带权图 + DFS**） |
| 链接 | https://leetcode.cn/problems/evaluate-division/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-24 |
| 最终提交 | ✅ **ACCEPTED - 29/29 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.3 MB |

## ⚡⚡ 图论重点标记（用户要求）

> 用户标记：**"这道题应该挺重要，我图相关的题目做得少"** —— 作为**图论入门代表题**重点复习。

**这题是图论入门的"三合一"训练**：
1. **建模**：把等式 `a/b = 2` 变成图的**有向边**（a→b 权 2，b→a 权 1/2）；
2. **遍历**：DFS/BFS 在图上**搜索路径**（不是单链走）；
3. **边权运算**：路径上边权**连乘**（a→b→c 得 a/c = 2×3 = 6）。

## 解法（用户带权图 + DFS）

```python
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))       # 正向边：a/b
            graph[b].append((a, 1 / values[i]))   # 反向边：b/a（倒数）
        results = []

        def dfs(cur, target, visited):
            if cur == target:
                return 1.0                        # 到达目标，乘数 1
            visited.add(cur)
            for neighbor, weight in graph[cur]:   # 遍历所有邻居
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:               # 找到路径
                        return weight * res       # 边权 × 后续结果
            return -1.0                           # 此路不通

        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1)                # 变量不在图中
            else:
                results.append(dfs(a, b, set()))
        return results
```

## 用户卡点回顾（3 个思维误区）

| 误区 | 错误写法 | 正确 |
|------|---------|------|
| ① graph 是"邻居列表" | `neighbor, value = graph[a]` | `for neighbor, weight in graph[cur]` |
| ② 没"换人" | `graph[a]` 里 a 从头到尾不变 | 需要 `cur` 变量沿路径推进 |
| ③ 当成"链"而非"图" | 单链直走 | **DFS/BFS 搜索**（图有分叉 + 需 visited 防环） |

**核心一句**：把图当成链 → 需要**图搜索**（遍历邻居、连乘边权、visited 防环、不通返回 -1）。

## 三个必查边界

1. **变量不在图中**（`a/e`、`x/x`）→ `-1.0`；
2. **`a == b` 且 a 在图中**（`a/a`）→ `1.0`；
3. **不连通** → `-1.0`。

## 验证

- 对拍 **自洽数据 3000 组（18000 个查询）0 不一致**；
- 样例：`[["a","b"],["b","c"]] / [2.0,3.0]` → `[6.0, 0.5, -1.0, 1.0, -1.0]` ✅。

## 复杂度

- 时间 **O(Q × (V+E))**（每个查询一次 DFS）；空间 O(V+E)。

## 关联：图论入门系列（v2）

| # | 题目 | 图论要点 |
|---|------|---------|
| 200 | 岛屿数量 | DFS/BFS 沉岛（网格图） |
| 207 | 课程表 | 拓扑排序（有向图） |
| 208 | 实现 Trie | 树形结构 |
| 994 | 腐烂的橘子 | 多源 BFS |
| **399** | **除法求值** | **带权图 + DFS（边权连乘）** |