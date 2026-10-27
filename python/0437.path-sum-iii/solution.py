# Created by Chono-Hina at 2026/09/15 19:35
# leetgo: 1.4.18
# https://leetcode.cn/problems/path-sum-iii/

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = [0]
        hash_map = {0: 1}            # 前缀和 → 出现次数；{0:1} 虚拟起点（路径可从根开始）

        def fun(root, acc=0):
            if root:
                acc += root.val                              # 当前前缀和
                result[0] += hash_map.get(acc - targetSum, 0)  # 查差值：有几个起点凑出 targetSum
                hash_map[acc] = hash_map.get(acc, 0) + 1     # 记录当前前缀和
                fun(root.left, acc)
                fun(root.right, acc)
                hash_map[acc] -= 1                           # ★ 回溯撤销（防跨子树）

        fun(root)
        return result[0]
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)
    print("\noutput:", serialize(ans, "integer"))
