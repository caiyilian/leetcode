# Created by Chono-Hina at 2026/09/14 19:41
# leetgo: 1.4.18
# https://leetcode.cn/problems/invert-binary-tree/

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def fun(root):
            if root:
                root.left, root.right = fun(root.right), fun(root.left)  # 元组赋值交换
                return root

        fun(root)
        return root
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().invertTree(root)
    print("\noutput:", serialize(ans, "TreeNode"))
