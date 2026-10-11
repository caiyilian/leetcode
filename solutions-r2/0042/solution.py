from typing import List

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
        # 二刷版：单调栈（存索引，O(n) 时间 / O(n) 空间）
        # 弹出条件：遇到比栈顶高的柱子 → 弹出"洼地"结算水量
        # 水量 = 宽(左右墙距离-1) × 高(min(左右墙) - 洼地底)
        stack = [0]                    # 单调递减栈，预置下标 0 当第一根"墙"
        length = len(height)
        total = 0
        for i in range(1, length):
            while stack and height[i] > height[stack[-1]]:   # 当前柱比栈顶高 → 栈顶是洼地
                mid = stack.pop()      # 洼地（凹槽底）
                if not stack:          # 栈空了 = 没有左墙 → 这格水没法结算（左墙高度不够）
                    break              # ★ 不能只用 while 条件：空栈发生在 pop 之后的循环体内
                w = i - stack[-1] - 1              # 宽 = 右墙(i) 与 左墙(新栈顶) 的距离 - 1
                h = min(height[i], height[stack[-1]]) - height[mid]  # 高 = min(两墙) - 洼地底
                total += h * w
            stack.append(i)
        return total


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))   # 6
    print(s.trap([4, 2, 0, 3, 2, 5]))                    # 9
    print(s.trap([2, 0, 2]))                             # 2
    print(s.trap([3, 1, 2]))                             # 1
    print(s.trap([]))                                    # 0