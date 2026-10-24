"""104. 二叉树的最大深度（二刷）——BFS 层数计数（O(n)/O(n) 标准解）

用户 AC 版（2026-10-24 19:38 提交 756722285，一次通过，4ms/21.7MB）
- 复用 102 层序的"按层快照"套路：每处理完一层 result += 1，层数 = 深度
- 空树守卫 if not root: return 0
- 与经典递归 1 + max 等价（一刷用过）；BFS 不递归、无爆栈风险
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


if __name__ == "__main__":
    s = Solution()

    def build(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        for i, n in enumerate(nodes):
            if n:
                l, r = 2 * i + 1, 2 * i + 2
                if l < len(nodes) and nodes[l]:
                    n.left = nodes[l]
                if r < len(nodes) and nodes[r]:
                    n.right = nodes[r]
        return nodes[0]

    print(s.maxDepth(build([3, 9, 20, None, None, 15, 7])))  # 3
    print(s.maxDepth(build([1, None, 2])))                     # 2
    print(s.maxDepth(build([])))                               # 0
    print(s.maxDepth(build([1])))                              # 1