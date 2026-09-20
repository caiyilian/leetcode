# Created by Chono-Hina at 2026/09/20 18:15
# leetgo: 1.4.18
# https://leetcode.cn/problems/minimum-window-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口 + 哈希：need 记录 t 需求，windows 记录窗口计数，valid 记达标字符种类数
        need = {}
        windows = {}
        for c in t:
            if c not in need:
                need[c] = 1
                windows[c] = 0
            else:
                need[c] += 1
                windows[c] = 0
        class_num = len(need)
        valid = 0
        best = ''
        length = float('inf')
        left, right = 0, 0
        while right < len(s):
            if s[right] in need:
                windows[s[right]] += 1
                if windows[s[right]] == need[s[right]]:
                    valid += 1        # 该字符达标
            if valid == class_num:     # 窗口全部达标
                if length > right - left + 1:
                    length = right - left + 1
                    best = s[left:right + 1]
                while True:            # 收缩左边界
                    left += 1
                    if s[left - 1] in need:
                        windows[s[left - 1]] -= 1
                        if windows[s[left - 1]] < need[s[left - 1]]:
                            valid -= 1        # 窗口失效
                            if right == len(s) - 1:
                                return best
                            break
                    if length > right - left + 1:
                        length = right - left + 1
                        best = s[left:right + 1]
            right += 1
        return best
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))
