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
        length1 = len(preorder)
        length2 = len(inorder)
        """
        输入[3,9,20,15,7],[9,3,15,20,7]，得到，root是3，
        left的先序和中序都是[9]，右的先序是[20,15,7]，中序是[15,20,8]
        """
        def fun(l1, r1, l2, r2):
            root_val = preorder[l1]
            index_root_inorder = inorder.index(root_val)   # O(n) 找根在中序的位置
            root = TreeNode(root_val)
            left_num = index_root_inorder - l2             # 左子树节点数
            right_num = r2 - index_root_inorder - 1        # 右子树节点数
            if left_num:
                root.left = fun(l1 + 1, l1 + 1 + left_num, l2, index_root_inorder)
            if right_num:
                root.right = fun(l1 + 1 + left_num, r1, index_root_inorder + 1, r2)
            return root

        result = fun(0, length1, 0, length2)
        return result
        

# @lc code=end

if __name__ == "__main__":
    preorder: List[int] = deserialize("List[int]", read_line())
    inorder: List[int] = deserialize("List[int]", read_line())
    ans = Solution().buildTree(preorder, inorder)
    print("\noutput:", serialize(ans, "TreeNode"))
