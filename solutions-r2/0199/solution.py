"""199. 二叉树的右视图（二刷）——BFS 层序取每层最右（O(n)/O(n) 标准解）

用户 AC 版（2026-10-24 22:34 提交 756750912，一次通过，0ms/19MB）
- 复用 102 层序的"按层快照"套路，收集每层最后一个节点
- 关键细节：for 循环结束后 node 停留在本层最后一个节点 → result.append(node.val)
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
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        result = []
        q = deque([root])
        while q:
            for _ in range(len(q)):        # 按层快照（102 同款）
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(node.val)        # ★ 循环结束后 node = 本层最后一个 = 最右
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

    print(s.rightSideView(build([1, 2, 3, None, 5, None, 4])))  # [1,3,4]
    print(s.rightSideView(build([1, None, 3])))                   # [1,3]
    print(s.rightSideView(build([1])))                            # [1]
    print(s.rightSideView(None))                                  # []