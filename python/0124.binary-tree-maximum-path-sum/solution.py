# Created by Chono-Hina at 2026/09/15 21:07
# leetgo: 1.4.18
# https://leetcode.cn/problems/binary-tree-maximum-path-sum/

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
    def maxPathSum(self, root: TreeNode | None) -> int:
        """
        某一个节点，它的最大，等于左节点向上传的和右节点向上传的加上自身
        然后它向上传的是自身加上非负的子节点
        """
        result = [float('-inf')]

        def fun(root):
            if root:
                left_max = max(fun(root.left), 0)     # 左单腿贡献（负数不选 → 0）
                right_max = max(fun(root.right), 0)   # 右单腿贡献
                result[0] = max(result[0], root.val + left_max + right_max)  # 两腿=过根路径
                return root.val + max(left_max, right_max)  # 单腿喂父
            return 0

        fun(root)
        return result[0]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxPathSum(root)
    print("\noutput:", serialize(ans, "integer"))
