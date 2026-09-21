# 85. 最大矩形 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 85. 最大矩形（Maximal Rectangle）· **困难**（v2 新增题 · 单调栈二维扩展） |
| 链接 | https://leetcode.cn/problems/maximal-rectangle/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-21 |
| 最终提交 | ✅ **ACCEPTED - 76/76 用例通过**（leetgo 复提交） |
| 运行时间 | 47 ms |
| 内存 | 24.4 MB |

## 解法（用户逐行转柱状图 + 单调栈，标准）

```python
class Solution:
    def maximalRectangle(self, matrix):
        def largestRectangleArea(heights):          # 84 单调栈（左右哨兵）
            heights = [0] + heights + [0]
            stack = [0, 1]
            area = 0
            for i in range(2, len(heights)):
                while heights[i] < heights[stack[-1]]:
                    mid = stack.pop()
                    w = i - stack[-1] - 1
                    h = heights[mid]
                    area = max(area, h * w)
                stack.append(i)
            return area

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        area = 0
        for i in range(m):                          # 逐行累加柱高
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            area = max(largestRectangleArea(heights), area)
        return area
```

## 核心：85 = 84 的二维扩展

1. **逐行累加"柱高"**：`heights[j]` 记录第 j 列从当前行往上连续 '1' 的高度（遇 '0' 清零）；
2. **每行转成 84 柱状图最大矩形**：单调栈求当前 heights 的最大矩形；
3. 所有行的最大矩形取 max。

**用户已 AC 84（柱状图最大矩形），85 是它的二维推广**——直接复用单调栈，一次写对。

## 验证

- 对拍 **3000 组随机矩阵 vs 暴力枚举 0 不一致**；
- 样例：`[["1","0","1","0","0"],...] → 6`。

## 复杂度

- 时间 **O(m×n)**（每行一次单调栈）；空间 O(n)。