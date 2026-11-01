"""152. 乘积最大子数组（二刷）——双状态 DP（负负得正，O(n)/O(1) 最优）

用户 AC 版（2026-11-01 17:57 提交 758061177，一次通过，3ms/19.4MB）
- 核心：因为负数会翻转大小关系，必须同时维护「以 i 结尾的最大乘积」和「最小乘积」
- 转移：max_prod[i] = max(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
-        min_prod[i] = min(nums[i], max_prod[i-1]*nums[i], min_prod[i-1]*nums[i])
- 三个候选含义：① 重新开始一段（nums[i] 自己）② 乘上前一段最大 ③ 乘上前一段最小（负数时翻盘）
- 答案 = 全程 max(res, cur_max)（子数组可以以任意位置结尾）
- ⚡ 注意：cur_min 计算要用更新前的 cur_max（旧值），别先覆盖
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        dp_max = nums[0]
        dp_min = nums[0]
        for i in range(1, len(nums)):
            result1 = dp_max * nums[i]          # 乘上前一段最大
            result2 = dp_min * nums[i]          # 乘上前一段最小（负数翻盘的关键）
            result = max(nums[i], result1, result2, result)   # 全局答案
            dp_max = max(nums[i], result1, result2)           # 更新双状态（旧值同时用）
            dp_min = min(nums[i], result1, result2)
        return result


# ===== 参考：一维 DP 数组版（用户 17:56 第一版，思路更直白） =====
class SolutionArray:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        result = nums[0]
        dp_max = [nums[0]] * (length + 1)
        dp_min = [nums[0]] * (length + 1)
        for i in range(1, length):
            result1 = dp_max[i - 1] * nums[i]
            result2 = dp_min[i - 1] * nums[i]
            result = max(nums[i], result1, result2, result)
            dp_max[i] = max(nums[i], result1, result2)
            dp_min[i] = min(nums[i], result1, result2)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))     # 6
    print(s.maxProduct([-2, 0, -1]))       # 0
    print(s.maxProduct([-2, 3, -4]))       # 24（负负得正关键例）