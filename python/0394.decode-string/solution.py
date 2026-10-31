# Created by Chono-Hina at 2026/09/17 19:37
# leetgo: 1.4.18
# https://leetcode.cn/problems/decode-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        length = len(s)
        i = 0
        while i < length:
            if s[i].isdigit():
                num = []
                while i < length and s[i].isdigit():
                    num.append(s[i])
                    i += 1
                num = int("".join(num))
                stack.append(num)
                stack.append(s[i])                     # 加上 '['
            elif s[i] == ']':                          # 验收一块
                each_str = ""
                while stack[-1] != "[":                # 弹出到分块起点
                    c = stack.pop()
                    each_str = c + each_str
                stack.pop()                            # 去掉 '['
                num = stack.pop()                      # 弹出重复次数
                stack.append(num * each_str)           # 乘回压栈
            else:                                      # 字母
                stack.append(s[i])
            i += 1
        return "".join(stack)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))
