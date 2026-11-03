"""5. 最长回文子串（二刷）——中心扩展法（用户 AC 版）

用户二刷（2026-11-03 11:04 提交 758337989，AC，175ms/19.1MB）
- 中心扩展：奇数中心 (i,i) 与偶数中心 (i,i+1) 各枚举一遍，向两侧扩展到不等为止
- 官方标准解之一（O(n²)/O(1)），比 DP 版（O(n²)/O(n)）空间更优、代码更短
- 不是 DP：每个中心独立扩展，不用子问题的答案（DP 版见 analysis 讲解）
"""

from typing import List


# ===== 用户 AC 版（中心扩展） =====
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        length = len(s)
        for i in range(length):                    # 奇数长度：单字符中心
            left, right = i, i
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if right - left - 1 > len(result):
                result = s[left + 1:right]
        for i in range(length - 1):                # 偶数长度：双字符中心
            left, right = i, i + 1
            while left >= 0 and right < length:
                if s[left] != s[right]:
                    break
                left -= 1
                right += 1
            if right - left - 1 > len(result):
                result = s[left + 1:right]
        return result


# ===== 参考：DP 版（标签"动态规划"的来源） =====
class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]       # dp[i][j] = s[i:j+1] 是回文
        best = s[0]
        for length in range(1, n + 1):             # 按区间长度从小到大（小区间先算）
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    continue                       # 两端不等 → 不是回文
                if length <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True                # 长度≤2 直接成立；否则看内层
                    if length > len(best):
                        best = s[i:j + 1]
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))    # bab / aba（任一）
    print(s.longestPalindrome("cbbd"))     # bb
    print(s.longestPalindrome("a"))        # a
    print(s.longestPalindrome("aaaa"))     # aaaa