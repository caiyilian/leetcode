# Created by Chono-Hina at 2026/09/19 11:45
# leetgo: 1.4.18
# https://leetcode.cn/problems/word-break/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 记忆化递归（top-down）：枚举"第一个单词"，吃掉前缀递归判断剩余
        mem = {'': True}
        def fun(s):
            if s not in mem:
                final = False
                for each_s in wordDict:
                    if s.startswith(each_s) and fun(s[len(each_s):]):
                        final = True
                        break
                mem[s] = final
            return mem[s]
        return fun(s)
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: List[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "boolean"))
