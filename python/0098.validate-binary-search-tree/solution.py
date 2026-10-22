# Created by Chono-Hina at 2026/09/15 10:16
# leetgo: 1.4.18
# https://leetcode.cn/problems/validate-binary-search-tree/

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 左中右递增不就好了
        last = [float('-inf')]

        def fun(root):
            if root:
                if fun(root.left) is False:   # 左子树不合法 → 剪枝
                    return False
                if last[0] >= root.val:       # 中序必须严格递增（>= 判重复值）
                    return False
                last[0] = root.val
                return fun(root.right)
            return True

        return fun(root)
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isValidBST(root)
    print("\noutput:", serialize(ans, "boolean"))
