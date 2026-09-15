# Created by Chono-Hina at 2026/09/15 10:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/validate-binary-search-tree/

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        中序遍历，就是左根右，如果上一个值大于当前值，就出错
        """
        last_list = [float('-inf')]
        def fun(tree_root):
            if tree_root:
                left_bool = fun(tree_root.left)
                if tree_root.val > last_list[0]:
                    last_list[0] = tree_root.val
                else:
                    return False
                if left_bool is False:
                    return False
                right_bool = fun(tree_root.right)
                return right_bool
            return True
        result = fun(root)
        return result
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isValidBST(root)
    print("\noutput:", serialize(ans, "boolean"))
