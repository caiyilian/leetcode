# 101. 对称二叉树 · 解析

## 题目简述

给你一个二叉树的根节点 `root`，检查它是否**轴对称**。

示例：`[1,2,2,3,4,4,3]` → true；`[1,2,2,None,3,None,3]` → false（3 的位置不对称）。

## ⚡ 重点标记：空树是 True

**空树天然对称** → `if not root: return True`。这行防护同时防止 `root.left` 对 None 访问崩溃。

## 核心套路：判断"互为镜像"（交叉递归）

对称 ≠ 左右子树相等，而是**左右子树互为镜像**：

```
镜像的定义：
  tree1 的左子树  == tree2 的右子树（镜像位置）
  tree1 的右子树  == tree2 的左子树（镜像位置）
```

```python
class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.fun(root.left, root.right)

    def fun(self, tree1, tree2):
        if tree1 and tree2:                      # 两个都非空 → 比较
            if tree1.val != tree2.val:
                return False
            return (self.fun(tree1.left, tree2.right)      # 交叉！
                    and self.fun(tree1.right, tree2.left)) # 交叉！
        return tree1 is tree2                    # 都 None → True；一个 None → False
```

## 用户写法的三个亮点

1. **交叉递归方向正确**：`left vs right` + `right vs left`——如果是 `left vs left` + `right vs right` 那就变成判断"相等"而不是"对称"（写反是本题头号错误）；用户版方向正确；
2. **`tree1 is tree2` 一行双边界**：都 None → True（`None is None`）；一个 None → False（`None is 对象`）——不用两个 if，Pythonic；
3. 空树防护（归档时补）：`if not root: return True`。

## 与 226 翻转二叉树的关系（镜像家族）

| 题 | 操作 | 方向 |
|----|------|------|
| 226 翻转二叉树 | **构造**镜像（交换左右） | 造 |
| 101 对称二叉树 | **判断**是否互为镜像（交叉比较） | 判 |

一对反向操作，都是"镜像"这一个概念的两种问法。101 也可以先翻转左子树再比较与右子树是否相等（`invert(left) == right`）——但直接交叉递归更省。

## 复杂度

- 时间 **O(n)**：每个节点最多访问一次；
- 空间 **O(h)** 递归栈（最坏 O(n) 斜树）。

## 考点

- 镜像判断（交叉递归）
- `is` 与 `==` 的区别（`is` 比身份，这里用来判 None 状态）
- 空边界（空树 True）
- 与 226 的镜像家族关系；迭代版（栈/队列成对入队）可在面试中补充

## 易错点

1. **递归方向写反**（比较了左 vs 左——那是相等不是对称）；
2. 空树不防护直接 `root.left` 崩溃；
3. `and` 短路：左边 False 时右边不再递归（正确但不影响结果）；
4. 值相同但结构不对称（如 `[1,2,2,None,3,None,3]`）要返回 False——结构也要镜像。