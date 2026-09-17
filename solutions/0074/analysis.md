# 74. 搜索二维矩阵 · 解析

## 题目简述

`m×n` 矩阵：每行升序，**每行行首 > 上一行行尾**。判断 target 是否存在。

## 核心套路：展平映射 + 35 模板一套（识别等价结构）

**题设条件的意义**：保证矩阵按行展开是**严格升序的一维数组**——

```
[[1,3,5,7],        →  [1,3,5,7,10,11,16,20,23,30,34,60]  严格升序
 [10,11,16,20],
 [23,30,34,60]]
```

所以"搜索二维矩阵" = "在有序数组里二分"（35 的活），**不需要真正拍平数组**（O(mn) 空间浪费），用下标映射：

```
一维下标 mid → 二维坐标：
    row = mid // n     （n = 列数：每行有 n 个元素）
    col = mid % n
    matrix[row][col]  ← 等价于 "nums[mid]"
```

```python
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            middle = (left + right) // 2
            i, j = middle // n, middle % n      # ★ 映射
            if matrix[i][j] >= target:
                right = middle                  # 35 模板：lower_bound
            else:
                left = middle + 1
        return matrix[left // n][left % n] == target   # 存在性检查（35 返回位置，本题要 bool）
```

**为什么最后还要 `== target`**：35 返回"插入位置"；本题要"是否存在"——二分收敛后 `left` 是"第一个 ≥ target 的位置"，**该位置的值恰好等于 target 才是 True**（注意：left 可能落在 m*n 边界外？——闭区间写法 right 初始 m*n-1，left 最多到 m*n-1，不会越界）。

## ⚠️ 力扣失败实录：下标映射 n/m 搞混（Restrictions Failed）

**失败提交**（749716293）：

```python
return matrix[left // m][left % m] == target    # ❌ 用 m（行数）
```

**正确**：

```python
return matrix[left // n][left % n] == target    # ✅ 用 n（列数）
```

**为什么错**：展平"每行有 n 个元素"——`mid // n` 是"走了几整行"（行号），`mid % n` 是"本行第几个"（列号）。写成 `//m` `%m`：
- 非方阵（3×4）时映射错位 → 访问到错误格子（如 mid=5 → (1,2) 而非 (1,1)）；
- 某些 mid 算出 row ≥ m → **越界** → 力扣报 "Restrictions Failed"（违反限制）；
- **方阵（m==n）时 `//m == //n` 碰巧正确** → 本地方阵测试发现不了。

**教训**：
1. **`mid//n, mid%n` 的 n 永远是列数**（每行宽度），和 m 无关；
2. **测试用非方阵**（如 3×4）专门验证映射，比全方阵更能暴露这类错；
3. "Restrictions Failed" 这类报错 ≈ 越界/非法访问信号，优先查下标计算。

## 复杂度

- 时间 **O(log(m·n))**——比"先找行再找列"（O(log m + log n)）同量级但代码更少更不易错；
- 空间 **O(1)**。

## 考点

- **等价结构识别**（矩阵 → 展平一维有序）
- 一维下标 ↔ 二维坐标映射
- 35 二分模板迁移（lower_bound 语义）
- m/n 变量混淆（本此失败点）

## 易错点

1. **`mid//m, mid%m` 用错除数**（本此教训）；
2. 返回 `left` 不检查 `== target` → tail>所有数时错判 True（left 落在边界外/等于尾后）；
3. 忘 `middle+1`（35 教训复读）；
4. `matrix[i][j] >= target` 用 `>` → 相等元素时收敛位置错（本题无重复但 lose_bound 语义要对）。

## 关联题

- **240 搜索二维矩阵 II**（每行每列单独升序——不能展平，用右上角阶梯法，用户已 AC）；
- 35（模板母题）、34（首尾位置）、33（旋转数组）、153（旋转最小值）、4（中位数）。