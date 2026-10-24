"""226. 翻转二叉树（二刷）——递归 + 元组赋值（O(n)/O(h) 标准解）

用户 AC 版（2026-10-24 22:42 提交 756752540，一次通过，0ms/19.1MB）
- 左右子树递归翻转后交换（后序：先处理孩子，再交换自己）
- 元组赋值 root.left, root.right = fun(right), fun(left) —— 先算右侧再算左侧，天然完成交换
- 空树守卫 if not root: return None
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def fun(root):
            if root:
                root.left, root.right = fun(root.right), fun(root.left)  # 元组赋值交换
                return root

        fun(root)
        return root


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

    def serialize(root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    print(serialize(s.invertTree(build([4, 2, 7, 1, 3, 6, 9]))))  # [4,7,2,9,6,3,1]
    print(s.invertTree(None))                                       # None
    print(serialize(s.invertTree(build([2, 1, 3]))))               # [2,3,1]
    print(serialize(s.invertTree(build([1]))))                     # [1]