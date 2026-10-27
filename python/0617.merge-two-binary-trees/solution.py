# Created by Chono-Hina at 2026/09/26 14:37
# leetgo: 1.4.18
# https://leetcode.cn/problems/merge-two-binary-trees/

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
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        """
        统一加到root1
        如果两个都有的节点，相加
        如果左是None，右有节点，把右接入左，然后不用继续往下走
        如果左不是None，右是，那就不用继续往下走
        """
        if not root1:
            return root2

        def fun(root1, root2):
            if root1 and root2:
                root1.val += root2.val
                root1.left = fun(root1.left, root2.left)
                root1.right = fun(root1.right, root2.right)
                return root1
            else:
                return root1 if root1 else root2

        root1 = fun(root1, root2)
        return root1
        

# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().mergeTrees(root1, root2)
    print("\noutput:", serialize(ans, "TreeNode"))
