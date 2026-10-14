"""41. 缺失的第一个正数（二刷）——归位法（数组即哈希表）

用户 AC 版（2026-10-14 15:24 提交 754762673，一次通过）
核心：值 v 应放在下标 v-1；交换归位 O(n)，再扫一遍找第一个"对不上"的。
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 归位：把值 [1, n] 内的数放到下标 v-1 处
        for i in range(n):
            while (nums[i] != (i + 1)) and (1 <= nums[i] <= n) and (nums[i] != nums[nums[i] - 1]):
                target_index = nums[i] - 1
                # ★ 必须先冻结 target_index 再交换！
                # 直接写 nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] 会死循环：
                # Python 元组交换左侧下标从左到右求值，第二步时 nums[i] 已是新值 → 下标被污染
                nums[i], nums[target_index] = nums[target_index], nums[i]
        # 找第一个对不上的位置
        for i in range(n):
            if nums[i] != (i + 1):
                return i + 1
        return n + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))       # 3
    print(s.firstMissingPositive([3, 4, -1, 1]))   # 2
    print(s.firstMissingPositive([7, 8, 9, 11, 12]))  # 1
    print(s.firstMissingPositive([1, 2, 3, 4]))    # 5