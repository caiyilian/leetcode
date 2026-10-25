# Created by Chono-Hina at 2026/09/15 20:22
# leetgo: 1.4.18
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        左树有，右树也有，那么当前节点就是其中一个祖先节点
        如果其中一个树有，另一个树没有，但是当前节点是其中一个，那么祖先节点就是当前节点
        如果两个树都没有，返回False
        """
        result = [None]

        def fun(root):
            if root:
                result_left = fun(root.left)
                result_right = fun(root.right)
                return_result = result_left + result_right
                if return_result == 2:                  # 左右子树各找到 p/q → 当前是 LCA
                    if result[0] is None:
                        result[0] = root
                else:                                   # 只有一侧找到
                    if (root is p) or (root is q):      # 自己是另一个目标
                        return_result += 1
                        if return_result == 2:
                            result[0] = root
                return return_result
            return 0

        fun(root)
        return result[0]


# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
