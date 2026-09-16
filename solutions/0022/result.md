# 22. 括号生成 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 22. 括号生成（Generate Parentheses）· 中等（回溯家族第 5 题 / 标签含动态规划） |
| 链接 | https://leetcode.cn/problems/generate-parentheses/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 8/8 用例通过** |
| 运行时间 | 3 ms（击败 38%） |
| 内存 | 19.1 MB（击败 94%） |

## 解法（用户回溯版：双条件剪枝）

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def fun(path, left, right):
            if len(path) == 2*n:
                result.append("".join(path))
                return
            if left < n:            # 条件①：左括号数没满才能放 (
                path.append("(")
                fun(path, left+1, right)
                path.pop()
            if left > right:        # 条件②：还有未匹配的左括号才能放 )
                path.append(")")
                fun(path, left, right+1)
                path.pop()
        fun([], 0, 0)
        return result
```

**用户 docstring 自悟**："继续右括号的条件是，之前的左括号还存在至少 1 个没有匹配的右括号"——即 `left > right`（前缀合法性的本质：任意前缀右括号不多于左括号）。

## 双解法（用户问的 DP 收录在 solution_readable.py）

| | 回溯（定稿） | DP（readable） |
|--|------------|---------------|
| 视角 | 按位置逐位决定放 ( 还是 ) | 按配对：第 1 个 ( 和谁配对 → "(" + a + ")" + b |
| 剪枝 | `left < n` + `left > right` | 无（构造即合法） |
| 方向 | 自顶向下 DFS | 自底向上 dp[0]→dp[n] |
| 复杂度 | O(Cₙ×n) | O(Cₙ×n)（相同，非优化型 DP） |

## 验证（三重对拍）

- **n=1..6 三方一致**：用户回溯版 vs DP 版 vs 暴力全枚举（2²ⁿ 组合 + 合法性检查）——全部 OK；
- **卡特兰数命中**：n=1..7 → 1, 2, 5, 14, 42, 132, 429 完美对应 Cₙ = C(2n,n)/(n+1)；
- 官方样例：n=3 → 5 个、n=1 → 1 个。

## 复杂度

- 时间 **O(Cₙ×n)**（Cₙ = 卡特兰数 ≈ 4ⁿ/(n^1.5·√π)，答案数 × 每答案生成 O(n)）；
- 空间 **O(n)**（递归深度 2n + path）；DP 版空间 O(Cₙ×n)（存所有中间串）。