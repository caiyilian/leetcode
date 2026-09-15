# Created by Chono-Hina at 2026/09/15 17:12
# leetgo: 1.4.18
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        前序是：根左右；中序是：左根右
        前序给"根是谁"，中序给"根的左右各有几个"
        """
        index_dict = {i: v for v, i in enumerate(inorder)}   # 值 → 中序索引（O(1) 定位）
        length = len(preorder)
        # 前两个用于前序，后两个用于中序
        left1, right1, left2, right2 = 0, length-1, 0, length-1
        def fun(left1, right1, left2, right2):
            if left1 > right1:
                return None
            root = TreeNode(preorder[left1])          # 前序第一个 = 根
            index = index_dict[preorder[left1]]       # 根在中序的索引
            left_count = index - left2                # 左子树节点数（中序里根左边有几个）
            root.left = fun(left1+1, left1+left_count, left2, index-1)
            root.right = fun(left1+left_count+1, right1, index+1, right2)
            return root
        return fun(left1, right1, left2, right2)
        

# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    inorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)
    print("\noutput:", serialize(ans, "TreeNode"))
