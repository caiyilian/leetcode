# 114. 二叉树展开为链表 · 解析

## 题目简述

给你二叉树的根节点 `root`，将它展开为单链表：展开后的链表与**先序遍历**顺序相同，每个节点 `left = None`、`right` 指向下一个节点。要求**原地修改**（不新建节点，进阶 O(1) 空间）。

## 核心洞察：展开顺序 = 先序遍历

`根 → 左子树 → 右子树`——所以展开的关键是**把右子树"接到"左子树的末尾之后**（先序里左子树走完才轮到右子树）。

## 解法一：v1 收集法（用户第一版，O(n) 空间）

```python
tree_list = []
def fun(root):
    if root:
        tree_list.append(root)          # 前序收集节点引用
        fun(root.left)
        fun(root.right)
        root.left = None
fun(root)
for i in range(len(tree_list)-1):
    tree_list[i].right = tree_list[i+1] # 按先序顺序连 right
```

**正确性**：先序顺序 = 展开顺序；收集引用（非值）→ 原地改指针，不新建节点。**短板**：tree_list O(n) 空间，不满足 O(1) 进阶。

## 解法二：v2 原地插接（用户第二版，O(n²)）

```python
while root:
    if root.left:
        max_right = find_max_right(root.left)[0]   # 左子树"展开后的链尾"
        max_right.right = root.right               # 原右子树嫁接到链尾
        root.right = root.left                     # 左子树搬到右边
        root.left = None
    root = root.right
```

**用户设计亮点**：找"左子树**展开后**的链尾"（= 前序最后一个节点），而不是标准解法的"right 链尾"——对未展开的树更通用、更好理解。

**两个短板（实测验证）**：
1. `find_max_right` 递归遍历**整棵**左子树 → 每轮 O(子树大小)，链状树总 **O(n²)**（左链 600：慢 440 倍）；
2. 递归深度 = 树高，左链 >1000 **栈溢出**（力扣约束 ≤2000 有风险）。

## 解法三：标准版（O(n)/O(1)，进阶达标）

```python
class Solution:
    def flatten(self, root):
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:          # 沿 right 链找尾（O(高度)）
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
```

**为什么沿 right 链就够了（O(n) 的关键）**：处理某节点时，它的左子树**已经被前面几轮部分展开**——左子树的 right 链恰好就是"已展开部分的末尾"。所以找尾只需 O(左子树高度)，不用遍历整棵。

## 三版对比

| | v1 收集法 | v2 找尾法（用户） | 标准版 |
|--|----------|------------------|--------|
| 时间 | O(n) | O(n²) | **O(n)** |
| 空间 | O(n) | O(1) + 递归栈 O(h) | **O(1)** |
| 风险 | 无 | 深树栈溢出 | 无 |
| 可读性 | 最直观 | 思路好但实现绕 | 简洁 |

## 复杂度

- v1：O(n) / O(n)；
- v2：O(n²) / O(1)（递归栈 O(h)）；
- 标准版：**O(n) / O(1)**（满足进阶）。

## 考点

- 原地修改 + 先序顺序（顺序是正确性钥匙）
- **O(1) 空间的树操作**（Morris 家族的思想萌芽——"临时改指针、用完恢复"的简化版）
- "引用 vs 局部变量移动"（ori = root 不必要的认知）
- 复杂度演进思维（v1 正确 → v2 优化 → 标准 O(n)）

## 易错点

1. **顺序**：先"接右子树到左链尾"再"左搬右"（反过来会丢右子树）；
2. 找尾必须用**当前时刻**的左子树（前面几轮已部分展开）；
3. 每个节点 left 都要置 None（special judge 检查）；
4. `flatten` 无返回值（原地修改，模板调用 `Solution().flatten(root)`）；
5. 空树/单节点直接返回（while 天然处理）。