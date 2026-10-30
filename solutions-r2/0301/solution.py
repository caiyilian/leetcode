"""301. 删除无效的括号（困难·二刷）——BFS 分层：删最少括号得到所有合法串（标准解）

用户 AC 版（2026-10-30 12:04 提交 757743685，111ms/19.8MB）
- ⚡ 核心：BFS 按"删除次数"分层——第 k 层 = 删 k 个括号能得到的全部串
- 逐层找：第一个出现合法串的层 = 最少删除层，收集该层所有合法串返回
- 每层 set 去重（不同删法可能删出同一串）；只删括号不删字母；空串守卫 return [""]
- isPair = 20 题练过的计数器判法（右括号不超左 + 最终左右相等）
"""

from typing import List


def isPair(s: str) -> bool:      # 括号串是否合法（计数器，等价 20 题）
    left = 0
    right = 0
    for c in s:
        if c == "(":
            left += 1
        elif c == ")":
            right += 1
            if right > left:     # 右括号不能先超左括号
                return False
    return left == right         # 最终左右平衡


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
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


if __name__ == "__main__":
    s = Solution()
    print(s.removeInvalidParentheses("()())()"))    # ["(())()", "()()()"]
    print(s.removeInvalidParentheses("(a)())()"))   # ["(a())()", "(a)()()"]
    print(s.removeInvalidParentheses(")("))         # [""]
    print(s.removeInvalidParentheses(""))           # [""]