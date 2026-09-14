# Created by Chono-Hina at 2026/09/14 17:29
# leetgo: 1.4.18
# https://leetcode.cn/problems/binary-tree-inorder-traversal/

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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.scan_tree(root, result)
        return result

    def scan_tree(self, root, result):
        if root:
            self.scan_tree(root.left, result)
            result.append(root.val)
            self.scan_tree(root.right, result)
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().inorderTraversal(root)
    print("\noutput:", serialize(ans, "integer[]"))
