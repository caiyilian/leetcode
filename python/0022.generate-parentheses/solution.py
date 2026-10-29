# Created by Chono-Hina at 2026/09/16 17:29
# leetgo: 1.4.18
# https://leetcode.cn/problems/generate-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        加右括号的条件是，之前左括号数量大于右括号数量
        加左括号的条件是，之前的左括号数量小于n
        """
        if n == 0:
            return []
        result = []

        def fun(path, num_left=0):
            if len(path) == 2 * n:
                result.append("".join(path))
                return path
            if len(path) - num_left < num_left:   # 右括号数 < 左括号数 → 可加右
                path.append(")")
                path = fun(path, num_left)
                path.pop()
            if num_left < n:                       # 左括号数 < n → 可加左
                path.append("(")
                path = fun(path, num_left + 1)
                path.pop()
            return path

        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
