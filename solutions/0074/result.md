# 74. 搜索二维矩阵 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 74. 搜索二维矩阵（Search a 2D Matrix）· 中等（二分查找分类第 2 题） |
| 链接 | https://leetcode.cn/problems/search-a-2d-matrix/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 133/133 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.2 MB |

## 解法（用户按 35 模板换皮：展平映射二分）

```python
class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            middle = (left + right) // 2
            i, j = middle // n, middle % n      # ★ 一维下标 → 二维坐标
            if matrix[i][j] >= target:
                right = middle
            else:
                left = middle + 1
        return matrix[left // n][left % n] == target
```

**核心洞察**：题设"每行行首 > 上一行行尾" → 矩阵按行展开是严格升序一维数组 → 无需真正拍平，下标映射 `row = mid//n, col = mid%n` 直接套 35 模板。

## ⚠️ 本次失败记录（力扣 749716293 Restrictions Failed）

**失败版**：`return matrix[left // m][left % m] == target` —— 写了**行数 m**，应为**列数 n**。

- 展平映射除的永远是**列数 n**（每行宽度）：`mid//n` 得行号、`mid%n` 得列号；
- 方阵（m==n）时结果碰巧相同 → 本地测试难发现；非方阵（3×4）错位 → 某些 mid 越界 → **Restrictions Failed**；
- 9:15 力扣第一次提交失败，第二次修正后 Accepted。

**记忆锚点：`mid // n, mid % n` 里的 n 是"每行几个元素"（列数）——m、n 连续写最容易顺手用反，非方阵用例保平安。**

## 验证

- 对拍 **2 万组随机升序矩阵 vs 拍平 in 检查 0 不一致**；
- 官方样例：3→True、13→False；边界 `[[1]]`+1→True、`[[1]]`+0→False。

## 复杂度

- 时间 **O(log(m·n))**；空间 **O(1)**。