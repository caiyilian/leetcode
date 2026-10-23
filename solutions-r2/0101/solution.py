"""101. 对称二叉树（二刷）——镜像交叉递归（O(n)/O(h) 标准解）

用户 AC 版 + 修复（2026-10-23 19:00 提交 756579251，力扣 AC 0ms/19.4MB）
- 镜像交叉递归：左子 ↔ 右子、右子 ↔ 左子（官方解法一），短路剪枝
- ⚡ 修复：原版 return fun(root.left, root.right) 在空树时 AttributeError（力扣测试集无空树用例，
  未测出）；改为 return fun(root, root)——fun(None,None) 走 tree1 or tree2 不成立 → True
- 一刷记忆：⚡ 空树=True
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        一开始root.left.val == root.right.val
        """
        def fun(tree1, tree2):
            if tree1 or tree2:
                if (tree1 is None) or (tree2 is None) or (tree1.val != tree2.val):
                    return False
                result1 = fun(tree1.left, tree2.right)      # 左 ↔ 右
                if result1 is False:
                    return False
                result2 = fun(tree1.right, tree2.left)      # 右 ↔ 左
                return result2
            return True

        return fun(root, root)      # ★ 修复：空树也正确（fun(None,None) → True）


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

    print(s.isSymmetric(build([1, 2, 2, 3, 4, 4, 3])))   # True 标准对称
    print(s.isSymmetric(build([1, 2, 2, None, 3, None, 3])))  # False
    print(s.isSymmetric(build([1, 2, 2])))                # True
    print(s.isSymmetric(build([1, None, 2])))             # False 单边
    print(s.isSymmetric(None))                            # True 空树
    print(s.isSymmetric(build([1])))                      # True 单节点