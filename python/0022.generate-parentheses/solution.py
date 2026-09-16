# Created by Chono-Hina at 2026/09/16 17:29
# leetgo: 1.4.18
# https://leetcode.cn/problems/generate-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        对于一个节点
        如果是左括号，那么往下走可以是左也可以是右，但是左的数量必须小于n才能继续左
        如果是右括号，那么往下走，可以是右括号，也可以左括号
        但是，继续右括号的条件是，之前的的左括号，还存在至少1个没有匹配的右括号
        """
        result = []
        def fun(path, left, right):
            if len(path) == 2*n:
                result.append("".join(path))
                return
            if left < n:            # 左括号数没满 → 能放 (
                path.append("(")
                fun(path, left+1, right)
                path.pop()
            if left > right:        # 还有未匹配的左括号 → 能放 )
                path.append(")")
                fun(path, left, right+1)
                path.pop()
        fun([], 0, 0)
        return result
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
