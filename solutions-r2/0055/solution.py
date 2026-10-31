"""55. 跳跃游戏（二刷）——贪心：最远可达距离（O(n)/O(1) 标准解）

用户 AC 版（2026-10-31 21:47 提交 757956270，WA×2 → AC，20ms/19.9MB）
- 贪心：far = 从已遍历位置能到达的最远下标
- 遍历时：若当前位置 i 在 far 内（能到达），更新 far = max(far, i + nums[i])
- ⚡ WA 修复：遍历到 length-1 为止（而非 length）——最后一个元素是否为 0 无关紧要，因为
    「能到达末尾」就赢了；用 range(length-1) 避免末尾 0 被误判为死路
- 等价写法（更通用）：若 i > far 直接 False（到不了当前位置），遍历完全部返回 True
"""

from typing import List


# ===== 用户 AC 版（range(length-1) + far==i 判 0） =====
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        length = len(nums)
        for i in range(length - 1):          # ⚡ 只到 length-1（末尾 0 不算死路）
            if far == i and nums[i] == 0:    # 当前位置无法越过
                return False
            far = max(far, i + nums[i])
        return True


# ===== 标准写法参考（i > far 判死路，语义更清晰） =====
class SolutionStd:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums)):
            if i > far:                      # 到不了当前位置 → 死路
                return False
            far = max(far, i + nums[i])      # 更新最远可达
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))    # True
    print(s.canJump([3, 2, 1, 0, 4]))    # False
    print(s.canJump([0]))                # True（单元素已到终点）
    print(s.canJump([2, 0, 0]))          # True（到末尾即胜，末尾 0 不算死路）