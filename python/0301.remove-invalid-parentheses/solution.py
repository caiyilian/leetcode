# Created by Chono-Hina at 2026/09/26 16:55
# leetgo: 1.4.18
# https://leetcode.cn/problems/remove-invalid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

def isPair(s):
    left = 0
    right = 0
    for c in s:
        if c == "(":
            left += 1
        elif c == ")":
            right += 1
            if right > left:
                return False
    return left == right


class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        if not s:
            return [""]          # ⚡ 空串本身就是合法（删 0 个）→ [""]
        result = []
        hash_set = set()
        hash_set.add(s)

        while hash_set and (not result):     # 找到结果层才停
            next_set = set()
            for s in hash_set:
                if isPair(s):
                    result.append(s)         # 当前层出现合法串 → 收集
                else:
                    for i in range(len(s)):  # 每个括号位置删一次 → 下一层
                        if s[i] not in "()":
                            continue         # 字母不删
                        new_str = s[:i] + s[i + 1:]
                        if not new_str:
                            continue
                        next_set.add(new_str)  # ★ set 去重（不同删法同串）
            hash_set = next_set

        return result if result else [""]
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().removeInvalidParentheses(s)
    print("\noutput:", serialize(ans, "string[]"))
