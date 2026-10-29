# Created by Chono-Hina at 2026/09/16 20:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/palindrome-partitioning/

from typing import *
from leetgo_py import *

# @lc code=begin

def isPa(s):
    length = len(s)
    p1 = 0
    p2 = length - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return []
        result = []
        length = len(s)

        def fun(path, start=0):
            if start >= length:                    # 切完整个串 → 收集
                result.append(path.copy())
                return path
            for i in range(start, length):
                if isPa(s[start:i + 1]):           # 子串是回文才切
                    path.append(s[start:i + 1])
                    path = fun(path, i + 1)        # 从切割点后继续
                    path.pop()
            return path

        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partition(s)
    print("\noutput:", serialize(ans, "string[][]"))
