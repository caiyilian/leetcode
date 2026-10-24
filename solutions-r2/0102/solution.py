"""102. 二叉树的层序遍历（二刷）——BFS 按层快照（O(n)/O(n) 标准解）

用户 AC 版（2026-10-24 19:28 提交 756720906，一次通过，0ms/19.8MB）
- deque 队列 BFS + for _ in range(len(q)) 按层快照
- 空树守卫 if not root: return []
"""

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
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

    print(s.levelOrder(build([3, 9, 20, None, None, 15, 7])))  # [[3],[9,20],[15,7]]
    print(s.levelOrder(build([1])))                             # [[1]]
    print(s.levelOrder(build([])))                              # []