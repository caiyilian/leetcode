# Created by Chono-Hina at 2026/09/14 20:06
# leetgo: 1.4.18
# https://leetcode.cn/problems/symmetric-tree/

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        一开始root.left.val == root.right.val
        """
        def fun(tree1, tree2):
            if tree1 or tree2:
                if (tree1 is None) or (tree2 is None) or (tree1.val != tree2.val):
                    return False
                result1 = fun(tree1.left, tree2.right)      # 左 ↔ 右
                if result1 is False:
                    return False
                result2 = fun(tree1.right, tree2.left)      # 右 ↔ 左
                return result2
            return True

        return fun(root, root)      # ★ 空树也正确（fun(None,None) → True）
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)
    print("\noutput:", serialize(ans, "boolean"))
