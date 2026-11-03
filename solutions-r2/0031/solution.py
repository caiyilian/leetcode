"""31. 下一个排列（二刷）——字典序三步骤（用户 AC 版）

用户二刷（2026-11-03 3 次提交演进）：v1 WA（19:42，等号边界错）→ v2 AC（19:44，sorted 收尾、
自觉不满足 O(1) 空间）→ v3 AC（19:45，758442541，双指针反转收尾，O(1) 空间 ✅，0ms/19.3MB）

核心三步：
① 从右往左找第一个升序对 nums[i-1] < nums[i]（i = 分界点）
② 在右侧降序段找"最小的大于 nums[i-1] 的数"交换（⚡ 找第一个 <= 的前一个，等号边界要 <=）
③ 反转 nums[i:]（降序 → 升序，得到"恰好下一个"）
全降序（无升序对）→ 整个数组变最小（反转=升序）。
"""

from typing import List


# ===== 用户 AC 版（v3，原样主逻辑 + 注释） =====
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        index = length - 1
        while index > 0:
            if nums[index - 1] < nums[index]:        # ① 找到升序对（分界点 index-1）
                # ② 在右侧降序段找"最小的大于 nums[index-1] 的数"
                #    （右侧降序 → 从右往左扫，第一个 <= x 的前一个就是目标）
                for i in range(index + 1, length):
                    if nums[i] <= nums[index - 1]:   # ⚡ 必须 <=（跳过相等，v1 WA 的坑）
                        nums[index - 1], nums[i - 1] = nums[i - 1], nums[index - 1]
                        break
                else:
                    # 右侧全大于 x → 最小的在末尾（降序最右端）
                    nums[index - 1], nums[-1] = nums[-1], nums[index - 1]
                # ③ 反转 nums[index:]（降序 → 升序）：双指针 O(1) 空间
                left = index
                right = length - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                break                                # 完成，跳出 while
            index -= 1
        else:                                        # 没找到升序对 = 全降序
            nums.reverse()                           # ⚡ 反转即升序（最小排列），
                                                     #    nums.sort() 会占 O(n) 空间，reverse() 严格 O(1)


# ===== 参考：标准三步（更简洁，面试推荐背） =====
class SolutionStd:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:        # ① 找第一个"左 < 右"的位置 i
            i -= 1
        if i >= 0:                                      # ② 右侧从右找第一个 > nums[i] 的 j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = reversed(nums[i + 1:])           # ③ 反转右侧（升序）


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3]; s.nextPermutation(a); print(a)    # [1,3,2]
    a = [3, 2, 1]; s.nextPermutation(a); print(a)    # [1,2,3]（回到最小）
    a = [1, 1, 5]; s.nextPermutation(a); print(a)    # [1,5,1]