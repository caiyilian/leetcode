"""538. 把二叉搜索树转换为累加树（二刷）——反中序累加（O(n)/O(h) 标准解）

用户 AC 版（2026-10-25 22:02 提交 756907866，一次通过，7ms/20.9MB）
- 累加树 = 每个节点替换为"原树中大于等于它的所有值之和"
- BST 中序升序 → 反中序（右→根→左）就是降序 → 一路累加，acc 即"已遍历过的更大值之和"
- 代码极简：反中序 + acc[0] 累加 + 原地改 val
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        acc = [0]                  # 已累加的"更大值"总和（闭包共享）

        def fun(root):
            if root:
                fun(root.right)    # 反中序：先右（更大的）
                acc[0] += root.val
                root.val = acc[0]  # 当前值 = 累计和（含自己）
                fun(root.left)     # 再左（更小的）
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

    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    t = build([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    print(inorder(s.convertBST(t)))   # [36,36,35,33,30,26,21,15,8]
    print(s.convertBST(None))         # None
    print(inorder(s.convertBST(build([1]))))  # [1]