# Created by Chono-Hina at 2026/09/25 20:59
# leetgo: 1.4.18
# https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        # 双指针扫描（O(n)）：找最后一个"小于左边最大值"(r) 和 最后一个"大于右边最小值"(l)
        # ★ 比较必须带 = （>= / <=），否则相等元素被漏掉（如 [1,3,2,2,2]）
        length = len(nums)
        max_l = nums[0]
        l = None
        r = None
        for i in range(1, length):          # 从左往右：找右边界
            if nums[i] >= max_l:
                max_l = nums[i]
            else:
                r = i                        # 最后一个"小于左边最大值"的位置
        if r is None:
            return 0
        min_r = nums[-1]
        for i in range(1, length):          # 从右往左：找左边界
            if nums[length - 1 - i] <= min_r:
                min_r = nums[length - 1 - i]
            else:
                l = length - 1 - i           # 最后一个"大于右边最小值"的位置
        return max(0, r - l + 1)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findUnsortedSubarray(nums)
    print("\noutput:", serialize(ans, "integer"))
