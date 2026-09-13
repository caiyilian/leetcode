# 48. 旋转图像 · 解析

## 题目简述

给定一个 `n × n` 的二维矩阵，原地将它顺时针旋转 90 度。**要求：不能分配另一个矩阵**（必须 in-place）。

示例：`[[1,2,3],[4,5,6],[7,8,9]]` → `[[7,4,1],[8,5,2],[9,6,3]]`。

## 核心：旋转的坐标公式

顺时针旋转 90° 的坐标映射：

```
(r, c) → (c, n-1-r)
```

即：第 r 行第 c 列的元素，旋转后到第 c 行第 n-1-r 列。所有解法都是这个公式的不同实现：

| 解法 | 实现方式 |
|------|---------|
| 转置 + 水平翻转 | 先 `(r,c)↔(c,r)` 对角交换，再每行左右翻转（公式等价变换） |
| **逐层四元素轮换**（用户解法） | 一层一圈，每次把一个 4 元素环转 90° |

## 用户解法：逐层旋转 + 四元素轮换

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        layer = 0
        for _ in range(n//2):                    # 逐层（外圈→内圈）
            for i in range(n-1-2*layer):          # 每层每边要轮换的位置数
                # 三次交换实现四元素环：left → top → right → bottom → left
                matrix[layer][i+layer], matrix[i+layer][n-1-layer] = \
                    matrix[i+layer][n-1-layer], matrix[layer][i+layer]           # ① top <-> right
                matrix[layer][i+layer], matrix[n-1-layer][n-1-i-layer] = \
                    matrix[n-1-layer][n-1-i-layer], matrix[layer][i+layer]       # ② top <-> bottom
                matrix[layer][i+layer], matrix[n-1-i-layer][layer] = \
                    matrix[n-1-i-layer][layer], matrix[layer][i+layer]           # ③ top <-> left
            layer += 1
```

### 四个位置的坐标（每层每边第 i 格）

| 位置 | 坐标 | 旋转后去向 |
|------|------|-----------|
| 上边第 i 格 `top` | `(layer, i+layer)` | 右边第 i 格 |
| 右边第 i 格 `right` | `(i+layer, n-1-layer)` | 下边第 i 格 |
| 下边第 i 格 `bottom` | `(n-1-layer, n-1-i-layer)` | 左边第 i 格 |
| 左边第 i 格 `left` | `(n-1-i-layer, layer)` | 上边第 i 格 |

环的走向：`left → top → right → bottom → left`（顺时针）。

### 三次交换为什么能转环

用 `temp` 保存 top 的话：

```
temp = top; top = left; left = bottom; bottom = right; right = temp
```

用户用**三次两两交换**代替临时变量：
1. `top ↔ right`：right 的旧值备份到 top；
2. `top ↔ bottom`：bottom 的旧值到 top（原 right 已被"赶"到 top？不——第 1 步后 top = 旧 right，第 2 步把 top 的旧 right 换给 bottom……）

准确推演：
- 初始 `top=T, right=R, bottom=B, left=L`
- ① top↔right → `top=R, right=T`
- ② top↔bottom → `top=B, bottom=R`（bottom 取走 top 现存的 R）
- ③ top↔left → `top=L, left=B`

最终：`top=L ✅, right=T ✅, bottom=R ✅, left=B ✅`——正好顺时针转了一圈。**三次交换 = 先留一个"临时口袋"在 top，把环依次倒进去**。

## 复杂度

- 时间 **O(n²)**：n² 个元素，每个恰好参与一次环交换；
- 空间 **O(1)**：三个标量变量，无临时矩阵。

## 考点

- 旋转公式 `(r,c)→(c, n-1-r)` 及其等价变换（转置÷翻转）
- 四元素环交换（逐层旋转的通用技巧）
- 原地操作（不能分配第二个矩阵——题面硬性要求）
- 边界：n=1 不旋转（`n//2=0` 循环不执行）；每层每边位置数 `n-1-2*layer`
- 与 54 题的关联：54 是"读出"螺旋路径，48 是"写入"旋转位置，都是矩阵坐标变换题

## 面试拓展

面试官常追问**转置 + 翻转解法**（更易口述）：

```python
# ① 转置：matrix[i][j] <-> matrix[j][i]（沿主对角线）
# ② 每行水平翻转：matrix[i][j] <-> matrix[i][n-1-j]
```

两种解法都 O(n²)/O(1)。手写面试题建议用"转置+翻转"（代码短、不易写错），理解层面用"四元素轮换"（更本质）。