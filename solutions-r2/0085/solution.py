"""85. 最大矩形（二刷）——逐行前缀高度 + 复用 84 单调栈（O(m×n) 最优解）

用户 AC 版（2026-10-17 22:27 提交 755424023，一次通过）
核心：把二维矩阵逐行降维成一维柱状图（heights[j] = 第 j 列往上连续 '1' 的高度），
      每行复用 84 的单调栈求最大矩形，取全局 max。
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n

        # 复用 84 的单调栈函数（子函数内嵌）
        def fun(heights: List[int]) -> int:
            heights = [0] + heights + [0]
            length = len(heights)
            stack = [0]
            result = 0
            for i in range(length):
                while heights[stack[-1]] > heights[i]:
                    now_index = stack.pop()
                    now_value = heights[now_index]
                    area = now_value * (i - stack[-1] - 1)
                    result = max(area, result)
                stack.append(i)
            return result

        result = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':     # ★ 矩阵元素是字符串 '0'/'1'，不是 int 0/1！
                    heights[j] = 0          # 遇 0 高度清零
                else:
                    heights[j] += 1         # 遇 1 累加（连续 1 的高度）
            result = max(result, fun(heights))  # 每行当柱状图跑 84
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maximalRectangle([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))  # 6
    print(s.maximalRectangle([["0"]]))    # 0
    print(s.maximalRectangle([["1"]]))    # 1