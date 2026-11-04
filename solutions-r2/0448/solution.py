"""448. 找到所有数组中消失的数字（二刷）——归位法（用户 AC 版）

用户二刷（2026-11-04 11:43 提交 758534018，AC 一次通过，71ms/30.6MB）
- 归位法（数组即哈希表）：值 v 应放在下标 v-1；把每个元素换到"它该在的位置"
- 交换条件合并写：while nums[i] != (i+1) and nums[i] != nums[nums[i]-1]
  （第二个条件 = 目标位置已是正确值，说明重复，停止交换）
- 最后 nums[i] != i+1 的下标 i → 缺失数字 i+1
- 允许修改原数组（与 287 不同），O(n)/O(1) 满足进阶要求
"""

from typing import List


# ===== 用户 AC 版（归位法） =====
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            # ⚡ 两个条件合并：没归位 + 目标位不是正确值（避免重复死循环）
            while nums[i] != (i + 1) and nums[i] != nums[nums[i] - 1]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]
        result = []
        for i in range(length):
            if nums[i] != (i + 1):       # 该位置的值错了 → i+1 缺失
                result.append(i + 1)
        return result


# ===== 参考：负数标记法（另一种 O(1) 空间技巧） =====
class SolutionMark:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]   # 把"出现过"的位置标负
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    s = Solution()
    print(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))    # [5,6]
    print(s.findDisappearedNumbers([1, 1]))                       # [2]
    print(s.findDisappearedNumbers([3, 3, 3]))                    # [1,2]