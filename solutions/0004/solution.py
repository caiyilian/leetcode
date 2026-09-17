# Created by Chono-Hina at 2026/09/17 16:09
# leetgo: 1.4.18
# https://leetcode.cn/problems/median-of-two-sorted-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m <= n:
            small, big = nums1, nums2
        else:
            small, big = nums2, nums1
            m, n = n, m
        num_half = (m + n + 1) // 2          # 左半元素总数（奇数左多 1）
        left, right = 0, m
        while left <= right:                 # 闭区间：i=m 可取（一个数组可能为空）
            i = (left + right) // 2          # i = small 左半元素个数（数量语义！）
            j = num_half - i                 # big 左半元素个数（自动跟随）
            # 四个边界值（显式哨兵，免疫负索引/越界）
            L1 = small[i - 1] if i > 0 else float('-inf')
            L2 = big[j - 1] if j > 0 else float('-inf')
            R1 = small[i] if i < m else float('inf')
            R2 = big[j] if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:        # 切割合法：左半全部 ≤ 右半
                if (m + n) % 2:
                    return max(L1, L2)                       # 奇数：左半最大
                return (max(L1, L2) + min(R1, R2)) / 2       # 偶数：左max + 右min
            if L1 > R2:
                right = i - 1                # small 左半取多了 → i 减小
            else:
                left = i + 1                 # small 左半取少了 → i 增大
        

# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "double"))
