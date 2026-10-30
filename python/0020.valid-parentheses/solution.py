# Created by Chono-Hina at 2026/09/14 10:59
# leetgo: 1.4.18
# https://leetcode.cn/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in hash_map:              # 左括号 → 压栈
                stack.append(c)
            else:                          # 右括号 → 弹栈比对
                if not stack or hash_map[stack.pop()] != c:
                    return False           # ★ 先查空栈（or 短路），再 pop
        return not stack                   # 栈空 = 全部匹配
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
