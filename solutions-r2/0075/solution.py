"""75. 颜色分类（二刷）——荷兰国旗三指针（用户 AC 版）进阶 O(1)/单遍

用户二刷（2026-11-03 22:09 提交 758475933，AC 一次通过，0ms/19.4MB）
- 进阶要求：一趟扫描 + 常数空间 → 三指针荷兰国旗法
- 三区不变量：[0,zero_bound) 全0｜[zero_bound,i) 全1｜(two_bound,末尾] 全2｜[i,two_bound] 未扫
- 用户两个微优化：①预处理跳过首部连续0/尾部连续2 ②换2后 while 跳过连续 2
- 完成条件：i 越过 two_bound（2 区已终态，不需要扫进去）
"""

from typing import List


# ===== 用户 AC 版（带预处理 + 跳过连续 2 优化） =====
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        zero_bound = 0                                  # 0 区右边界（该处不是 0）
        two_bound = length - 1                          # 2 区左边界（该处不是 2）
        # ⚡ 优化①：预处理跳过首部连续 0 / 尾部连续 2，减少主循环
        while zero_bound < length and nums[zero_bound] == 0:
            zero_bound += 1
        while two_bound >= 0 and nums[two_bound] == 2:
            two_bound -= 1
        i = zero_bound
        while i <= two_bound:
            if nums[i] == 1:
                i += 1
                continue
            if nums[i] == 2:
                # 换 2：换来的数没检查过 → i 不动（三指针灵魂）
                nums[i], nums[two_bound] = nums[two_bound], nums[i]
                two_bound -= 1
                # ⚡ 优化②：换完立即跳过连续 2（等价但少几轮循环）
                while nums[two_bound] == 2:
                    two_bound -= 1
                continue
            if nums[i] == 0:
                nums[i], nums[zero_bound] = nums[zero_bound], nums[i]
                zero_bound += 1
                i += 1


# ===== 参考：标准三指针（教科书版，面试推荐背） =====
class SolutionStd:
    def sortColors(self, nums: List[int]) -> None:
        left, i, right = 0, 0, len(nums) - 1
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:                                       # == 2
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1                              # i 不动！换来的还没检查


if __name__ == "__main__":
    s = Solution()
    a = [2, 0, 2, 1, 1, 0]; s.sortColors(a); print(a)   # [0,0,1,1,2,2]
    a = [2, 0, 1]; s.sortColors(a); print(a)            # [0,1,2]
    a = [2, 2, 2]; s.sortColors(a); print(a)            # [2,2,2]
    a = [1, 2, 0]; s.sortColors(a); print(a)            # [0,1,2]