# Created by Chono-Hina at 2026/09/20 10:56
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展法：奇数中心（i,i）+ 偶数中心（i,i+1）
        length = len(s)
        if length == 1:
            return s
        max_length = 1
        best = s[0]
        # 奇数回文：以 i 为中心
        for i in range(length):
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            if max_length < (right - left - 1):      # while 后多退一步
                max_length = right - left - 1
                best = s[left + 1:right]
        # 偶数回文：以 i, i+1 为中心
        for i in range(length - 1):
            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1
                right += 1
            if max_length < (right - left - 1):
                max_length = right - left - 1
                best = s[left + 1:right]
        return best
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
