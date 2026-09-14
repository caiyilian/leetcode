# 94. 二叉树的中序遍历 · 解析

## 题目简述

给定二叉树的根节点 `root`，返回它的中序遍历（左 → 根 → 右）。

## 核心套路：递归（最简单）与迭代（无栈溢出风险）

### 解法一：递归版（用户定稿）

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.scan_tree(root, result)
        return result

    def scan_tree(self, root, result):
        if root:
            self.scan_tree(root.left, result)   # ① 左
            result.append(root.val)             # ② 根
            self.scan_tree(root.right, result)  # ③ 右
```

3 行核心逻辑 = 中序定义本身。**用一个 result 列表贯穿**（而非每层新建再拼接——避免 O(n²) 的重复拷贝）。

### 解法二：迭代版（显式栈模拟）

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, cur = [], [], root
        while stack or cur:
            while cur:                  # ① 一路向左，路径节点全压栈
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()           # ② 弹出 = 访问（最左无左孩子的节点）
            res.append(cur.val)
            cur = cur.right             # ③ 转向右子树（下一轮继续压它的左链）
        return res
```

**为什么这样写**：递归版依赖"系统栈"保存还没处理的祖先；迭代版**把系统栈换成显式栈**，一步步还原：

```
递归版顺序：访问左子树（整棵压栈）→ 访问自身 → 访问右子树
迭代版模拟：① 压栈左链（对应"调用左子树"） ② 弹栈访问（对应"访问自身"） ③ 转右子树（对应"调用右子树"）
```

## 复杂度与空间口径

| 版本 | 时间 | 额外空间 | 适用 |
|------|------|---------|------|
| 递归版 | O(n) | O(h) 系统栈 | 最简洁，面试首选 |
| 迭代版 | O(n) | O(h) 显式栈 | 深树安全（无递归上限）、面试官要求"不用递归"时 |

- **输出列表 O(n) 不算额外空间**（标准口径：只统计计算过程中的额外开销）；
- 递归栈 = 系统调用栈（Python 默认上限 ~1000 层），**斜树（深度 = n）时递归版可能 RecursionError，迭代版不会**——这是迭代版最实际的优点。

## 考点

- **二叉树三种遍历**（前/中/后序）——树的基石，104/226/543 等都依赖遍历
- 递归 → 迭代的转换思路（显式栈模拟系统栈）
- 一个 result 贯穿 vs 每层新建列表（后者 O(n²) 拷贝陷阱）
- 空间口径：输出 vs 额外空间

## 易错点

1. 递归版每层 `return scan(left) + [root.val] + scan(right)` 会反复拷贝列表（O(n²)）——**用共享 result 列表**；
2. 迭代版"转向右子树"后外层循环会继续压它的左链（不能漏 `cur = cur.right`，否则死循环）；
3. `[]` 空树返回 `[]`（不是 None）；
4. 深树：递归版有栈溢出风险（可用迭代版兜底）。