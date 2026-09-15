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
        某个节点为根节点的最大路径：
        自身、自身+左节点最大、自身+右节点最大
        自身 + max(左节点最大,0) + max(右节点最大,0)
        对于这个节点，能组成最大的，以及上报给父节点的不是同一个数
        """
        max_list = [float("-inf")]
        def fun(root):
            if root:
                max_left = max(fun(root.left), 0)        # 左贡献（负数砍掉）
                max_right = max(fun(root.right), 0)      # 右贡献（负数砍掉）
                now_max = root.val + max_left + max_right      # 两腿：更新全局答案
                to_father = root.val + max(max_left, max_right)  # 单腿：喂父节点
                max_list[0] = max(max_list[0], now_max)
                return to_father
            return 0
        fun(root)
        return max_list[0]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxPathSum(root)
    print("\noutput:", serialize(ans, "integer"))
