# Created by Chono-Hina at 2026/09/20 16:08
# leetgo: 1.4.18
# https://leetcode.cn/problems/next-permutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        # 下一个排列：从右找升序对 → 交换"最小的大于它的数" → 反转后半段
        length = len(nums)
        for i in range(length):
            index = length - 1 - i
            if index < length - 1 and nums[index] < nums[index + 1]:
                # 右边降序，找"最小的大于 nums[index] 的数"
                for j in range(index + 1, length):
                    if nums[j] <= nums[index]:   # ★ 必须有 =（右边可能含相等元素）
                        nums[index], nums[j - 1] = nums[j - 1], nums[index]
                        break
                else:
                    nums[index], nums[length - 1] = nums[length - 1], nums[index]
                break
        else:
            index = -1     # 完全降序：无升序对
        # 反转 index+1 到末尾（变升序）
        left, right = index + 1, length - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().nextPermutation(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))
