# 84. 柱状图中最大的矩形 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 84. 柱状图中最大的矩形（Largest Rectangle in Histogram）· **困难**（栈分类收官题） |
| 链接 | https://leetcode.cn/problems/largest-rectangle-in-histogram/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 99/99 用例通过**（leetgo 复提交，用户力扣原提交已过） |
| 运行时间 | 127 ms（leetgo 噪声，击败 70%） |
| 内存 | 31.4 MB |

## ⚡⚡ 机考复习标记（用户要求：考之前必看）

## 解法（用户按提示实现：单调递增栈 + 双哨兵 + 弹出结算）

```python
class Solution:
    def largestRectangleArea(self, heights):
        result = 0
        heights = [0] + heights + [0]   # 双哨兵：开头 0 保左边界；结尾 0 强制全部结算
        length = len(heights)
        stack = []                      # 单调递增栈，存下标
        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:   # while：一个矮子顶掉一串
                h = heights[stack.pop()]
                w = i - stack[-1] - 1   # 右边界=i（第一个更矮），左边界=弹后栈顶
                result = max(result, h * w)
            stack.append(i)
        return result
```

**用户认知链路**：先自创错误思路（"当前高 × 栈大小"，[5,6] 处碰巧算出 10）→ 提示后实现正确版但**仍有三个疑问**（是否每根柱子都结算 / 为什么 while 不是 if / 双哨兵作用）→ 逐条讲透后确认理解。归档时保留完整答疑。

## 验证

- 对拍 **5 万组随机柱状图 vs 暴力枚举参照 0 不一致**（含全递增/全递减/等高）；
- 官方样例：`[2,1,5,6,2,3] → 10`、`[2,4] → 4`。

## 复杂度

- 时间 **O(n)**（每下标入栈一次、出栈一次）；空间 **O(n)**。

## 三个必考点（用户疑问的答案，全文见 analysis.md）

1. **每根柱子都在"被弹出时"结算恰好一次**——右边界=触发弹出的更矮柱，左边界=弹后栈顶；
2. **while 不是 if**：一个矮柱子同时是多个高柱子的右边界，全部要结算；
3. **双哨兵**：开头 0 保左边界不越界（省判空），结尾 0 强制清空栈结算（否则残留柱子漏算）。

## 🏆 栈分类 5/5 全通关（20 → 155 → 394 → 739 → 84）