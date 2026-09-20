# Created by Chono-Hina at 2026/09/20 17:20
# leetgo: 1.4.18
# https://leetcode.cn/problems/sliding-window-maximum/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调队列（递减）：deque 存索引，队头恒为窗口最大值
        length = len(nums)
        arr = deque()               # 存索引，维护递减（队头最大）
        result = []
        # 初始化前 k 个
        for i in range(k):
            while arr and nums[i] > nums[arr[-1]]:   # 队尾比 nums[i] 小的都弹掉
                arr.pop()
            arr.append(i)
        result.append(nums[arr[0]])
        # 滑动窗口
        for i in range(1, length - k + 1):
            new = i - 1 + k
            while arr and nums[new] > nums[arr[-1]]:
                arr.pop()
            arr.append(new)
            if arr[0] < i:           # 队头超出窗口范围 → 弹出
                arr.popleft()        # deque 的 O(1)（list.pop(0) 是 O(n)）
            result.append(nums[arr[0]])
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
