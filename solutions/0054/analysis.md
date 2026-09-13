# 54. 螺旋矩阵 · 解析

## 题目简述

给你一个 `m 行 n 列` 的矩阵，按照**螺旋顺序**（顺时针：右 → 下 → 左 → 上，层层向内）返回矩阵中的所有元素。

示例：`[[1,2,3],[4,5,6],[7,8,9]]` → `[1,2,3,6,9,8,7,4,5]`。

## 两种主流思路

### 思路 A：方向轮转 + 边界收缩（用户解法 ✅）

**核心**：维护四个边界 `dir_max = [right, bottom, left, top]`（初始 `[n, m, 0, 0]`），按 `右→下→左→上` 轮转行走；每走完一条边，对应的边界向内收缩一格。**走过的行/列就不会再被访问**，因此不需要 visited 标记。

```python
dir_max = [n, m, 0, 0]   # right, bottom, left, top 四个边界
use_dir_index = 0        # 0右 1下 2左 3上
while True:
    if use_dir_index == 0:      # 向右
        if j < dir_max[0] - 1:  # 没到右边界 → 继续走
            j += 1; result.append(matrix[i][j]); count += 1
        else:                   # 到边界 → 上边界下移一行，转向
            dir_max[-1] += 1    # 注意：use_dir_index=0 时 -1 → up 边界（负索引技巧）
            use_dir_index = (use_dir_index + 1) % 4
    # ... 同理：下/左/上
    if count == m * n: break
```

**边界对应关系**（精华，务必理解）：

| 走完的方向 | 收缩的边界 | 代码 |
|-----------|-----------|------|
| 向右（顶行走完） | **上边界** top +1 | `dir_max[-1] += 1` |
| 向下（右列走完） | **右边界** right -1 | `dir_max[0] -= 1` |
| 向左（底行走完） | **下边界** bottom -1 | `dir_max[1] -= 1` |
| 向上（左列走完） | **左边界** left +1 | `dir_max[2] += 1` |

**为什么收缩的是"对侧"边界**：向右走完的是最上面一行，接下来往下的起点应该是第二行，所以收缩的是 top 而不是 right——同理类推。这个"走哪条边、缩哪个界"的对应关系是本题最容易写错的地方。

### 思路 B：边界逐层剥（标准写法，等价的另一种形态）

```python
top, bottom, left, right = 0, m-1, 0, n-1
while top <= bottom and left <= right:
    for j in range(left, right+1): result.append(matrix[top][j])   # →
    top += 1
    for i in range(top, bottom+1): result.append(matrix[i][right]) # ↓
    right -= 1
    if top <= bottom:
        for j in range(right, left-1, -1): result.append(matrix[bottom][j])  # ←
        bottom -= 1
    if left <= right:
        for i in range(bottom, top-1, -1): result.append(matrix[i][left])    # ↑
        left += 1
```

两种思路本质相同（都是"边界收缩"），思路 A 是"走一步判一次界"，思路 B 是"一段路走完再缩界"。归档的 `solution_readable.py` 是思路 A 的可读化版本。

## 复杂度

- 时间 **O(m·n)**：每个元素恰好访问一次，理论下限；
- 空间 **O(1) 额外**：思路 A 无 visited 数组、无方向数组，只读不写矩阵——**同时满足进阶要求**。

## 考点

- 螺旋模拟（面试高频手写题）
- 边界收缩的对应关系（走哪缩哪）
- 无 visited 标记的 O(1) 空间技巧
- 终止条件（count == m×n）
- 单行/单列/单元素的边界处理（本题通过"先走再判界"天然规避）

## 踩坑提醒

- **不要想着转置或四角分割**：螺旋会重复访问边界元素，直接用"收缩边界"最干净；
- 思路 A 的 `dir_max[use_dir_index-1]` 在 direction=0 时是负索引 `dir_max[-1]`，指到 up 边界——语义正确但隐晦，复习时用注释标注；
- 空矩阵（m=0 或 n=0）题目约束不会出现，但 `matrix[0][0]` 初始化依赖非空。