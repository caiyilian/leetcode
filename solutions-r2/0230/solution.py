"""230. 二叉搜索树中第 K 小的元素（二刷）——中序递增 + 计数剪枝（O(h+k)/O(h)）

用户 AC 版（2026-10-24 23:05 WA → 23:23 AC，3ms/21.8MB）
- BST 中序 = 升序，第 k 小 = 中序遍历数到第 k 个
- 计数 result[0] 减到 0 时，result[1] 记录答案并剪枝（不再遍历右子树）
- ⚡ WA→AC：计数变量 result[0] 不能复用存答案（WA 版覆盖计数导致右子树判断错）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [k, 0]                # result[0]=剩余计数, result[1]=答案（分离！）

        def fun(root):
            if root:
                fun(root.left)         # 中序：先左
                result[0] -= 1
                if result[0] == 0:     # 数到第 k 个
                    result[1] = root.val
                    return             # 剪枝：不再遍历右子树
                fun(root.right)

        fun(root)
        return result[1]


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

    r = build([3, 1, 4, None, 2])
    print(s.kthSmallest(r, 1))    # 1
    print(s.kthSmallest(r, 2))    # 2
    print(s.kthSmallest(r, 3))    # 3
    print(s.kthSmallest(r, 4))    # 4