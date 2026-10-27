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
        """
        每一个树的最长，等于左树上传+右树上传
        而这个树的最长，与上传，是不同的，
        上传只取最长的那颗树加1
        """
        result = [0]               # 全局答案：最长路径边数

        def fun(root):
            if root:
                left = fun(root.left)
                right = fun(root.right)
                result[0] = max(result[0], left + right)   # 两腿：过当前节点的路径 = 左链+右链
                return max(left, right) + 1                # 单腿：喂父节点（最长单链高度）
            return 0

        fun(root)
        return result[0]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().diameterOfBinaryTree(root)
    print("\noutput:", serialize(ans, "integer"))
