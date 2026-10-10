from typing import List

# @lc code=begin

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 二刷版：双指针两端收缩（O(n) 最优解）
        # 核心：容量 = 距离 × 矮边高度 → 矮的那边才有机会变大，动矮边
        left, right = 0, len(height) - 1
        max_storage = 0
        while left < right:
            if height[left] < height[right]:
                now_storage = (right - left) * height[left]   # 左边矮 → 以左高为水位
                left += 1                                     # 动矮边（左移右）
            else:
                now_storage = (right - left) * height[right]  # 右边矮（或相等）→ 以右高为水位
                right -= 1                                    # 动矮边（右移左）
            max_storage = max(max_storage, now_storage)
        return max_storage


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))   # 49
    print(s.maxArea([1, 1]))                        # 1
    print(s.maxArea([4, 3, 2, 1, 4]))               # 16
    print(s.maxArea([2, 3, 4, 5, 18, 17, 6]))       # 17