# Created by Chono-Hina at 2026/09/25 17:23
# leetgo: 1.4.18
# https://leetcode.cn/problems/convert-bst-to-greater-tree/

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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = [0]                  # 已累加的"更大值"总和（闭包共享）

        def fun(root):
            if root:
                fun(root.right)    # 反中序：先右（更大的）
                acc[0] += root.val
                root.val = acc[0]  # 当前值 = 累计和（含自己）
                fun(root.left)     # 再左（更小的）
        fun(root)
        return root
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().convertBST(root)
    print("\noutput:", serialize(ans, "TreeNode"))
