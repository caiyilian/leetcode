# 98. 验证二叉搜索树 · 解析

## 题目简述

给你一个二叉树的根节点 `root`，判断其是否是一个**有效的二叉搜索树**（BST）。

BST 定义（严格版）：
- 节点的**左子树**只包含**小于**当前节点的数；
- 节点的**右子树**只包含**大于**当前节点的数；
- 左右子树也必须是 BST。

> 注意"小于/大于"是**严格**的——`[2,2,2]` 不是 BST。

## 核心套路一：中序遍历递增（用户定稿，最简洁）

**BST 的性质**：中序遍历结果是**严格递增**序列（左 < 中 < 右，中序正好按这个顺序访问）。

所以：中序遍历一遍，边走边检查"当前值 > 上一个值"，一旦出现 `<=` 就是非 BST。

```python
class Solution:
    def isValidBST(self, root):
        last_list = [float('-inf')]          # 上一个中序值（哨兵）
        def fun(tree_root):
            if tree_root:
                left_bool = fun(tree_root.left)
                if tree_root.val > last_list[0]:
                    last_list[0] = tree_root.val
                else:
                    return False
                if left_bool is False:
                    return False
                right_bool = fun(tree_root.right)
                return right_bool
            return True
        return fun(root)
```

**为什么它能抓"子树边界"陷阱**（`[5,4,6,null,null,3,7]`）：

```
       5
      / \
     4   6
        / \
       3   7     ← 3 在 6 的右子树里，但它 < 5！

中序序列：4, 5, 3, 6, 7  → 5 > 3？不！→ False ✅
```

只检查"父 vs 子"的简单递归（`左<根<右` 只看局部）会漏掉这种跨层违反；**中序递增法把全局顺序铺开，任何违反都被"相邻比较"抓到**——这就是它比"局部递归"强的根本原因。

## 核心套路二：带区间递归（另一标准解法，面试可补充）

```python
def isValidBST(root):
    def helper(node, lo, hi):
        if not node:
            return True
        if not (lo < node.val < hi):
            return False
        return helper(node.left, lo, node.val) and helper(node.right, node.val, hi)
    return helper(root, float('-inf'), float('inf'))
```

思路：每个节点携带允许区间 `(lo, hi)`——左子树收窄上限、右子树收窄下限。违反区间即 False。**同是 O(n)/O(h)，写法对称，面试常被要求两种都讲**。

## 两法对比

| | 中序递增法（用户版） | 区间递归法 |
|--|--------------------|-----------|
| 思想 | 性质：中序严格递增 | 定义：携带 (lo, hi) 区间 |
| 代码 | 需维护 last 状态 | 无状态，纯参数 |
| 直观性 | 依赖"BST ⇔ 中序递增"性质 | 直接对应定义 |
| 通用性 | 也可改造成"第 k 小"（230 题） | 变体少 |

## 复杂度

- 时间 **O(n)**（每节点一次）；空间 **O(h)** 递归栈（最坏 O(n)）。

## 考点

- BST ⇔ 中序递增（性质应用）
- 全局状态（last）与递归的配合（543 学过的"列表绕开 nonlocal"复用）
- 严格递增 vs 非严格（重复值）
- 子树边界陷阱（跨层违反）

## 易错点

1. **初始值**：`last` 必须用 `float('-inf')`（任何 int 都比它大）——用 `0` 或 `None` 处理负值树会出错；
2. **严格性**：`val > last` 更新 / `val <= last` 判错——写成 `>=`/`<` 会把合法 BST 判错；
3. 只比较"父 vs 子"的局部递归会漏跨层违反（必须中序或区间法）；
4. 空树 / 单节点 → True；
5. Python int 不可变 → 用 `last_list = [float('-inf')]` 存状态（嵌套函数不用 nonlocal 的惯用技巧）。