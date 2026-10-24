"""124. 二叉树中的最大路径和（二刷）——两腿更新答案/单腿喂父节点（O(n)/O(h) 标准解）

用户 AC 版（2026-10-24 22:23 提交 756748870，一次通过，7ms/23.5MB）
- 543 直径同款骨架：每个节点"两腿"（左贡献+右贡献+自己）更新全局答案；"单腿"（自己+较大一侧，负数截断为0）喂父节点
- 路径和允许负值，但向上传的贡献用 max(...,0) 截断——负数分支不选
- ⚡ 全局答案初始 float('-inf')（全负树也必须选一个节点，不能从 0 起）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        某一个节点，它的最大，等于左节点向上传的和右节点向上传的加上自身
        然后它向上传的是自身加上非负的子节点
        """
        result = [float('-inf')]

        def fun(root):
            if root:
                left_max = max(fun(root.left), 0)     # 左单腿贡献（负数不选 → 0）
                right_max = max(fun(root.right), 0)   # 右单腿贡献
                result[0] = max(result[0], root.val + left_max + right_max)  # 两腿=过根路径
                return root.val + max(left_max, right_max)  # 单腿喂父
            return 0

        fun(root)
        return result[0]


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

    print(s.maxPathSum(build([1, 2, 3])))                            # 6
    print(s.maxPathSum(build([-10, 9, 20, None, None, 15, 7])))      # 42
    print(s.maxPathSum(build([-3])))                                  # -3
    print(s.maxPathSum(build([-1, -2, -3])))                         # -1