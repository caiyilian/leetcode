# 207. 课程表 · 解析

## 题目简述

`numCourses` 门课（编号 0~n-1），`prerequisites[i] = [a, b]` 表示**先学 b 才能学 a**。判断能否修完所有课（课程依赖图是否**无环**——有环则永远学不完）。

**本质：有向图判环**（能拓扑排序 ⇔ 无环）。

## 核心套路：Kahn 拓扑排序（BFS 队列版）

**拓扑排序**：给课程排一个"先学后学"的线性顺序，使得每条边 `b → a` 都满足 b 在 a 前面。**能排出来 ⇔ 无环 ⇔ 能学完所有课**。

### 三步构造

1. **入度表**：`count_dict[a]` = a 有多少门前置没学（入度 = 指向 a 的边数）；
2. **出边表**：`need_dict[b]` = 依赖 b 的课程列表（b 学完后要通知谁）；
3. **队列消入度**：入度 0 的课可直接学（入队）→ 出队学掉 → 依赖它的课入度 -1 → 谁减到 0 谁入队。

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        count_dict = defaultdict(int)        # 入度表
        need_dict = defaultdict(list)        # 出边表
        for back, before in prerequisites:
            count_dict[back] += 1            # 边 before -> back：back 入度 +1
            need_dict[before].append(back)
        q = deque([i for i in range(numCourses) if count_dict[i] == 0])
        learned = 0
        while q:
            for _ in range(len(q)):
                num = q.popleft()
                learned += 1
                for need in need_dict[num]:
                    count_dict[need] -= 1
                    if count_dict[need] == 0:
                        q.append(need)
        return learned == numCourses
```

## 演进史：v1 粗暴版 → v2 队列版（用户自驱优化）

### v1（O(V²)）：每轮全扫

```python
while True:
    learn_round = 0
    for i in range(numCourses):          # 每轮全扫所有课程
        if i not in learned and count_dict[i] == 0:
            learned.add(i)
            ...减依赖入度...
    if learn_round == 0:
        break
```

**问题**：最多 V 轮 × 每轮扫 V 个 = **O(V²)**。虽然正确，但"找入度 0"完全可以用事件驱动。

### v2（O(V+E)）：队列事件驱动（定稿）

**核心认知（用户自悟）**：

> **"入度变 0"不是扫出来的，是被"前置刚学掉"这个事件触发的**——谁的前置学完了、入度减到 0，谁就立刻可以学。用队列维护"当前可学"，天然无轮次扫描。

每个节点入队/出队一次（O(V)），每条边被减一次（O(E)）→ **O(V+E)**。

### 102 快照分层的迁移（加分点）

`for _ in range(len(q))` 让"同一轮可学的"一起出队——**不是必需的**（deque 天然 FIFO，不分层也是正确拓扑序），但保留"轮"的直觉、可读性好，是用户跨题迁移模式的又一例证（200 → 994 → 207 连续三次复用）。

## 为什么能判环

- **无环图**：至少有一个入度 0 的节点，每轮都有可学的 → 最终 learned == V；
- **有环图**：环上的课程互相依赖，永远没人入度减到 0 → 队列提前空 → learned < V。

（也可以从"每个节点入队次数 ≤ 1"理解：入度只减一次到 0，重复入队不可能——用户的 learned 计数因此无需 set。）

## 复杂度

- 时间 **O(V+E)**；空间 **O(V+E)**（两张表）。

## 考点

- **拓扑排序（Kahn）**：入度表 + 出边表 + 队列消入度
- 有向图判环（拓扑序存在性）
- 事件驱动 vs 轮询扫描（复杂度优化的思维）
- 快照分层复用（102 → 207）

## 易错点

1. **边的方向**：`[a, b]` 是 `b → a`（先学 b）——入度加在 a 上，出边挂在 b 上，搞反全盘皆错；
2. `defaultdict` / `deque` 忘 import（本地 NameError）；
3. 初始入队的是**全部**入度 0 的课（不止一个）；
4. 判断用 `learned == numCourses`（有孤立课程也要算——它们入度 0 初始就在队列里）；
5. 无环但不在 prerequisites 里的课程（入度天然 0）别漏。

## 关联题

- **210 课程表 II**：同题要求输出拓扑序（把 `learned` 计数改成收集列表）；
- **802 找到最终的安全状态**：反向拓扑；
- **994 腐烂的橘子**：同样是"队列事件驱动"思维（感染 = 事件）。