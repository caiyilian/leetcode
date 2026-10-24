# Created by Chono-Hina at 2026/09/14 19:23
# leetgo: 1.4.18
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        result = 0
        while q:
            for _ in range(len(q)):        # 按层快照：处理完一层 result+1
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result += 1
        return result
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().maxDepth(root)
    print("\noutput:", serialize(ans, "integer"))
