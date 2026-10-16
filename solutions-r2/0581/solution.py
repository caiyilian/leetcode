"""581. 最短无序连续子数组（二刷）——双向扫描（O(n)/O(1) 最优解）

用户 AC 版（2026-10-16 10:25 提交 755129199，一次通过）
核心：找最后一个"小于左边最大值"的位置（右边界）+ 最后一个"大于右边最小值"的位置（左边界）。
"""

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        # 第一趟（左→右）：找最后一个乱序点 = 区间的右边界
        left = None
        max_left = float('-inf')
        for i in range(length):
            if nums[i] < max_left:     # 小于历史最大值 → 乱序点
                left = i
            else:
                max_left = nums[i]     # 相等也算"达标"（>= 语义），不触发更新
        if left is None:               # 单调递增 → 全有序
            return 0
        # 第二趟（右→左）：找最后一个乱序点 = 区间的左边界
        right = None
        max_right = float('inf')
        for i in range(length):
            if nums[length - i - 1] > max_right:   # 大于历史最小值 → 乱序点
                right = length - i - 1
            else:
                max_right = nums[length - i - 1]
        return left - right + 1        # 右边界 - 左边界 + 1（不是反过来！）


if __name__ == "__main__":
    s = Solution()
    print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))   # 5
    print(s.findUnsortedSubarray([1, 2, 3, 4]))              # 0
    print(s.findUnsortedSubarray([2, 1]))                    # 2
    print(s.findUnsortedSubarray([1, 3, 2, 2, 2]))           # 4