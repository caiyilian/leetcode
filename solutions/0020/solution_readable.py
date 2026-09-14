# -*- coding: utf-8 -*-
"""
第 20 题 有效的括号 · 标准优化版
与用户原版思路一致（栈 + 右括号映射左括号），三点优化使其更快更省：
① 无 s[1:] 切片（省 O(n) 字符串副本）② dict 一次判断 ③ 无 None 哨兵（not stack 判空）
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')': '(', '}': '{', ']': '['}
        for c in s:                        # 直接遍历，无切片
            if c in pair:                  # 右括号：必须匹配栈顶
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:                          # 左括号：入栈
                stack.append(c)
        return not stack                   # 栈空 = 全部匹配