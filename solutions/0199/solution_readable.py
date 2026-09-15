# -*- coding: utf-8 -*-
"""
第 199 题 二叉树的右视图 · 用户 v1（层队列版）
思路：list1 是"层的队列"（一个元素 = 一整层），每层取最后一个节点。
与 final 版（deque 快照版）结果等价（5 万组对拍 0 差异）。
注意：list1.pop(0) 是 O(层数)（列表头弹出移动元素），已改进为 deque 快照版。
"""
from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        list1 = [[root]]
        result = [root.val]
        while list1:
            q = list1.pop(0)                     # 取出当前层
            list_layer = []
            for node in q:
                if node.left is not None:
                    list_layer.append(node.left)
                if node.right is not None:
                    list_layer.append(node.right)
            if not list_layer:
                break
            result.append(list_layer[-1].val)    # 每层最右 = 右视图
            list1.append(list_layer)
        return result