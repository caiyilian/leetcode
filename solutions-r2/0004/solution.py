"""4. 寻找两个正序数组的中位数（二刷·困难）——二分短数组切分（O(log min(m,n))/O(1) 最优解）

用户 AC 版（2026-10-31 15:49 提交 757905102，一次通过，0ms/19.5MB）
- 核心：只在短数组（nums1）上二分切分点 i，nums2 的切分点 j = k - i 由总数自动算出
- k = (m+n+1)//2：左半元素总数（奇数时左半多 1 个，天然覆盖中位数）
- 平衡条件：左半最大值 <= 右半最小值（两个交叉条件）；越界用 ±inf 占位
- ⚡ 用户观察：本实现 while 永远不会自然退出（right=i 保留候选 + 平衡点唯一）→ 均在 else return

也可以：right = i - 1 的标准二分（见 SolutionStd 参考）
"""

from typing import List


# ===== 用户 AC 版（right = i 保留候选） =====
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)     # 短的
        n = len(nums2)     # 长的
        if m > n:          # 保证在短数组上二分
            nums1, nums2 = nums2, nums1
            m, n = n, m

        half_length = (m + n + 1) // 2   # 左半（含中位数侧）元素总数
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2      # nums1 左半取 i 个
            j = half_length - i          # nums2 左半取 j 个（由总数自动约束）

            left_num1 = nums1[i - 1] if i - 1 >= 0 else float('-inf')
            left_num2 = nums2[j - 1] if j - 1 >= 0 else float('-inf')
            right_nums1 = nums1[i] if i < m else float('inf')
            right_nums2 = nums2[j] if j < n else float('inf')

            if left_num1 > right_nums2:      # nums1 切大了 → 往左移
                right = i
            elif left_num2 > right_nums1:    # nums1 切小了 → 往右移
                left = i + 1
            else:                            # 平衡：左半最大 <= 右半最小
                if (m + n) % 2 == 0:         # 偶数 → 中间两个取平均
                    return (max(left_num1, left_num2) + min(right_nums1, right_nums2)) / 2
                else:                        # 奇数 → 左半最大值即中位数
                    return max(left_num1, left_num2)


# ===== 标准二分版参考（right = i - 1，写法更常规） =====
class SolutionStd:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            a_left = nums1[i - 1] if i > 0 else float('-inf')
            b_left = nums2[j - 1] if j > 0 else float('-inf')
            a_right = nums1[i] if i < m else float('inf')
            b_right = nums2[j] if j < n else float('inf')
            if a_left > b_right:
                hi = i - 1
            elif b_left > a_right:
                lo = i + 1
            else:
                if (m + n) % 2:
                    return max(a_left, b_left)
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
        raise ValueError("unreachable")


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))              # 2.0
    print(s.findMedianSortedArrays([1, 2], [3, 4]))           # 2.5
    print(s.findMedianSortedArrays([], [1]))                  # 1.0
    print(s.findMedianSortedArrays([1, 1, 1], [1, 1, 1]))     # 1.0