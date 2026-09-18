# Created by Chono-Hina at 2026/09/18 11:26
# leetgo: 1.4.18
# https://leetcode.cn/problems/kth-largest-element-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快速选择（三路分区版，用户自写）：随机 pivot，分 >/==/< 三路，只递归一边
        from random import choice

        def fast_choose(nums, k):
            pivot = choice(nums)                    # 随机化防退化
            left, middle, right = [], [], []        # > pivot / == pivot / < pivot
            for n in nums:
                if n > pivot:
                    left.append(n)
                elif n < pivot:
                    right.append(n)
                else:
                    middle.append(n)
            if len(left) >= k:                      # 第 k 大在 left（>pivot 的那堆）
                return fast_choose(left, k)
            elif len(left) + len(middle) >= k:      # 第 k 大恰好 == pivot
                return pivot
            else:                                   # 第 k 大在 right（<pivot 的那堆）
                return fast_choose(right, k - len(left) - len(middle))

        return fast_choose(nums, k)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthLargest(nums, k)
    print("\noutput:", serialize(ans, "integer"))
