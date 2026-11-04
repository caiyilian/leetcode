"""399. 除法求值（二刷）——带权有向图 + DFS（用户 AC 版）⚡ 图论重点

用户二刷（2026-11-04 13:54 提交 758548884，AC 一次通过，0ms/19.5MB）
- 抽象：变量=节点，等式 a/b=v → a --v--> b 且 b --1/v--> a（反向边取倒数）
- 查询 a/b = 路径上边权连乘（2×3=6）；查不到（缺变量/不连通）= -1
- 用户用嵌套字典（graph[a][b]=v）存图——字符串节点查边权 O(1)
- ⚡ 坑：visited 不加起点 a——否则 ["a","a"] 绕环回 a 被拦截返回 -1；
  隐式成立靠"任意闭合路径边权积=1"（商连环约分 a/b×b/a=1）
"""

from typing import List


# ===== 用户 AC 版（嵌套 dict + 隐式环处理） =====
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        hash_map = {}
        for i in range(len(equations)):
            a, b = equations[i]
            v = values[i]
            if a not in hash_map:
                hash_map[a] = {}
            if b not in hash_map:
                hash_map[b] = {}
            hash_map[a][b] = v
            hash_map[b][a] = 1 / v                      # ⚡ 反向边取倒数

        result = []

        def fun(a, b, weight, visited):
            if a not in hash_map or b not in hash_map:
                return -1
            for key, value in hash_map[a].items():
                if key in visited:                      # 防环
                    continue
                if key == b:
                    return weight * value               # 找到终点：累计乘积
                visited.add(key)
                v = fun(key, b, weight * value, visited)
                if v != -1:
                    return v                            # 该分支找到了就向上传
            return -1

        for a, b in queries:
            if a not in hash_map or b not in hash_map:
                result.append(-1)
                continue
            visited = set()
            v = fun(a, b, weight=1, visited=visited)     # ⚡ visited 不加 a：
            result.append(v)                             #   让 ["a","a"] 能绕环命中
        return result


# ===== 参考1：显式处理版（模板一刷风格，面试推荐——更直白） =====
from collections import defaultdict


class SolutionExplicit:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(cur, target, visited):
            if cur == target:                    # ⚡ 显式"到了"（含 cur 就是起点）
                return 1.0
            visited.add(cur)
            for nxt, w in graph[cur]:
                if nxt not in visited:
                    res = dfs(nxt, target, visited)
                    if res != -1.0:
                        return w * res
            return -1.0

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
                continue
            ans.append(dfs(a, b, set()))
        return ans


if __name__ == "__main__":
    s = Solution()
    eq = [["a", "b"], ["b", "c"]]
    v = [2.0, 3.0]
    q = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(s.calcEquation(eq, v, q))       # [6.0, 0.5, -1, 1.0, -1]