# Created by Chono-Hina at 2026/09/14 21:47
# leetgo: 1.4.18
# https://leetcode.cn/problems/diameter-of-binary-tree/

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_list = [0]
        self.fun(root, max_list)
        return max_list[0]

    def fun(self, root, max_list):
        if root:
            left_dep = self.fun(root.left, max_list)
            right_dep = self.fun(root.right, max_list)
            # 职责①：两腿相加 = 经过当前节点的直径，更新全局答案
            max_list[0] = max(left_dep + right_dep, max_list[0])
            # 职责②：返回单腿深度（供父节点继续往上拼）——返回值 ≠ 答案！
            return max(left_dep, right_dep) + 1
        # 是 None，深度 0
        return 0
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().diameterOfBinaryTree(root)
    print("\noutput:", serialize(ans, "integer"))
