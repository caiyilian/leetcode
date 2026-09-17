# Created by Chono-Hina at 2026/09/17 19:37
# leetgo: 1.4.18
# https://leetcode.cn/problems/decode-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decodeString(self, s: str) -> str:
        """
        一个函数，处理字符串
        如果是普通字符，就加到列表里面
        如果是数字，就提取数字，直到左括号[，就可以知道数字是多少
        然后遇到[也是正常加入栈
        但是遇到]就得开始逐个pop，直到[
        单栈混合版：数字串 / 字母 / "[" 全存一个栈
        """
        result = []
        c26 = set(chr(i + 97) for i in range(26))
        number = set(str(i) for i in range(10))
        num_str = ""
        for i, c in enumerate(s):
            if c in c26:
                result.append(c)
            elif c in number:
                num_str += c
            elif c == '[':
                result.append(num_str)
                result.append("[")
                num_str = ""
            else:  # 那就是 ]，一直 pop 到 [
                each_str = ""
                while True:
                    c2 = result.pop()
                    if c2 == "[":
                        break
                    each_str = c2 + each_str
                each_str = each_str * int(result.pop())
                result.append(each_str)
        return "".join(result)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().decodeString(s)
    print("\noutput:", serialize(ans, "string"))
