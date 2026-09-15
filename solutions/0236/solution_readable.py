# -*- coding: utf-8 -*-
"""
第 236 题 二叉树的最近公共祖先 · 递归版（标准三情况，10 行，机考必看）
⚡⚡ 用户标记：机考之前要看一下，太妙了。

三种情况的递归归纳：
① 空节点 / 命中 p 或 q → 直接返回该节点
② 左右子树都找到 → 当前节点就是 LCA（p、q 分居两侧）
③ 只有一侧找到 → 那一侧的结果就是 LCA（p、q 在同一侧）

验证：与用户 BFS 父链剪枝版 3 万组对拍 0 差异。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root                       # ① 空 / 命中
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root                       # ② 分居两侧 → 根是 LCA
        return left or right                  # ③ 同侧 → 返回找到的那侧