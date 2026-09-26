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
        # 原地合并到 root1，三种情况：
        # ① 都不为 None：值相加，递归合并左右子树
        # ② 只有 root2：直接采用 root2
        # ③ 只有 root1：保持 root1（return root1）
        def fun(root1, root2):
            if root1 and root2:                # 都不为 None
                root1.val += root2.val
                root1.left = fun(root1.left, root2.left)
                root1.right = fun(root1.right, root2.right)
            elif root2:                        # root2 不为 None，root1 为 None
                root1 = root2
            return root1

        root1 = fun(root1, root2)              # ★ 必须接住返回值（内部 root1=root2 是局部绑定）
        return root1
        

# @lc code=end

if __name__ == "__main__":
    root1: TreeNode = deserialize("TreeNode", read_line())
    root2: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().mergeTrees(root1, root2)
    print("\noutput:", serialize(ans, "TreeNode"))
