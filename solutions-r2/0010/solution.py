"""10. 正则表达式匹配（二刷）——记忆化递归（用户 AC 版）困难题·收官题

用户二刷（2026-11-04 17:24 提交 758597776，AC，23ms/19.3MB；TLE→AC 演进）
- 自顶向下递归 fun(i, j)：s 前 i 个 与 p 前 j 个 是否匹配（下标从 0 起）
- 转移：
  - p[j] 非 '*'：s[i] 与 p[j] 匹配（相等或 p[j]=='.'）且 前面也匹配
  - p[j] == '*'：* 匹配 0 次（p 退两位）或 匹配 ≥1 次（s 退一位，前提当前位能对上）
- ⚡ TLE→AC：把"会消耗 s 的递归 fun(i-1,j)"挪到 and 右侧，靠短路剪枝——本题无记忆化也能过
- 与 72/1143 同族：双串 DP 表，只是多 '*' 一个分支
"""

from typing import List


# ===== 用户 AC 版（记忆化递归，短路剪枝） =====
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True
        ls = len(s)
        lp = len(p)

        def is_fit(i, j):
            if i < 0 or j < 0:
                return False
            return (s[i] == p[j]) or (p[j] == ".")

        def fun(i, j):
            if i < 0 and j < 0:          # 都耗尽 → 匹配
                return True
            if j < 0:                    # p 耗尽但 s 还有 → 不匹配
                return False
            if p[j] != "*":              # 普通字符 / '.'
                return is_fit(i, j) and fun(i - 1, j - 1)
            # ⚡ '*'：匹配 0 次（p 退 2） 或 匹配 ≥1 次（s 退 1，且当前位能对上）
            # 短路顺序关键：先试"匹配 0 次"；消耗 s 的分支放 and 右侧
            return fun(i, j - 2) or (is_fit(i, j - 1) and fun(i - 1, j))

        return fun(ls - 1, lp - 1)


# ===== 参考：标准二维 DP（自底向上，模板一刷版） =====
class SolutionDP:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):                # 空 s 匹配 "x*" / "x*y*"
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]          # 最后一位对上
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]              # * 匹配 0 次
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]   # * 匹配 ≥1 次
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    print(s.isMatch("aa", "a"))          # False
    print(s.isMatch("aa", "a*"))         # True
    print(s.isMatch("ab", ".*"))         # True
    print(s.isMatch("aab", "c*a*b"))     # True
    print(s.isMatch("mississippi", "mis*is*p*."))  # False