"""32. 最长有效括号（二刷）——栈存下标 + 段起点（用户 AC 版）困难题

用户二刷（2026-11-04 16:39 提交 758586256，AC，19ms/20.2MB，WA→AC 演进）
- 思路：栈存 '(' 下标 + left_num 计数 + start 记录"当前段的起点"
- 遇见 ')'：无未配 '(' → start 移到 i+1（开启新段）；有 → pop 一个 '('，
  结算长度 = i - (段起点或栈顶 '(' 的前一位)
- ⚡ WA 复盘（16:31 版）：`i - start + 1 - left_num` 以 start 为基准计算，
  当段内有"被匹配掉但没闭合"的 '(' 时会把 unpaired 的长度也包进来算错
  （反例 '()(()' 算成 4，正确 2）；AC 版改为以"栈顶 '(' 前一位"为左边界，
  只算真正闭合成对的窗口 ✨
- 对比：标准哨兵栈版（-1 打底）更简洁，面试首选；DP 版是另一思路（见参考）
"""

from typing import List


# ===== 用户 AC 版（栈存下标 + left_num + start 段起点） =====
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        length = len(s)
        result = 0
        start = 0
        left_num = 0
        for i in range(length):
            if s[i] == ')':
                if left_num == 0:                    # 没有待匹配的 '(' → 当前段断了
                    start = i + 1                    # 新段从下一位开始
                else:
                    left_num -= 1
                    stack.pop()                      # 弹出一个 '('
                    # ⚡ 关键：左边界 = 段起点前一位（若段内无剩余 '('）
                    #         或栈顶 '(' 的前一位（还有剩余的 '('）
                    left_index = (start - 1) if left_num == 0 else stack[-1]
                    result = max(result, i - left_index)
            else:
                stack.append(i)                      # '(' 入栈存下标
                left_num += 1
        return result


# ===== 参考1：标准哨兵栈（面试推荐，最简洁） =====
class SolutionStd:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]                                 # ⚡ 哨兵：栈底存"段起点前一位"
        best = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:                            # 栈非空 → 配成了对
                    best = max(best, i - stack[-1])  # 以栈顶为左边界结算
                else:                                # 栈空 → 这个 ')' 是"墙"
                    stack.append(i)                  # 它成为新段的哨兵
        return best


# ===== 参考2：DP（dp[i] = 以 i 结尾的最长有效括号长度） =====
class SolutionDP:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        best = 0
        for i in range(1, n):
            if s[i] == '(':
                continue
            if s[i - 1] == '(':                                       # "...()"
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':  # "...((...))"
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0)
            best = max(best, dp[i])
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("(()"))             # 2
    print(s.longestValidParentheses(")()())"))          # 4
    print(s.longestValidParentheses("()(()"))           # 2
    print(s.longestValidParentheses(""))                # 0
    print(s.longestValidParentheses("()(())"))          # 6