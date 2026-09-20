# Created by Chono-Hina at 2026/09/20 16:45
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-the-duplicate-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # 快慢指针（Floyd 判圈）：数组当链表，nums[i] = i 指向的下一个节点
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:              # 第一阶段：找相遇点
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0                         # 第二阶段：slow 回起点
        while slow != fast:              # 同速走，再次相遇点 = 环入口 = 重复数
            slow = nums[slow]
            fast = nums[fast]
        return slow
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findDuplicate(nums)
    print("\noutput:", serialize(ans, "integer"))
