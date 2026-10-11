from typing import List

# @lc code=begin

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 二刷版：排序 + 固定 i + 双指针夹逼（O(n²) 最优，去重三处齐全）
        results = []
        nums.sort()                        # 排序：让双指针夹逼成为可能 + 重复元素相邻
        length = len(nums)
        last = float('inf')
        for i in range(length - 1):
            target = -nums[i]              # 剩下两数要找的和
            if target == last:             # 去重 i：target 相同 = nums[i] 相同 → 跳过
                continue
            last = target
            left, right = i + 1, length - 1
            while left < right:
                left_val, right_val = nums[left], nums[right]
                if left_val + right_val < target:
                    left += 1              # 太小 → 左指针右移（和变大）
                elif left_val + right_val > target:
                    right -= 1             # 太大 → 右指针左移（和变小）
                else:
                    results.append([-target, left_val, right_val])
                    left += 1
                    right -= 1
                    # 去重 l 和 r：跳过与刚记录相同的值
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
        return results


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1,-1,2],[-1,0,1]]
    print(s.threeSum([0, 1, 1]))               # []
    print(s.threeSum([0, 0, 0]))               # [[0,0,0]]
    print(s.threeSum([-2, 0, 1, 1, 2]))        # [[-2,0,2],[-2,1,1]]