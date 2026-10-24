"""114. 二叉树展开为链表（二刷）——返回(头,尾)的递归拼接（O(n)/O(h) 标准解）

用户 AC 版（2026-10-24 21:30 WA → 21:38 AC，0ms/19.2MB）
- fun(root) 返回 (展平链头, 展平链尾)——左右子树各自展平，拿到头尾后拼接
- 拼接规则：左链尾.right = 右链头；root.right = 左链头；root.left = None
- ⚡ WA→AC 修复：右子树为空时 right_last=None，要把链尾改成 left_last（否则父级拼接丢节点）
- 本题要求原地改（Do not return anything）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        先把左树搞定，返回左头尾两个指针
        然后搞定右，返回右头尾
        如果左头是None，那就直接合格了，返回根和右尾
        否则，把右头接入左尾巴，然后把左头接入根节点的右
        然后return根和右尾
        如果是叶子节点，那么返回的两个都是本身
        """
        def fun(root):
            if root:
                root.left, left_last = fun(root.left)
                root.right, right_last = fun(root.right)
                if root.left:
                    left_last.right = root.right
                    root.right = root.left
                    root.left = None
                    if right_last is None:        # ★ 修复：右子树为空时，链尾=左链尾
                        right_last = left_last
                return root, right_last if (right_last is not None) else root
            return None, None

        fun(root)
        return root


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
        res = []
        cur = root
        while cur:
            res.append(cur.val)
            cur = cur.right
        return res

    s = Solution()
    r = build([1, 2, 5, 3, 4, None, 6])
    s.flatten(r)
    print(collect(r))            # [1,2,3,4,5,6] 官方示例
    r2 = build([1, 2, None, 3])  # 原 WA 用例：节点2只有左孩子
    s.flatten(r2)
    print(collect(r2))           # [1,2,3]
    r3 = build([])
    s.flatten(r3)
    print(r3)                    # None