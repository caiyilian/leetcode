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
        self.count = 0
        prefix = {0: 1}                      # ① 虚拟起点：前缀和为 0 出现 1 次
        def dfs(node, cur_sum):
            if not node:
                return
            cur_sum += node.val              # ② 当前前缀和 = 根到本节点的路径和
            self.count += prefix.get(cur_sum - targetSum, 0)   # ③ 查差：找"前缀和=cur_sum-targetSum"的祖先
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1       # ④ 记录当前前缀和
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            prefix[cur_sum] -= 1             # ⑤ 回溯撤销（防止跨子树——关键！）
        dfs(root, 0)
        return self.count
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().pathSum(root, targetSum)
    print("\noutput:", serialize(ans, "integer"))
