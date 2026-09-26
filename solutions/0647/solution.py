# Created by Chono-Hina at 2026/09/26 15:59
# leetgo: 1.4.18
# https://leetcode.cn/problems/palindromic-substrings/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countSubstrings(self, s: str) -> int:
        # 中心扩展法（同 5 最长回文子串的套路）：每扩展成功一次 = 找到一个回文
        length = len(s)
        count = 0
        # 奇数中心：单字符为中心（"aba" 型）
        for i in range(length):
            left = right = i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        # 偶数中心：相邻字符对中间为中心（"abba" 型）
        for i in range(length - 1):
            left = i
            right = i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        return count
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().countSubstrings(s)
    print("\noutput:", serialize(ans, "integer"))
