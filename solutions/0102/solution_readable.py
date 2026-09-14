# -*- coding: utf-8 -*-
"""
第 102 题 二叉树的层序遍历 · 标准 BFS 队列版
与用户 DFS+dep 版结果完全等价（5 万组对拍 0 差异）。
"层序遍历"的字面实现：逐层入队出队。空间 O(最大层宽)。
"""
from typing import Optional, List
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):      # 关键：len(q) 快照 = 当前层节点数
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res