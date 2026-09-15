# -*- coding: utf-8 -*-
"""
第 230 题 二叉搜索树中第 K 小的元素 · 迭代版（O(h + k)，彻底提前终止）
与用户递归剪枝版（v2）结果等价（5 万组对拍 0 差异）。
递归版剪不掉左子树的多余深度（栈里压着祖先）；
迭代版控制入栈时机，数到第 k 个立即返回 → 真正的 O(h + k)。
"""
from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack, cur = [], root
        while stack or cur:
            while cur:                       # 走到最左，路径入栈
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()                # 弹出 = 中序第 1, 2, 3... 个
            k -= 1
            if k == 0:
                return cur.val               # 数到第 k 个 → 停
            cur = cur.right
        return -1