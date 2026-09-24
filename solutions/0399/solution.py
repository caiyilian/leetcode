# Created by Chono-Hina at 2026/09/24 18:10
# leetgo: 1.4.18
# https://leetcode.cn/problems/evaluate-division/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 带权有向图 + DFS：a/b=2, b/c=3 → a/c = 2*3（边权连乘）
        graph = defaultdict(list)
        # 建图：双向边，反向边权取倒数
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        # 查询
        results = []

        def dfs(cur, target, visited):
            if cur == target:
                return 1.0                      # 到达目标，乘数 1
            visited.add(cur)
            for neighbor, weight in graph[cur]:  # 遍历所有邻居（不是 unpack 单个）
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:              # 找到路径
                        return weight * res      # 边权 × 后续结果
            return -1.0                          # 此路不通

        for a, b in queries:
            if a not in graph or b not in graph:
                results.append(-1)               # 变量不在图中
            else:
                results.append(dfs(a, b, set()))
        return results
        

# @lc code=end

if __name__ == "__main__":
    equations: List[List[str]] = deserialize("List[List[str]]", read_line())
    values: List[float] = deserialize("List[float]", read_line())
    queries: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().calcEquation(equations, values, queries)
    print("\noutput:", serialize(ans, "double[]"))
