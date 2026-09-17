# 739. 每日温度 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 739. 每日温度（Daily Temperatures）· 中等（栈分类第 4 题 / **单调栈入门**） |
| 链接 | https://leetcode.cn/problems/daily-temperatures/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 48/48 用例通过**（leetgo 复提交） |
| 运行时间 | 95 ms（击败 61%，leetgo 噪声） |
| 内存 | 27.6 MB（击败 85%） |

## 解法（用户按提示独立重写：单调栈存下标 + 定点填）

```python
class Solution:
    def dailyTemperatures(self, temperatures):
        length = len(temperatures)
        index_stack = []              # ★ 存下标（距离 = i - idx）
        result = [0] * length         # 全 0：没被顶掉的（后面无更高温）= 0

        for i in range(length):
            while index_stack and temperatures[index_stack[-1]] < temperatures[i]:
                result[index_stack[-1]] = i - index_stack[-1]   # 定点填
                index_stack.pop()
            index_stack.append(i)
        return result
```

**用户路径**：先写"存值的半成品"（count 数弹出个数当距离，思路对但算不出距离）→ 提示后**没看参考答案**独立重写为存下标版——两个修正（存下标 / 定点填）全部自己吸收。

## 验证

- 对拍 **5 万组随机温度序列 vs 暴力双循环参照 0 不一致**；
- 官方样例：`[73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]`；
- 边界：严格递增 `[30,40,50,60]→[1,1,1,0]`、严格递减、单元素 `[30]→[0]`；
- 复杂用例 `[89,62,...,70] → [8,1,5,4,3,2,1,1,0,0]` 全对。

## 复杂度

- 时间 **O(n)**（每元素入栈一次、出栈一次）；空间 **O(n)**。

## ⚡ 核心教训（本归档最值钱的一条）

**单调栈存"下标"而不是"值"**——"距离/跨度"类问题的结算公式是 `i - idx`，存值只能判断"有没有"，算不出"隔多远"。判断取值用 `temperatures[stack[-1]]`，结算用 `i - stack[-1]`。