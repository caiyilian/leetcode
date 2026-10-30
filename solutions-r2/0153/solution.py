"""153. 寻找旋转排序数组中的最小值（二刷）——二分找断点（O(logn)/O(1) 标准解）

用户 AC 版（2026-10-30 21:02 提交 757826866，一次通过，0ms/19.3MB）
- ⚡ 只比 nums[mid] 和 nums[right]：mid 在大段（nums[mid] > nums[right]）→ 最小在右，mid 可排除 left=mid+1
-                          mid 在小段（nums[mid] <= nums[right]）→ 最小可能是 mid 自己 → right=mid（别 mid-1！）
- while left < right（不是 <=），最后 nums[left] 即最小值
- 与 33 的区别：33 想 target 在哪个有序半段；153 只用"最小值在哪边"一个比较，分支只有 2 个
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:   # mid 在大段 → 最小值必在右半（mid 也可排除）
                left = mid + 1
            else:                          # mid 在小段 → 最小值可能是 mid 本身
                right = mid               # ★ 必须保留 mid（别写 mid-1！）
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3, 4, 5, 1, 2]))        # 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    print(s.findMin([11, 13, 15, 17]))       # 11（未旋转）
    print(s.findMin([5]))                    # 5
    print(s.findMin([2, 1]))                 # 1