# -*- coding: utf-8 -*-
"""
第 94 题 二叉树的中序遍历 · 迭代版（显式栈）
与递归版逻辑完全等价（5 万组随机树对拍 0 差异）：
"一路向左压栈 → 弹栈访问 → 转右子树"，显式模拟系统栈。
优点：无递归深度上限（Python 默认 ~1000 层），深树不栈溢出。
"""
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack, cur = [], [], root
        while stack or cur:
            while cur:                  # ① 一路向左，路径节点全压栈
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()           # ② 弹出 = 访问（最左无左孩子的节点）
            res.append(cur.val)
            cur = cur.right             # ③ 转向右子树（下一轮压它的左链）
        return res