"""20. 有效的括号（二刷）——栈 + 哈希映射（O(n)/O(n) 标准解）

用户 AC 版（2026-10-30 16:05 提交 757780196，RE→AC→WA→AC 后定稿，5ms/19.3MB）
- 左括号压栈；右括号弹出栈顶比对（映射表左→右）
- ⚡ 关键：判空栈必须在 pop 之前（or 短路先查 not stack）——v1 RE / v3 WA 都是空栈问题
- 结束 return not stack（右括号多了栈空提前返回 False；左括号多了栈非空返回 False）
"""


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


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))   # True
    print(s.isValid("(]"))       # False
    print(s.isValid("([{}])"))   # True
    print(s.isValid(""))         # True
    print(s.isValid("]"))        # False