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
        result = [k, 0]                # result[0]=剩余计数, result[1]=答案（分离！）

        def fun(root):
            if root:
                fun(root.left)         # 中序：先左
                result[0] -= 1
                if result[0] == 0:     # 数到第 k 个
                    result[1] = root.val
                    return             # 剪枝：不再遍历右子树
                fun(root.right)

        fun(root)
        return result[1]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallest(root, k)
    print("\noutput:", serialize(ans, "integer"))
