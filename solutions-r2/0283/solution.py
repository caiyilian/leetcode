from typing import List

# @lc code=begin

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ===== 改进版：快慢指针（4 行，推荐）=====
        # j 永远指向"下一个非 0 该放的位置"；i 遇到非 0 就换到 j，j 前进
        # i == j 时交换是自己换自己（无操作），天然处理"前面没有 0"的情况
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        # ===== 用户二刷原版：双指针交换（语义等价）=====
        # p1 指向第一个 0 的位置；p2 向右扫找非 0，找到就与 p1 交换
        # length = len(nums)
        # p1 = p2 = 0
        # while True:
        #     while p2 < length and nums[p2] == 0:   # p2 跳过 0
        #         p2 += 1
        #     if p2 == length:                        # 到头没有非 0 → 结束
        #         break
        #     while p1 < p2 and nums[p1] != 0:        # p1 停在 0 上
        #         p1 += 1
        #     if p1 != p2:
        #         nums[p1], nums[p2] = nums[p2], nums[p1]
        #     p1 += 1
        #     p2 += 1


# @lc code=end

if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 0, 3, 12]; s.moveZeroes(a); print(a)   # [1,3,12,0,0]
    a = [0, 0, 1];       s.moveZeroes(a); print(a)    # [1,0,0]
    a = [1, 2, 3];       s.moveZeroes(a); print(a)    # [1,2,3]
    a = [];              s.moveZeroes(a); print(a)    # []