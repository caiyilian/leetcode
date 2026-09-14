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
        if not root:
            return True          # ⚡ 空树是 True（天然对称）
        return self.fun(root.left, root.right)

    def fun(self, tree1, tree2):
        if tree1 and tree2:
            if tree1.val != tree2.val:
                return False
            # 交叉比较：左 vs 右、右 vs 左（镜像的定义）
            return self.fun(tree1.left, tree2.right) and self.fun(tree1.right, tree2.left)
        return tree1 is tree2    # 都 None → True；一个 None → False
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isSymmetric(root)
    print("\noutput:", serialize(ans, "boolean"))
