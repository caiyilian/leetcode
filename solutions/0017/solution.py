# Created by Chono-Hina at 2026/09/16 16:06
# leetgo: 1.4.18
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:               # 空串边界：没有字母可组合 → []
            return []
        length = len(digits)
        result = []
        num2char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        """
        每一层遍历的是那一层的那些字母
        给下一层传下一个字符
        """
        def fun(path, index=0):
            if len(path) == length:
                result.append("".join(path))  # join 创建新字符串（不可变），天然免疫引用陷阱
                return
            for c in num2char[digits[index]]:
                path.append(c)
                fun(path, index+1)
                path.pop()
        fun([])
        return result
        

# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))
