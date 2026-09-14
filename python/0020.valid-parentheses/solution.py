# Created by Chono-Hina at 2026/09/14 10:59
# leetgo: 1.4.18
# https://leetcode.cn/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isValid(self, s: str) -> bool:
        List = [None, s[0]]
        pair_dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for c in s[1:]:
            # 列表里面没有东西了，表示这个是新的东西
            if List[-1] is None:
                if pair_dict.get(c, ""):
                    # 如果这个新入栈的是一个右括号，那必定是出错
                    return False
                List.append(c)
                continue
            # 并且当前符号是右括号
            if pair_dict.get(c, ""):
                # 如果是对应的左括号，就出栈
                if pair_dict[c] == List[-1]:
                    List.pop(-1)
                    continue
                # 否则，就出错
                return False
            # 当前符号是新增的左括号
            List.append(c)
            
            
        if List[-1] is None:
            return True
        return False
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
