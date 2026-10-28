# 207. 课程表 · 解析（二刷）

## 一、核心思路：能不能学完 = 图有没有环

把课程当作**有向图**：`[ai, bi]` 表示"学 ai 之前必须先学 bi" → 边 `bi → ai`。

- **能学完所有课** ⇔ 不存在环（有环则环上的课互相依赖，永远学不完）；
- 所以本题 = **拓扑排序判环**。

```
0 → 1 → 2    无环，可学完（顺序 0,1,2 或 0,2...）
0 → 1 → 0    有环，学不完 → False
```

## 二、标准解法：Kahn（BFS 入度法）

**核心思想**：入度 = 这门课有几个先修。**入度 0 的课可以学**，学完把它所有后继的入度 -1，减到 0 的又可以学——用**队列**天然管理这个流程：

```python
from collections import defaultdict, deque

def canFinish(self, numCourses, prerequisites):
    indeg = [0] * numCourses                 # 入度数组
    out = defaultdict(list)                  # 邻接表：bi → [ai...]
    for ai, bi in prerequisites:
        indeg[ai] += 1
        out[bi].append(ai)

    q = deque([i for i in range(numCourses) if indeg[i] == 0])   # 初始可学课程
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1                             # 学掉一门
        for v in out[u]:
            indeg[v] -= 1                    # 后继先修 -1
            if indeg[v] == 0:
                q.append(v)                  # ★ 减到 0 立即入队
    return cnt == numCourses                 # 学完的课 = 总数 → 无环
```

**关键心法：`入度减到 0 就入队`**——不需要每轮重新扫全表找零入度（用户版就是在这退化成 O(n²) 的）。

## 三、⚡ 用户版 vs 标准版

用户版思路对（每轮找零入度全学掉），但 `while len(learned) < numCourses: for i in range(numCourses): ...` 每轮 O(n) 扫全表，最坏 **O(n²)**（一刷 7ms vs 二刷 255ms ≈ 40 倍）。

改成队列版：**初始把所有零入度入队，弹一个就减后继、减到 0 再入队**——O(n+e)，每门课/每条边只处理一次。

## 四、复杂度

- 时间：O(n+e)（Kahn 队列版）
- 空间：O(n+e)（邻接表 + 入度数组）

## 五、一刷 vs 二刷

- 一刷（9-16）：标准 Kahn AC ×3（7ms）；
- 二刷（10-28）：多轮扫描版（思路对、写法 O(n²)）——归档主解用标准 Kahn，用户版留档对比。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| Kahn 拓扑 | **210 课程表 II**（返回拓扑序不是判环）、207 本体 |
| DFS 三色环检测 | 207 另一解（灰白黑染回边）、802 找到最终的安全状态 |
| 拓扑序应用 | 310 最小高度树（剥叶子）、269 火星词典（进阶） |

**207/210 是图论拓扑排序的入门对**：207 判环，210 返回顺序，Kahn 一套代码两个题。

## 七、一句话记住

> **课程表 = Kahn 拓扑判环：入度 0 入队，弹出学掉、后继入度 -1、减到 0 再入队；学的课数 = 总数即无环。记住"减到 0 立即入队"，别每轮扫全表（O(n²)）。**