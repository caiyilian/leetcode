"""236. 二叉树的最近公共祖先（二刷）——后序计数法（O(n)/O(h) 标准解变体）

用户 AC 版（2026-10-25 15:13 提交 756829468，一次通过，164ms/49.7MB）
- 后序计数：fun(root) 返回子树包含 p/q 的个数；第一个凑齐 2 的节点 = LCA
- 后序遍历天然"从下往上"，最深的凑齐点必然是最低公共祖先
- 注意：力扣约束 p != q；若允许 p == q 需改判断（题目明确 p≠q，无影响）
- 另附官方解法一（递归返回节点）作参考
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ========== 用户 AC 版：后序计数 ==========
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        左树有，右树也有，那么当前节点就是其中一个祖先节点
        如果其中一个树有，另一个树没有，但是当前节点是其中一个，那么祖先节点就是当前节点
        如果两个树都没有，返回False
        """
        result = [None]

        def fun(root):
            if root:
                result_left = fun(root.left)
                result_right = fun(root.right)
                return_result = result_left + result_right
                if return_result == 2:                  # 左右子树各找到 p/q → 当前是 LCA
                    if result[0] is None:
                        result[0] = root
                else:                                   # 只有一侧找到
                    if (root is p) or (root is q):      # 自己是另一个目标
                        return_result += 1
                        if return_result == 2:
                            result[0] = root
                return return_result
            return 0

        fun(root)
        return result[0]


# ========== 官方解法一：递归返回节点（参考，10 行内） ==========
class SolutionStandard:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        return l or r


if __name__ == "__main__":
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

    def collect(root):
        by_val = {}
        def dfs(node):
            if node:
                by_val[node.val] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return by_val

    t = build([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    m = collect(t)
    s = Solution()
    print(s.lowestCommonAncestor(t, m[5], m[1]).val)   # 3
    print(s.lowestCommonAncestor(t, m[5], m[4]).val)   # 5（p 是祖先）
    print(s.lowestCommonAncestor(t, m[3], m[3]).val)   # 3