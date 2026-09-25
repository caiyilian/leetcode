# Created by Chono-Hina at 2026/09/25 17:23
# leetgo: 1.4.18
# https://leetcode.cn/problems/convert-bst-to-greater-tree/

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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 反中序遍历（右→根→左 = 降序）+ 累加
        # 累加和 = 所有 ≥ 当前节点的值之和 → 正好是累加树定义
        sums = [0]               # 用列表引用，嵌套函数才能原地改（闭包陷阱）
        def fun(root):
            if root:
                fun(root.right)       # 右（大的）先
                root.val += sums[0]   # 加上已累加的所有更大值
                sums[0] = root.val    # 更新累加器
                fun(root.left)        # 左（小的）后
        fun(root)
        return root
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().convertBST(root)
    print("\noutput:", serialize(ans, "TreeNode"))
