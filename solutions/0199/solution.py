# Created by Chono-Hina at 2026/09/15 16:15
# leetgo: 1.4.18
# https://leetcode.cn/problems/binary-tree-right-side-view/

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        result = []
        while q:                                    # 队列不为空，表示还没处理完的层
            for _ in range(len(q)):                 # len(q) 快照 = 当前层节点数
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(node.val)                 # for 循环结束 node = 本层最右 ✅
        return result
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().rightSideView(root)
    print("\noutput:", serialize(ans, "integer[]"))
