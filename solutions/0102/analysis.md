# 102. 二叉树的层序遍历 · 解析

## 题目简述

给你二叉树的根节点 `root`，返回其节点值的**层序遍历**（逐层从左到右访问，同一层节点放在同一个子列表）。

示例：`[3,9,20,null,null,15,7]` → `[[3],[9,20],[15,7]]`。

## 核心洞察：层序的本质是"分组"，不是"BFS"

大多数人想到层序 = BFS 队列。但用户的解法证明了更本质的认知：

> **层序 = 按深度分组**。只要每个节点知道自己在第几层，无论用什么顺序遍历，归档后输出都是层序。

## 解法一：DFS + 深度分组（用户定稿，力扣官方解法二）

```python
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        self.fun(root, result)
        return result

    def fun(self, root, result, dep=1):
        if root:
            if len(result) < dep:
                result.append([])        # 遇到更深的层，先建空列表
            result[dep - 1].append(root.val)   # 按深度归档
            self.fun(root.left, result, dep + 1)
            self.fun(root.right, result, dep + 1)
```

**为什么正确**：先序遍历的访问顺序（一路左到底再回头）不影响"节点属于第几层"——`dep` 是绝对信息，`result[dep-1]` 归档保证每层的成员完全正确。

**两个细节**：
- `len(result) < dep`：第一次到达第 dep 层时建空列表（也可以初始化 `result = [[]]`，但 `[]` 更干净，fun 会自动建层）；
- 递归的 `and` 顺序无关：左右子树最终都归档到正确层。

## 解法二：BFS 队列（标准版，"层序遍历"的字面实现）

```python
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):      # 关键：len(q) 快照 = 当前层节点数
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
```

**关键**：`for _ in range(len(q))`——`len(q)` 是**循环开始时快照**（当前层节点数），循环中新入队的下一层节点不会被本轮处理。这是 BFS 分层输出的灵魂。

## 两版对比

| | DFS + dep 版 | BFS 队列版 |
|--|-------------|-----------|
| 空间 | O(h) 递归栈 | O(w) 队列（w = 最大层宽） |
| 满二叉树（h=20） | ✅ 栈仅 20 层 | ❌ 队列存 ~50 万节点 |
| 斜树（n 个） | ❌ 栈 O(n) | ✅ 队列 O(1) |
| 代码风格 | 递归 7 行 | 迭代 10 行 |
| 面试印象 | 解法二（进阶思路） | 解法一（标准答案） |

**结论**：不是"标准 vs 笨"，是"两种遍历思路"——用户版在宽树上反而更优，面试时能讲出"DFS 也能层序"是加分项。

## 复杂度

- 时间 **O(n)**（每节点访问一次）；
- 空间：DFS 版 O(h)、BFS 版 O(w)。

## 考点

- 层序的本质（按深度分组）
- DFS 带深度参数（104 的 deep 版在此复现）
- BFS 分层快照（`len(q)` 在循环前取值）
- deque 的 popleft O(1)（queue.pop(0) 是 O(n)，树工具 build_tree 也用过这个坑）

## 易错点

1. BFS 忘记快照 `len(q)`（写成 `for _ in range(len(q))` 每轮重算会死循环或串层）；
2. DFS 版 `result[dep-1]` 索引越界（必须先 `len(result) < dep` 建层）；
3. 空树返回 `[]`（不是 `[[]]`）；
4. `queue.pop(0)` 是 O(n)（用 deque）。