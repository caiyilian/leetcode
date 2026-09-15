# 199. 二叉树的右视图 · 解析

## 题目简述

给定二叉树的根节点 `root`，想象自己站在它的**右侧**，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例：`[1,2,3,null,5,null,4]` → `[1,3,4]`。

## 核心套路：层序遍历 + 每层取最右

**右视图 = 每层最后一个节点**（从左到右看一层，最右边那个就是右侧能看到的）。所以本质是层序遍历（BFS），每层取尾。

## 定稿：deque 快照版（最简洁）

```python
class Solution:
    def rightSideView(self, root):
        from collections import deque
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            for _ in range(len(q)):        # ① len(q) 快照 = 当前层节点数
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(node.val)        # ② for 结束 node = 本层最右 ✅
        return result
```

**两个关键细节**：

1. **`len(q)` 快照**（102 题 BFS 版的知识点）：循环开始时 `len(q)` 是**当前层节点数**，循环中新入队的下一层节点不会被本轮处理——天然分层；
2. **`node.val` 白捡**：`for` 循环走完后 `node` 停留在本层**最后一个出队的节点**——恰好是最右节点，直接收进结果，省掉"先存层再取尾"。

## v1：层队列版（用户初版，思路更直白）

```python
list1 = [[root]]                          # "层的队列"：每个元素 = 一整层
while list1:
    q = list1.pop(0)
    list_layer = []
    for node in q:
        if node.left:  list_layer.append(node.left)
        if node.right: list_layer.append(node.right)
    if not list_layer:
        break
    result.append(list_layer[-1].val)     # 每层最右
    list1.append(list_layer)
```

**特点**：`list1` 存的是"整层节点"，取 `list_layer[-1]` 直白对应"每层最右"。**短板**：`list1.pop(0)` 是 O(层数)（列表头弹出要移动后面所有元素）——改进为 deque 后性能达标。

## 两版对比

| | v1 层队列版 | 定稿 deque 快照版 |
|--|------------|------------------|
| 数据结构 | 层队列（元素=整层） | 节点队列 + 快照分层 |
| 每层取最右 | `list_layer[-1]` | `for` 后 `node`（白捡） |
| pop 开销 | O(层数)（list.pop(0)） | O(1)（deque.popleft） |
| 代码量 | 较长 | 更简洁 |

## 复杂度

- 时间 **O(n)**（每节点恰好一次）；
- 空间 **O(w)**（队列最多存一层，w = 最大层宽；满二叉树 w ≈ n/2）。

## 考点

- BFS 分层三件套（102 层序 → 199 右视图 → 103 锯齿都是它）
- `len(q)` 快照的复用
- deque 的 popleft（list.pop(0) 是 O(n) 的老坑）

## 易错点

1. **for 循环里别用动态 len(q)**：`for _ in range(len(q))` 的 `len(q)` 在**循环开始时求值一次**（快照）——放循环里重算会串层；
2. 空树返回 `[]`；
3. 右视图要**每层都有一个值**（即使那层只有左子树节点——比如 `[1,2,3,4,null,null,null,5]` → `[1,3,4,5]`，层 3 的最右是 5 左边的兄弟……不对，![重要] 层 3 只有 5 一个节点，最右就是 5 ✅）；
4. 取的是"层最后的节点"，不是"最右子树的节点"——BFS 层序天然正确，DFS 想当然会错。