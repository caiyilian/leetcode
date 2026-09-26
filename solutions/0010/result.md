# 10. 正则表达式匹配 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 10. 正则表达式匹配（Regular Expression Matching）· **困难**（v2 新增题 · 二维 DP） |
| 链接 | https://leetcode.cn/problems/regular-expression-matching/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-26 |
| 最终提交 | ✅ **ACCEPTED - 354/354 用例通过**（leetgo 复提交） |
| 运行时间 | 7 ms（击败 78%） |
| 内存 | 19.1 MB |

## 解法（用户二维 DP，标准）

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):                  # 空 s 匹配 "x*" 等
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]    # 普通匹配：继承前面
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]        # * 匹配 0 次
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = (dp[i - 1][j] or dp[i][j])   # * 匹配 ≥1 次
        return dp[m][n]
```

## ⚠️ 调试记录（用户 2 处 bug，AI 误报 1 处）

| 问题 | 说明 | 是否必须改 |
|------|------|-----------|
| ① 返回 `dp[m-1][n-1]` | dp 是 (m+1)×(n+1)，答案在右下角 `dp[m][n]`——少算一行/列导致 `''/'a*'`、`'mississippi'` 错 | ✅ 致命 |
| ② 普通字符 `dp[i][j]=True` | 应继承 `dp[i-1][j-1]`（前面不匹配则整体不匹配） | ✅ 必须 |
| ③ `if` 顺序（普通字符在前） | **AI 误报**——`s` 不含 `*`，`s[i-1]` 永远不等 `'*'`，不会误入普通分支，顺序无所谓。**用户验证后纠正了 AI** | ❌ 不用改 |

**用户亮点**：质疑 AI 的建议（顺序），实测验证后确认自己只改 2 处就 AC——判断比 AI 更准确。

## 核心：`*` 的两个分支（OR）

```
dp[i][j] = dp[i][j-2]                 # * 匹配 0 次（丢掉 p[j-2]*，s 不动）
         | dp[i-1][j]                 # * 匹配 ≥1 次（s 前进一步，p 不动）
         （当 s[i-1] == p[j-2] 或 p[j-2] == '.'）
```

## 验证

- 对拍 **3000 组随机 vs Python `re.fullmatch` 0 不一致**；
- 样例：`aa/a→False`、`aa/a*→True`、`ab/.*→True`、`aab/c*a*b→True`、`mississippi/mis*is*p*.→False`、`''/a*→True`。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)。