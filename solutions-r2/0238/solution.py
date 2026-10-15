"""238. 除自身以外数组的乘积（二刷）——前缀积 + 滚动后缀积（O(1) 额外空间）

用户 AC 版（2026-10-15 23:03 提交 755093333）
核心：输出数组当"前缀积"用（结果集不算额外空间），反向遍历时用一个变量滚动存后缀积。
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # 第一趟（左→右）：result[i] = 前缀积 nums[0..i-1]
        result = [1]
        for i in range(length - 1):
            result.append(result[-1] * nums[i])   # result = [1, 1, 2, 6]（[1,2,3,4] 为例）
        # 第二趟（右→左）：R 滚动存后缀积，直接乘进 result
        R = 1                                     # 当前后缀积（i 右边的乘积）
        for i in range(length):
            result[length - i - 1] *= R           # 前缀积 × 后缀积 = 答案
            R *= nums[length - i - 1]             # 后缀积滚一个位置
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))          # [24,12,8,6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))     # [0,0,9,0,0]
    print(s.productExceptSelf([1, 0]))                # [0,1]