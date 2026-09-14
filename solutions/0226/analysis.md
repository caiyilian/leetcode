# 226. 翻转二叉树 · 解析

## 题目简述

给定一棵二叉树的根节点 `root`，翻转这棵二叉树（每个节点的左右子树交换），并返回根节点。

示例：`[4,2,7,1,3,6,9]` → `[4,7,2,9,6,3,1]`。

## 核心套路：递归（和 104 同款分治模式）

**翻转整棵树 = 翻转左子树 + 翻转右子树 + 交换左右**。递归三步走：

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
```

## ⚡ 隐藏考点：元组赋值"右边先求值"

用户版的关键一行：

```python
root.left, root.right = self.fun(root.right), self.fun(root.left)
```

**Python 语义**：赋值号**右边整体先求值**（两个 `fun(...)` 递归调用依次执行完毕），再按位置赋给左边。

```
执行顺序：
① fun(root.right)  → 返回翻转后的右子树（此时 root 还没交换）
② fun(root.left)   → 返回翻转后的左子树
③ root.left = ①的结果（原右子树翻转版）
④ root.right = ②的结果（原左子树翻转版）
```

**"先递归翻转、再交换"一步完成**。如果手滑写成：

```python
root.left, root.right = root.right, root.left        # 先交换
self.invertTree(root.left)                            # 再递归——子树已经被换位，会翻两次抵消！
self.invertTree(root.right)
```

得到的结果是**原树**（翻转两次 = 原样）——这是 226 最经典的错误写法，很多面试者栽在这。**用元组赋值一行，天然避免**。

## 复杂度

- 时间 **O(n)**：每个节点恰好访问一次；
- 空间 **O(h)** 递归栈（最坏 O(n) 斜树）。

## 考点

- 树的分治递归模式（104 → 226 → 101/543 一脉相承）
- Python 元组赋值的求值顺序（隐藏考点）
- 原地修改 vs 新建（本题原地翻转，不改节点值）

## 易错点

1. **先交换后递归 = 翻两次抵消**（上面分析的经典陷阱）；
2. 空节点返回 None（`if not root` 基线）；
3. 原地翻转时要保证递归拿到的是"交换前"的子树——元组赋值最稳。

## 关联题

- 101 对称二叉树：判断镜像（递归比较左右），和本题"构造镜像"是反方向的操作；
- 104 最大深度：同款分治递归模板。