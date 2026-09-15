# Created by Chono-Hina at 2026/09/15 20:22
# leetgo: 1.4.18
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        BFS 记录父节点映射 + 深度对齐 + 同步上溯（160 相交链表思路的树版本）
        剪枝：找到 p/q 就 break（father_dict 只需祖先链，BFS 层序保证祖先已记录）
        """
        from collections import deque
        que = deque([root])
        father_dict = {}
        depth = 0
        deep_p = None
        deep_q = None
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node == p:
                    deep_p = depth
                    if deep_q is not None:
                        break
                if node == q:
                    deep_q = depth
                    if deep_p is not None:
                        break
                if node.left:
                    father_dict[node.left] = node
                    que.append(node.left)
                if node.right:
                    father_dict[node.right] = node
                    que.append(node.right)
            else:
                depth += 1
                continue
            break
        # 深度对齐（深的先上溯到同一层）
        if deep_p > deep_q:
            for _ in range(deep_p - deep_q):
                p = father_dict[p]
        else:
            for _ in range(deep_q - deep_p):
                q = father_dict[q]
        # 同步上溯直到相遇 = 最近公共祖先
        while p != q:
            p = father_dict[p]
            q = father_dict[q]
        return p
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    p: int = deserialize("int", read_line())
    q: int = deserialize("int", read_line())
    ans = Solution().lowestCommonAncestor(root, p, q)
    print("\noutput:", serialize(ans, "TreeNode"))
