"""337. 打家劫舍 III（二刷）——树形 DP（用户 AC 版）

用户二刷（2026-11-02 16:38 提交 758214307，AC 一次通过，0ms/20.6MB）
- 树上状态机：每个节点返回二元组 (no, yes) = 该子树在"根不偷/根偷"下的最大收益
- 后序遍历自底向上：偷 → 子节点必须不偷（root.val + no左 + no右）
-                     不偷 → 子节点偷不偷都行（max(偷,不偷) 左右相加）
- 198 打家劫舍（数组线性）→ 本题树形：同样的"选/不选"，只是邻居关系从相邻变成父子
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ===== 用户 AC 版（树形 DP 二元组） =====
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def fun(root):
            if root:
                no_rob_left, robed_left = fun(root.left)
                no_rob_right, robed_right = fun(root.right)
                # 如果自己偷，子节点必须是不偷
                yes = root.val + no_rob_left + no_rob_right
                # 如果不偷，子节点可以是不偷，也可以是偷
                no = max(robed_left, no_rob_left) + max(robed_right, no_rob_right)
                return no, yes
            return 0, 0
        no, yes = fun(root)
        return max(no, yes)


# ===== 参考：等价写法（dfs 命名 + 元组解包） =====
class SolutionRef:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return (0, 0)          # (不偷, 偷)
            l0, l1 = dfs(node.left)
            r0, r1 = dfs(node.right)
            cur0 = max(l0, l1) + max(r0, r1)   # 不偷当前：子树随意
            cur1 = node.val + l0 + r0          # 偷当前：子树必须不偷
            return (cur0, cur1)
        a, b = dfs(root)
        return max(a, b)


if __name__ == "__main__":
    s = Solution()
    r1 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    print(s.rob(r1))                     # 7
    r2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(s.rob(r2))                     # 9