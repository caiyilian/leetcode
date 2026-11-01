"""139. 单词拆分（二刷）——前缀 DP（O(n²)/O(n) 标准解）

用户 AC 版（2026-11-01 17:35 提交 758057691，一次通过，7ms/19.1MB）
- 【反向排除版】：dp = [True]*(n+1)，只有"找不到任何可接的前缀 j"才把 dp[i] 标 False（for-else）
- 语义：dp[i] = s[0:i] 能否被 wordDict 完全拆分；dp[j] 真 + s[j:i]∈字典 → dp[i] 真
- ⚡ for-else 是 Python 特色写法：else 在循环没 break 时执行，天然表达"一个都没连上"

标准版（对照）：dp[0]=True + 找到可拆才置 True，语义等价
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [True] * (length + 1)          # 默认可行（反向排除法）

        for i in range(1, length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:   # 前缀可拆 + 最后一段是单词
                    break                          # 找到一个拆法即可
            else:                                  # 循环没 break → 一个都没连上
                dp[i] = False                      # 这个前缀不可拆
        return dp[-1]


# ===== 参考：标准正向版（dp[0]=True + 置真） =====
class SolutionStd:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("leetcode", ["leet", "code"]))           # True
    print(sol.wordBreak("applepenapple", ["apple", "pen"]))      # True
    print(sol.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False