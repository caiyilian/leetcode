"""617. 合并二叉树（二刷）——以 root1 为主的递归合并（O(n)/O(h) 标准解）

用户 AC 版（2026-10-27 21:14 提交 757299057，一次通过，0ms/19.5MB）
- 以 root1 为主树：两棵都有的节点值相加，单边为空直接接上另一边
- 递归返回"合并后的当前节点"：root1 上有 → 继续向下合并；否则返回非空的一边
- 空树守卫 if not root1: return root2（root1 空则整棵用 root2）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        统一加到root1
        如果两个都有的节点，相加
        如果左是None，右有节点，把右接入左，然后不用继续往下走
        如果左不是None，右是，那就不用继续往下走
        """
        if not root1:
            return root2

        def fun(root1, root2):
            if root1 and root2:
                root1.val += root2.val
                root1.left = fun(root1.left, root2.left)
                root1.right = fun(root1.right, root2.right)
                return root1
            else:
                return root1 if root1 else root2

        root1 = fun(root1, root2)
        return root1


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

    t1 = build([1, 3, 2, 5])
    t2 = build([2, 1, 3, None, 4, None, 7])
    print(serialize(s.mergeTrees(t1, t2)))          # [3,4,5,5,4,None,7]
    print(serialize(s.mergeTrees(None, build([1, 2]))))  # [1,2]
    print(serialize(s.mergeTrees(build([1, 2]), None)))  # [1,2]
    print(s.mergeTrees(None, None))                    # None