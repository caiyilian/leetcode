# Created by Chono-Hina at 2026/09/15 15:08
# leetgo: 1.4.18
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        先把左树搞定，返回左头尾两个指针
        然后搞定右，返回右头尾
        如果左头是None，那就直接合格了，返回根和右尾
        否则，把右头接入左尾巴，然后把左头接入根节点的右
        然后return根和右尾
        如果是叶子节点，那么返回的两个都是本身
        """
        def fun(root):
            if root:
                root.left, left_last = fun(root.left)
                root.right, right_last = fun(root.right)
                if root.left:
                    left_last.right = root.right
                    root.right = root.left
                    root.left = None
                    if right_last is None:        # ★ 修复：右子树为空时，链尾=左链尾
                        right_last = left_last
                return root, right_last if (right_last is not None) else root
            return None, None

        fun(root)
        return root
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    Solution().flatten(root)
    ans = root
    print("\noutput:", serialize(ans, "TreeNode"))
