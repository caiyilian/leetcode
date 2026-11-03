"""647. 回文子串（二刷）——中心扩展计数（用户 AC 版）

用户二刷（2026-11-03 12:41 提交 758353963，AC 一次通过，103ms/19.3MB）
- 与 5 最长回文子串同模板：中心扩展，每次扩展命中 = 找到一个回文，count += 1
- 奇数中心 (i,i) + 偶数中心 (i,i+1) 各枚举一遍；break 条件用 if/else
- 复杂度 O(n²)/O(1)——比 DP 表（O(n²)/O(n)）空间更优
"""


# ===== 用户 AC 版（中心扩展计数） =====
class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        result = 0
        for i in range(length):                    # 奇数中心 (i,i)
            left, right = i, i
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
        for i in range(length - 1):                # 偶数中心 (i,i+1)
            left, right = i, i + 1
            while left >= 0 and right < length:
                if s[left] == s[right]:
                    result += 1
                    left -= 1
                    right += 1
                else:
                    break
        return result


# ===== 参考：DP 表（另一种标准解法，dp[i][j]=s[i:j+1] 是否回文） =====
class SolutionDP:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        cnt = 0
        for length in range(1, n + 1):             # 按区间长度从小到大
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] != s[j]:
                    continue
                if length <= 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    cnt += 1
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("abc"))    # 3
    print(s.countSubstrings("aaa"))    # 6
    print(s.countSubstrings("aba"))    # 4
    print(s.countSubstrings("aaaa"))   # 10