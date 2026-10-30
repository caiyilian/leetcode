"""33. 搜索旋转排序数组（二刷）——旋转数组二分：先判有序半段再区间定位（O(logn)/O(1) 标准解）

标准 AC 版（官方写法，推荐）——2026-10-30 15:52 用户提交 757777147 AC
- 核心：mid 分割后，左半或右半必有一半是有序的 → 判断 target 是否在该有序半段内
- 若在 → 往该半段二分；不在 → 去另一半
- ⚡ 关键判断：nums[left] <= nums[mid] 左半有序；区间包含判断用 nums[left] <= target < nums[mid]
"""

from typing import List


# ===== 标准版（主解，官方写法） =====
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:              # 左半段有序
                if nums[left] <= target < nums[mid]: # target 在左半
                    right = mid - 1
                else:                                # 否则去右半
                    left = mid + 1
            else:                                    # 右半段有序
                if nums[mid] < target <= nums[right]:# target 在右半
                    left = mid + 1
                else:                                # 否则去左半
                    right = mid - 1
        return -1


# ===== 用户最终四分支 AC 版（757808201，正确但偏绕，留档对比） =====
class SolutionFourBranch:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                # 中间值大于target
                if nums[left] <= nums[mid]:
                    # 左半边是递增
                    if nums[left] <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    # 右边是递增,而mid又大于target，所以右边一定没有
                    right = mid - 1
            else:
                # 中间值小于target
                if nums[left] < nums[mid]:
                    # 左半是递增，左边只有比中间值小的，那么左边一定没有
                    left = mid + 1
                else:
                    # 右边递增
                    if nums[right] >= target:
                        # 在右边
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))    # 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))    # -1
    print(s.search([1], 0))                      # -1
    print(s.search([2, 1], 1))                   # 1