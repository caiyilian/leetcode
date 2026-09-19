# Created by Chono-Hina at 2026/09/19 21:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/longest-valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 栈存下标，栈底始终是"最后一个未匹配的右括号"（一堵墙）
        max_length = 0
        stack = [-1]                        # -1 哨兵免判空
        for i, c in enumerate(s):
            if c == ')':
                top = stack.pop()
                if top == -1:                # 栈空（哨兵被弹出）→ 这个 ')' 无匹配
                    stack.append(i)
                else:
                    if s[top] == '(':        # 配对成功
                        max_length = max(max_length, i - stack[-1])
                    else:                    # 栈顶是"没人要的右括号"→ 新的墙
                        stack.append(i)
            else:                            # '(' 直接入栈
                stack.append(i)
        return max_length
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestValidParentheses(s)
    print("\noutput:", serialize(ans, "integer"))
