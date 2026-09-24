# Created by Chono-Hina at 2026/09/24 15:14
# leetgo: 1.4.18
# https://leetcode.cn/problems/house-robber-iii/

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
    def rob(self, root: TreeNode | None) -> int:
        # 树形 DP：返回 (偷当前节点的最大值, 不偷当前节点的最大值)
        def fun(root):
            if root:
                rob_left, no_rob_left = fun(root.left)
                rob_right, no_rob_right = fun(root.right)
                # 偷当前节点 → 左右孩子都不能偷
                rob_now = root.val + no_rob_left + no_rob_right
                # 不偷当前节点 → 左右孩子可偷可不偷，各取最大
                no_rob_now = max(rob_left, no_rob_left) + max(rob_right, no_rob_right)
                return rob_now, no_rob_now
            return (0, 0)   # 空节点：偷与不偷都是 0
        rob_now, no_rob_now = fun(root)
        return max(rob_now, no_rob_now)

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().rob(root)
    print("\noutput:", serialize(ans, "integer"))
