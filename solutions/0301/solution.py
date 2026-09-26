# Created by Chono-Hina at 2026/09/26 16:55
# leetgo: 1.4.18
# https://leetcode.cn/problems/remove-invalid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

def invaid(s):
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        elif c == ")":
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0

def next_level(s):
    length = len(s)
    s_set = set()
    for i in range(length):
        if s[i] in "()":                  # 只删括号，跳过字母（优化）
            s_set.add(s[:i] + s[i + 1:])
    return s_set


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        # BFS 逐层删括号：第一个合法层 = 最少删除
        # set 去重：删不同位置得到同一串时避免重复
        level = {s}
        while level:
            valid = [each for each in level if invaid(each)]
            if valid:
                return valid              # 最少删除层，返回所有合法结果
            next_level_set = set()
            for x in level:
                next_level_set.update(next_level(x))
            level = next_level_set
        return [""]
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeInvalidParentheses(s)
    print("\noutput:", serialize(ans, "string[]"))
