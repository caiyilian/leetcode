"""84. 柱状图中最大的矩形（二刷）——单调栈 + 首尾哨兵 0（O(n) 最优解）

用户 AC 版（2026-10-17 22:19 提交 755422634，WA→AC）
核心：单调递增栈存下标；遇到更矮的柱子就弹出结算（宽 = i - 新栈顶 - 1）；
      头尾补 0 哨兵（头 0 兜空栈 / 尾 0 强制清栈）。
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 哨兵：头 0 保证栈永远非空；尾 0 保证最后强制结算所有柱子
        heights = [0] + heights + [0]
        length = len(heights)
        stack = [0]
        result = 0
        for i in range(length):
            # 遇到更矮的柱子 → 弹出结算（栈单调递增，栈顶是当前最高）
            while heights[stack[-1]] > heights[i]:
                now_index = stack.pop()
                now_value = heights[now_index]
                # ★ 宽 = i（右边第一个更矮）- 新栈顶（左边第一个更矮）- 1
                #   不是 i - now_index！那是"从自己到右界"，漏掉左边能撑的
                area = now_value * (i - stack[-1] - 1)
                result = max(area, result)
            stack.append(i)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))   # 10
    print(s.largestRectangleArea([2, 4]))               # 4
    print(s.largestRectangleArea([2, 1, 2]))            # 3
    print(s.largestRectangleArea([1]))                  # 1