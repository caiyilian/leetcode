# Created by Chono-Hina at 2026/09/15 12:32
# leetgo: 1.4.18
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        def fun(root, k):
            if root:
                fun(root.left, k)
                if len(result) == k:
                    return
                result.append(root.val)
                fun(root.right, k)
        fun(root, k)
        return result[k-1]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallest(root, k)
    print("\noutput:", serialize(ans, "integer"))
