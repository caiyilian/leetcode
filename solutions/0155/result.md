# 155. 最小栈 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 155. 最小栈（Min Stack）· 中等（栈分类第 2 题） |
| 链接 | https://leetcode.cn/problems/min-stack/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 45/45 用例通过**（leetgo 复提交） |
| 运行时间 | 123 ms（leetgo 噪声，击败 33%） |
| 内存 | 32.3 MB |

## 解法（用户独立完成：辅助栈同步记录，含 inf 哨兵优化）

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.time_min_val = [float('inf')]     # 辅助栈；inf 哨兵免判空

    def push(self, value):
        self.stack.append(value)
        self.time_min_val.append(min(value, self.time_min_val[-1]))

    def pop(self):
        self.stack.pop()
        self.time_min_val.pop()                # 同步弹出（回到上一时刻最小值）

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.time_min_val[-1]           # O(1)
```

**用户的小优化**：辅助栈初始 `[float('inf')]` → `min(value, inf) = value`，push 第一个元素时不用判空（比"if not min_stack"少一行）。

## 验证

- 对拍 **5 万步随机操作序列（含负数/重复值）vs 暴力 min 参照 0 不一致**；
- 官方样例：push(-2)/push(0)/push(-3) → getMin=-3、pop 后 top=0、getMin=-2；
- 复杂度：四个方法均无循环，全部 **O(1)** ✅（符合题目要求）；空间 O(n)。

## 踩坑记录

- leetgo 模板自带 5 个空方法体（__init__/push/pop/top/getMin），首次替换只覆盖 __init__ 导致 IndentationError（208 同款）——清理残留后通过。