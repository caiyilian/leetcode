# Created by Chono-Hina at 2026/09/15 10:56
# leetgo: 1.4.18
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.fun(nums)

    def fun(self, nums):
        if not nums:
            return None
        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])
        root.left = self.fun(nums[:middle_index])
        root.right = self.fun(nums[middle_index + 1:])   # Python 切片越界自动截断，不会崩
        return root
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedArrayToBST(nums)
    print("\noutput:", serialize(ans, "TreeNode"))
