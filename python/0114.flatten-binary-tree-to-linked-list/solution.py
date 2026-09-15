# Created by Chono-Hina at 2026/09/15 15:08
# leetgo: 1.4.18
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                # 找到左子树展开后的链尾（前序遍历最后一个节点）
                max_right = self.find_max_right(root.left)[0]
                max_right.right = root.right   # 原右子树接到左链尾后面
                root.right = root.left          # 左子树整体搬到右边
                root.left = None                # 清空左指针
            root = root.right

    def find_max_right(self, root, result=[None]):
        """找左子树展开后的链尾（递归遍历整棵子树，功能正确但 O(子树大小)）"""
        if root:
            result[0] = root
            if not root.right:
                self.find_max_right(root.left)
            self.find_max_right(root.right)
            return result
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    Solution().flatten(root)
    ans = root
    print("\noutput:", serialize(ans, "TreeNode"))
