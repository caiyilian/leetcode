# -*- coding: utf-8 -*-
"""
第 104 题 二叉树的最大深度 · 用户原版（deep 传参版）
思路：把深度提前算好一路带下去，空节点返回 deep-1。
与经典版（1 + max）结果完全等价（5 万组对拍 0 差异），
但每层递归多传 deep 参数 + 空节点多一次 deep-1 运算，本机实测慢 ~48%。
复杂度同为 O(n)，保留此版作为"另一种正确思路"的对比参考。
"""
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.scan(root)

    def scan(self, root, deep=1):
        if root:
            # 返回左和右树最大的那个
            return max(self.scan(root.left, deep=deep + 1),
                       self.scan(root.right, deep=deep + 1))
        # 是 None，那么深度不增加
        return deep - 1