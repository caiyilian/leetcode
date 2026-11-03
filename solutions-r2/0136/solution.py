"""136. 只出现一次的数字（二刷）——异或（用户 AC 版）

用户二刷（2026-11-03 22:24 提交 758478960，AC 一次通过，0ms/20.7MB）
- 异或三条性质：① a^a=0（相同抵消）② a^0=a ③ 交换律/结合律
- 全部数异或 → 成对的抵消为 0，剩下的就是单身数字
- 进阶要求：线性时间 O(n) + 常数空间 O(1) —— 异或是唯一同时满足的解
"""

from typing import List


# ===== 用户 AC 版（异或） =====
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]      # a^a=0，成对抵消，剩单身
        return result


# ===== 参考：等价写法（从 0 起 xor，更通用） =====
class SolutionAlt:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2, 2, 1]))        # 1
    print(s.singleNumber([4, 1, 2, 1, 2]))  # 4
    print(s.singleNumber([1]))              # 1