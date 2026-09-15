# -*- coding: utf-8 -*-
"""
第 108 题 将有序数组转换为二叉搜索树 · 进阶版（传下标区间，O(n)，无切片拷贝）
与用户切片版结果等价（同一棵平衡 BST）。
进阶点：切片 nums[:mid] 每次拷贝 O(k)，总 O(n log n)；
        传 lo/hi 下标不拷贝，每个元素只访问一次 → O(n)。面试加分写法。
"""
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = fun(lo, mid - 1)
            root.right = fun(mid + 1, hi)
            return root
        return fun(0, len(nums) - 1)