"""98. 验证二叉搜索树（二刷）——中序遍历递增法（O(n)/O(h) 标准解）

用户 AC 版（2026-10-22 20:21 提交 756409485，一次通过，0ms/20.8MB）
- BST ⇔ 中序遍历严格递增（官方解法二）
- last = [float('-inf')] 哨兵（列表包一层避免闭包 UnboundLocalError）
- >= 判重：严格递增，相等即 False；左子树 False 提前剪枝
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 左中右递增不就好了
        last = [float('-inf')]

        def fun(root):
            if root:
                if fun(root.left) is False:
                    return False
                if last[0] >= root.val:
                    return False
                last[0] = root.val
                return fun(root.right)
            return True

        return fun(root)


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

    print(s.isValidBST(build([2, 1, 3])))        # True
    print(s.isValidBST(build([5, 1, 4, None, None, 3, 6])))  # False（右子树 3<4 跨层违反）
    print(s.isValidBST(build([1, 1])))           # False（重复值）
    print(s.isValidBST(build([])))               # True（空树）
    print(s.isValidBST(build([1])))              # True
    print(s.isValidBST(build([5, 6, 4])))        # False（左 6 > 根 5）