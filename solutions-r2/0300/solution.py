"""300. 最长递增子序列（二刷）——进阶 O(n log n) 手写二分（用户 AC 版）

用户二刷（2026-11-01 两版演进）：
- 20:12 AC O(n²) DP（758078932，1239ms）——标准解法一，正确但慢
- 21:15 AC 进阶 O(n log n)（758090378，11ms）——手写二分 + tails"最小尾巴"数组（本文件主解）
- ⚡ 中间 21:01 WA（758087678）：只替换 tails[-1] 破坏单调性（[4,10,4,3,8,9] → tails 变 [4,4] 非严格递增）
- 必须二分找"第一个 >= x 的位置"替换，维护 tails 严格递增 → 有序才能二分 → O(n log n)

方法本质：tails[k] = 长度 k+1 的递增子序列的最小末尾；替换不改变长度但让尾巴更小，给未来留空间
"""

from typing import List


# ===== 用户进阶 AC 版（手写二分，O(n log n)/O(n)） =====
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        tails = [nums[0]]
        for i in range(1, length):
            if nums[i] > tails[-1]:          # 比所有尾巴都大 → 新长度
                tails.append(nums[i])
            else:
                # 手写二分：找第一个 >= nums[i] 的位置并替换（== 时 break 短路）
                left, right = 0, len(tails)
                while left <= right:
                    mid = (left + right) // 2
                    if tails[mid] == nums[i]:
                        break
                    if tails[mid] > nums[i]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    tails[left] = nums[i]    # for-else：循环未 break（未命中）→ 替换
        return len(tails)


# ===== 标准解法一：O(n²) DP（用户 20:12 AC 版） =====
class SolutionDP:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [1] * length                    # dp[i] = 以 i 结尾的最长递增子序列
        result = 0
        for i in range(length):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
            result = max(result, dp[i])
        return result


# ===== 参考：bisect 标准写法（面试可更简洁） =====
class SolutionBisect:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        tails = []
        for x in nums:
            i = bisect.bisect_left(tails, x)     # 第一个 >= x
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
        return len(tails)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))           # 4
    print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))        # 1
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))          # 3（3,8,9）