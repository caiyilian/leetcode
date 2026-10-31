"""739. 每日温度（二刷）——单调栈（O(n)/O(n) 标准解）

用户 AC 版（2026-10-31 18:48 提交 757932664，一次通过，87ms/28.3MB）
- 单调递减栈（存下标）：栈底到栈顶温度递减
- 遍历 i：while 栈非空且 栈顶温度 < 当前温度 → 弹出结算（res[弹]=i-弹）；最后 i 入栈
- ⚡ 相等不结算（严格 <）：等温天不算"更高温度"，正确保留在栈里等更高温度
- 没被结算的（如最后一天/最大温度）保持 0
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                     # 存下标，温度单调递减
        length = len(temperatures)
        results = [0] * length
        for i in range(length):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()    # 找到第一个更高的温度 → 结算
                results[index] = i - index
            stack.append(i)
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    # [1, 1, 4, 2, 1, 1, 0, 0]
    print(s.dailyTemperatures([30, 40, 50, 60]))     # [1, 1, 1, 0]
    print(s.dailyTemperatures([30, 60, 90]))         # [1, 1, 0]