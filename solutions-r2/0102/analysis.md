# 102. 二叉树的层序遍历 · 解析（二刷）

## 一、核心思路：BFS 队列 + 按层快照

层序 = 一层一层从左到右输出。BFS 天然逐层推进，关键在**怎么知道一层在哪结束**——`for _ in range(len(q))` 按层快照：

```
q = [3]                   第0层：len=1 → 弹 3，入 9,20
q = [9, 20]               第1层：len=2 → 弹 9,20，入 15,7
q = [15, 7]               第2层：len=2 → 弹 15,7
```

**`len(q)` 在 for 开始时一次性取值** = 当前层节点数；处理完这层，队列恰好只剩下一层的新节点。一层一个子列表，天然分组。

## 二、代码骨架

```python
if not root:
    return []                     # 空树守卫
result = []
q = deque([root])
while q:
    now = []
    for _ in range(len(q)):       # ★ 按层快照
        node = q.popleft()
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        now.append(node.val)
    result.append(now)
return result
```

- **deque 而不是 list**：`popleft()` O(1)，list 的 `pop(0)` 是 O(n)；
- 只压非空孩子（`if node.left:`），队列不会出现 None。

## 三、另一种解法：DFS + dep 分组（一刷自创 = 官方解法二）

```python
def dfs(node, dep):
    if not node:
        return
    if len(res) == dep:     # 第一次到这个深度，开新层
        res.append([])
    res[dep].append(node.val)
    dfs(node.left, dep + 1)
    dfs(node.right, dep + 1)
```

**层序本质 = 按深度分组**（同一 dep 的节点进同一层）。DFS 也能做，只是顺序是"先左到底再右"——只要 dep 相同就归一组，结果一样。

## 四、复杂度

- 时间：O(n)——两种解法都每个节点访问一次
- 空间：BFS O(n)（队列最宽一层）；DFS O(h)（递归栈，一般更省）

## 五、一刷 vs 二刷：同一题两种解法

| | 一刷（9-14） | 二刷（10-24） |
|---|---|---|
| 解法 | DFS + dep 分组（官方解法二） | BFS 按层快照（官方解法一） |
| 结果 | 0ms/100% | 0ms/19.8MB 一次 AC |

**两种官方法都会了**——面试灵活度直接拉满。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| BFS + 按层快照 | 199 二叉树的右视图（每层最后一个）、103 锯齿形遍历（奇数层反转） |
| BFS 通用 | 二叉树的序列化 297（空节点也入队）、对称二叉树 101（两两入队） |
| DFS dep 分组 | 104 最大深度（dep 传参版）、437 路径总和（回溯） |

## 七、一句话记住

> **层序遍历 = BFS + 按层快照：`for _ in range(len(q))` 先取长度再弹一层，一层一个子列表；DFS 也行——层序本质是按 dep 分组。**