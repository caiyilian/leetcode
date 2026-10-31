"""45. 跳跃游戏 II（二刷）——贪心分层：end/far 双指针版（O(n)/O(1) 标准解）⚡⚡⚡ 重点复习

用户 AC 版（2026-10-31 22:55 提交 757965482，WA×1→AC，7ms/19.8MB）
- ⚡⚡⚡ 用户标记：一刷花了很久、二刷又忘了（2026-10-31 确认）——重点复习题

核心模型（"分层"思想，等价 BFS 按层数）：
- end = 当前这一步能到达的右边界（"墙"）
- far = 墙内所有格子向前够，最远能摸到哪（下一层的墙）
- 遍历 i：far 每步更新；i 撞到 end → 结算一步 step+1，把墙推到 far

⚡ 二刷踩的坑（WA 一次）：不要 while+开头 step+=1+i=next_start 跳层写法——
  会重复计数（一步到终点被算成 2 步）且漏看层内位置。用 for 逐格走 + 踩墙才结算。
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)

        step = 0
        far = 0
        end = 0
        for i in range(length - 1):        # 只到倒数第 2 个（到末尾即完成，末尾不参与起跳）
            far = max(far, nums[i] + i)    # ① 每步更新最远可达
            if i == end:                   # ② 踩到当前层的墙 → 结算一步
                step += 1
                end = far                  #    墙推到 far（下一层的边界）
        return step


# ===== 一刷写法参考（2026-09-18 AC，若你喜欢这版也可用） =====
class SolutionV1:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        steps = 0
        end = 0
        far = 0
        for i in range(n - 1):
            far = max(far, i + nums[i])
            if i == end:
                steps += 1
                end = far
        return steps


if __name__ == "__main__":
    s = Solution()
    print(s.jump([2, 3, 1, 1, 4]))     # 2
    print(s.jump([2, 3, 0, 1, 4]))     # 2
    print(s.jump([0]))                 # 0
    print(s.jump([1, 1, 1, 1]))        # 3