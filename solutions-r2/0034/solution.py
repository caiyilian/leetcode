"""34. 在排序数组中查找元素的第一个和最后一个位置（二刷）——二分左右边界（O(logn)/O(1) 标准解）

用户 AC 版（2026-10-30 14:40 提交 757761608，一次通过，0ms/20.2MB）
- 三个二分：① 确认 target 存在（for-else 不存在返回 [-1,-1]）
- ② 用假想值 target-0.5 二分 → start = 第一个 >= target 的下标（35 的 return left）
- ③ 用假想值 target+0.5 二分 → end = 最后一个 <= target 的下标
- ⚡ ±0.5 技巧：把"找边界"化为"找插入位置"，整数数组天然免疫（没有等于 target±0.5 的元素）
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:                     # ① 确认存在
            mid = (left + right) // 2
            if nums[mid] == target:
                break
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        else:
            return [-1, -1]                      # 不存在

        # ② 左边界：找第一个 >= target 的位置（假想 target-0.5）
        left, right = 0, length - 1
        target1 = target - 0.5
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target1:
                left = mid + 1
            else:
                right = mid - 1
        start = left

        # ③ 右边界：找最后一个 <= target 的位置（假想 target+0.5）
        right = length - 1
        target2 = target + 0.5
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target2:
                left = mid + 1
            else:
                right = mid - 1
        end = left

        return [start, end - 1]                  # end 是第一个 > target 的 → -1


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))   # [3, 4]
    print(s.searchRange([5, 7, 7, 8, 8, 10], 6))   # [-1, -1]
    print(s.searchRange([], 0))                    # [-1, -1]
    print(s.searchRange([7, 7, 7], 7))             # [0, 2]