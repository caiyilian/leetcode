# -*- coding: utf-8 -*-
"""
第 437 题 路径总和 III · 暴力参照版（O(n²)，用于对拍验证前缀和版）
以每个节点为起点，向下枚举所有路径。仅作理解/验证用，面试讲前缀和版。
"""
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def from_node(node, acc):
            if not node:
                return 0
            acc += node.val
            return (1 if acc == targetSum else 0) \
                + from_node(node.left, acc) + from_node(node.right, acc)
        return from_node(root, 0) + self.pathSum(root.left, targetSum) \
            + self.pathSum(root.right, targetSum)