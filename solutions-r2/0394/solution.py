"""394. 字符串解码（二刷）——单栈：数字/[/字符混存，遇 ] 弹到 [ 合并乘回（O(n)/O(n) 标准解）

用户 AC 版（2026-10-31 18:18 提交 757929758，一次通过，0ms/19.1MB）
- 单栈混存：数字（int）、'['、字符——'[' 当"分块起点"标记
- 遇 ']' = 验收一块：弹出到 '[' 为止拼成 each_str，再弹出数字 num，压回 num * each_str
- 多位数处理：isdigit 循环收集；边界无括号（纯字母）、单层、多层嵌套都正确
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        length = len(s)
        i = 0
        while i < length:
            if s[i].isdigit():
                num = []
                while i < length and s[i].isdigit():   # 多位数
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


# ===== 标准双栈参考（数字栈 + 字符串栈 + cur） =====
class SolutionStd:
    def decodeString(self, s: str) -> str:
        num_stack, str_stack = [], []
        cur, num = "", 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                num_stack.append(num)
                str_stack.append(cur)
                num, cur = 0, ""
            elif c == ']':
                cur = str_stack.pop() + cur * num_stack.pop()
            else:
                cur += c
        return cur


if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))       # aaabcbc
    print(s.decodeString("3[a2[c]]"))        # accaccacc
    print(s.decodeString("2[abc]3[cd]ef"))   # abcabccdcdcdef
    print(s.decodeString("abc"))             # abc
    print(s.decodeString("10[a]"))           # aaaaaaaaaa