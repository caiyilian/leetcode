# Created by Chono-Hina at 2026/09/16 20:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/palindrome-partitioning/

from typing import *
from leetgo_py import *

# @lc code=begin

def is_palindrome(s):
    p1, p2 = 0, len(s) - 1
    while p2 >= p1:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        length = len(s)
        result = []
        def fun(path, index):
            if index == length:                # 切完整个字符串 → 记录（基线按目标进度）
                result.append(path.copy())
                return
            for i in range(index + 1, length + 1):   # 穷举切割终点
                if is_palindrome(s[index:i]):        # 这段是回文才切
                    path.append(s[index:i])
                    fun(path, i)                     # 从切割点继续
                    path.pop()
        fun([], 0)
        return result
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partition(s)
    print("\noutput:", serialize(ans, "string[][]"))
