# Created by Chono-Hina at 2026/09/14 21:22
# leetgo: 1.4.18
# https://leetcode.cn/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            now = []
            for _ in range(len(q)):        # ★ 按层快照：此刻队列里的就是这一层
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                now.append(node.val)
            result.append(now)
        return result
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("\noutput:", serialize(ans, "integer[][]"))
