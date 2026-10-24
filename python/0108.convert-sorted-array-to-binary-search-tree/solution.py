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
        """
        平衡：左右两个数深度相差不超过1
        搜索树，左树全都小于当前节点
        """
        if not nums:
            return None
        length = len(nums)

        def fun(start, end):
            middle = (end - start) // 2 + start      # 中点：左半比右半多0/1个 → 平衡
            root = TreeNode(nums[middle])
            left_num = middle - start
            right_num = end - middle - 1
            if left_num > 0:
                root.left = fun(start, middle)
            if right_num > 0:
                root.right = fun(middle + 1, end)
            return root

        return fun(0, length)
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedArrayToBST(nums)
    print("\noutput:", serialize(ans, "TreeNode"))
