"""94. 二叉树的中序遍历（二刷）——递归（左中右）

用户 AC 版（2026-10-22 20:10 提交 756406720，一次通过，0ms/19MB）
- 标准中序递归：左 → 中 → 右
- result 用闭包共享（不用返回值传递）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # 左中右
        result = []

        def fun(root):
            if root:
                fun(root.left)
                result.append(root.val)
                fun(root.right)

        fun(root)
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

    print(s.inorderTraversal(build([1, None, 2, None, None, 3])))  # [1,3,2]
    print(s.inorderTraversal(build([])))                            # []
    print(s.inorderTraversal(build([1])))                           # [1]
    print(s.inorderTraversal(build([1, 2, 3])))                     # [2,1,3]
