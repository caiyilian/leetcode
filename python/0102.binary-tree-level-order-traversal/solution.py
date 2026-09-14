# Created by Chono-Hina at 2026/09/14 21:22
# leetgo: 1.4.18
# https://leetcode.cn/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.fun(root, result)
        return result

    def fun(self, root, result, dep=1):
        if root:
            if len(result) < dep:
                result.append([])        # 遇到更深的层，先建空列表
            result[dep - 1].append(root.val)
            self.fun(root.left, result, dep + 1)
            self.fun(root.right, result, dep + 1)
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
