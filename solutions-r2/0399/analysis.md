# 399. 除法求值 · 解析（二刷）⚡ 图论重点

## 一、题目

- 中文：除法求值
- English：Evaluate Division
- 难度：中等（图论 + DFS/并查集）
- 问题：给若干除法等式（a/b = v），查任意两个变量的比值

## 二、核心抽象：等式 → 带权有向图

**关键第一步（也是最难的）**：把 `a / b = v` 翻译成图：

```
a/b = 2.0  →  节点 a --2.0--> b  且  b --1/2.0--> a（反向边取倒数！）
```

- **变量 = 节点**（注意是字符串，不是数字下标）
- **比值 = 边权**
- 建图时**必须建两条边**（正 + 反倒数），否则反向查询全错

## 三、查询 = 找路径，答案 = 边权连乘

```
query ["a","c"]：路径 a→b→c，答案 = 2.0 × 3.0 = 6.0
query ["b","a"]：b→a 直达边 0.5
```

**为什么是连乘**：`a/c = (a/b) × (b/c)`——中间变量约掉了，商沿着路径连乘。

**三种返回 -1 的情况**：
| 情况 | 处理 |
|------|------|
| `x/x` 且 x 在图中 | 1.0（自己除自己）|
| 起点或终点**不在图中** | -1.0 |
| 在图里但**不连通** | -1.0 |

## 四、DFS 写法（用户 AC 版，嵌套 dict）

```python
# 建图：graph[a][b] = v（dict 嵌套 dict，字符串节点 O(1) 查边）
hash_map[a][b] = v
hash_map[b][a] = 1 / v

# 查询 DFS
def fun(a, b, weight, visited):
    if a not in hash_map or b not in hash_map:
        return -1
    for key, value in hash_map[a].items():      # 遍历所有邻居
        if key in visited:
            continue
        if key == b:
            return weight * value               # 到终点：返回累计乘积
        visited.add(key)
        v = fun(key, b, weight * value, visited) # 递归：乘积累乘
        if v != -1:
            return v                            # 找到就向上传
    return -1

for a, b in queries:
    if a not in hash_map or b not in hash_map:
        result.append(-1); continue
    v = fun(a, b, weight=1, visited=set())      # ⚡ 每 query 新建 visited！
    result.append(v)
```

## 五、⚡ 两个关键坑（本次实战验证）

1. **每 query 必须新建 visited**：不能跨 query 复用——第一次搜索走过的节点会"隔离"第二次的路径，导致假 -1；
2. **visited 加不加起点 a**（用户亲手踩）：用户版没显式处理"起点==终点"，`["a","a"]` 靠"绕环回 a"命中（`key == a` 命中），所以 **visited 不能加 a**；若加 a，绕环被拦截 → 判 -1。
   - 隐式成立的原理：**任意闭合路径的边权积恒为 1**（a/b × b/c × c/a = 1，商约分）——绕一圈回 a 的乘积恰好是 1.0；
   - 更稳的写法：DFS 开头显式 `if a == b: return 1.0`，这样 visited 可放心加 a（防环更严谨），且语义直白。**面试推荐显式版**。

## 六、复杂度

- 时间：O(Q × (V+E))（每个查询独立 DFS 走全图）
- 空间：O(V+E)（图）

（进阶：带权并查集可把每个查询压到 O(α)、空间 O(V)——Union-Find 复习时补。）

## 七、关联题目：图论家族

| 题 | 关系 |
|----|------|
| **399 本题** | 带权图 DFS——"边权连乘" |
| **200 岛屿数量**（⚡ 已做）| 无向图连通分量（DFS/BFS 数块）|
| **207 课程表**（⚡ 已做）| 有向图环检测（DFS/拓扑）|
| **994 腐烂的橘子**（候选）| 多源 BFS 分层扩散 |

**识别信号**："等式关系 + 批量查询 + 传递性（a→b→c 串起来）" → 带权图 DFS/并查集；"变量是字符串" → 用 dict 存图（嵌套 dict 或 defaultdict(list) 均可）。

## 八、一句话记住

> **399 = 等式建带权图（a--v-->b 和 b--1/v-->a），查询=路径边权连乘，缺变量/不连通=-1；DFS 每 query 新建 visited；⚡ 闭合路径边权积恒为 1——隐式处理 a/a，显式 if a==b: return 1 更稳。**