"""189. 轮转数组（二刷）——三次反转（O(1) 空间最优解）

用户 AC 版（2026-10-15 18:06 提交 755031348）
演进：块交换 WA/TLE ×2 → 三次反转 AC（详见 result.md）
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n                       # 先取模（防 k>n 和 k=0）
        nums[:] = nums[::-1]         # ① 整个反转
        nums[:k] = nums[:k][::-1]    # ② 前 k 个再反转
        nums[k:] = nums[k:][::-1]    # ③ 后 n-k 个再反转


if __name__ == "__main__":
    s = Solution()
    for nums, k, exp in [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
                         ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
                         ([1, 2], 3, [2, 1])]:
        s.rotate(nums, k)
        print(nums, '期望', exp, '✓' if nums == exp else '✗')