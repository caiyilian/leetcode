# 32. 最长有效括号 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 32. 最长有效括号（Longest Valid Parentheses）· **困难**（动态规划分类收官题） |
| 链接 | https://leetcode.cn/problems/longest-valid-parentheses/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 235/235 用例通过**（leetgo 复提交） |
| 运行时间 | 16 ms |
| 内存 | 20.4 MB |

## 解法（用户栈解法，主解）

```python
class Solution:
    def longestValidParentheses(self, s):
        max_length = 0
        stack = [-1]                        # -1 哨兵免判空
        for i, c in enumerate(s):
            if c == ')':
                top = stack.pop()
                if top == -1:               # 栈空 → 这个 ')' 无匹配
                    stack.append(i)
                else:
                    if s[top] == '(':       # 配对成功
                        max_length = max(max_length, i - stack[-1])
                    else:                   # 栈顶是"没人要的右括号"→ 新的墙
                        stack.append(i)
            else:
                stack.append(i)
        return max_length
```

## 栈解法的核心（用户自悟，理解到位）

栈底始终是**"最后一个未匹配的右括号"**（一堵墙），栈里其他是"等人配对的左括号"。关键等价性：

**栈顶是 `)` ⇔ 前面已经没有未匹配的左括号了**（因为左括号会优先被 pop 配对，能留到现在的右括号必然孤立）。

所以：
- 有效长度 = `i - stack[-1]`（当前右括号 - 墙的位置）；
- 每遇到一个"没人要的右括号"就多一堵墙，它成为新的"左边界"。

## DP 解法（略，暂不深入）

dp[i] = 以 s[i] 结尾的最长有效括号长度，分 `...()` 和 `...))` 两种情况。栈解法已足够，DP 版存档于 solution_readable.py 备用。

## 验证

- 对拍 **5 万组随机括号串 vs 标准栈 0 不一致**；
- 官方样例：`(()→2`、`)()())→4`、`()(()→2`、`(()())→6`。

## 复杂度

- 时间 **O(n)**；空间 O(n)。

## 🏆 动态规划分类 10/10 全通关！