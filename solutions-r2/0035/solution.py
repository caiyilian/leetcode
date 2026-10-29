"""35. 搜索插入位置（二刷）——二分查找左闭右闭模板（O(logn)/O(1) 标准解）⚡机考二分母题

用户 AC 版（2026-10-29 22:29 提交 757689694，一次通过，0ms/19.8MB）
- 本质：找"第一个 >= target 的位置"（bisect_left）
- 左闭右闭模板：while left <= right；命中返回 mid；否则 right=mid-1 / left=mid+1
- 退出时 left = 第一个 >= target 的位置（含越界）→ 直接返回 left
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left                 # ★ 退出时 left 就是插入位置


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))    # 2
    print(s.searchInsert([1, 3, 5, 6], 2))    # 1
    print(s.searchInsert([1, 3, 5, 6], 7))    # 4（越界后）
    print(s.searchInsert([1, 3, 5, 6], 0))    # 0（最前）
    print(s.searchInsert([], 5))              # 0（空数组）