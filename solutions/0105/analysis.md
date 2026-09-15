# 105. 从前序与中序遍历序列构造二叉树 · 解析

## 题目简述

给定两个整数数组 `preorder`（前序）和 `inorder`（中序），构造并返回二叉树。两数组内**无重复元素**（关键前提——索引映射才能唯一）。

## 核心套路：前序定根 + 中序分界（递归分治）

**本质一句话**：

> 前序给"根是谁"（`preorder` 第一个就是根），中序给"根的左右各有几个"（根在中序的位置把序列劈成左/右）。

```
前序：  [根 | 左子树全体 | 右子树全体]
中序：  [左子树全体 | 根 | 右子树全体]
```

对角看：前序的根 = 中序的中间那个；中序里根左边的个数 = 左子树大小——用它把前序的"左全体/右全体"精确切出来，递归。

## 四边界推导（用户版，最不易错的写法）

```python
index_dict = {i: v for v, i in enumerate(inorder)}   # 值 → 中序索引
left1, right1 = 0, length-1    # 前序范围
left2, right2 = 0, length-1    # 中序范围

def fun(left1, right1, left2, right2):
    if left1 > right1:
        return None
    root = TreeNode(preorder[left1])        # ① 前序第一个 = 根
    index = index_dict[preorder[left1]]     # ② 根在中序的位置
    left_count = index - left2              # ③ 关键翻译：中序位置差 = 左子树大小
    root.left  = fun(left1+1,           left1+left_count,   left2,    index-1)
    root.right = fun(left1+left_count+1, right1,            index+1,  right2)
    return root
```

**为什么 `left_count = index - left2`**：中序里 `[left2, index)` 之间的元素都是根的左子树——数量 = `index - left2`。前序里根的后面正好连续这么多元素属于左子树 → `[left1+1, left1+left_count]`。

**为什么基线只查 `left1 > right1`**：两个序描述的是同一棵子树，范围长度同步变化——前序空了中序必空，查一个即可（这也是代码简洁的来源）。

## 为什么不用每次都 inorder.index()

`index_dict` 预哈希让"找根在中序的位置"变成 O(1)。若每次 `inorder.index(root.val)` 是 O(n)——总复杂度退化为 **O(n²)**。预计算是 105 的标准优化（面试会问"如何从 O(n²) 变 O(n)"）。

## 复杂度

- 时间 **O(n)**（每节点一次 + hash O(1)）；
- 空间 **O(n)**（index_dict）+ **O(h)** 递归栈（最坏 O(n) 斜树）。

## 考点

- 两种遍历的"对角互补"（根的位置互相确定）
- **序列范围递归**（四边界法 vs 切片法：切片每次 O(k) 拷贝 → O(n²)，边界法 O(1) 递进）
- hash 预计算优化
- 系列题母题：**106 中序+后序**（后序第一个是右子树的根，边界反过来）、889 前序+后序——105 会了，106 只改 2 行

## 易错点

1. **前序里 `left1+1` 是左子树起点**（不是 left1——根已经在 left1 了）；
2. `left_count = index - left2` 用**中序左边界**减，不是 0（递归到子树时 left2 会变）；
3. 右子树前序起点 = `left1 + left_count + 1`（+1 别忘了，那是根的左子树全体之后）；
4. 依赖"无重复元素"（有重复则中序定位不唯一）；
5. 空数组（`left1 > right1`）返回 None。

## 关联题

- 94/98/108/230：中序遍历三兄弟（读写两侧）
- **106 从中序与后序**：同模板，把"前序取根"换成"后序取根"（后序从尾部取），左右边界调整即可；
- 889 根据前序和后序构造二叉树：更复杂的变体（无中序分界，需额外推断）。