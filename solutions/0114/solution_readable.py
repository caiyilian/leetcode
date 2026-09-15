# -*- coding: utf-8 -*-
"""
第 114 题 二叉树展开为链表 · 标准版（O(n) 时间 / O(1) 空间）
与用户 v2 功能等价（5 万组对拍一致），但找"链尾"只沿 right 链走 O(高度)，
不遍历整棵左子树 → 总时间 O(n)，且无递归无栈溢出风险。
原理：处理某节点时，其左子树已被前面几轮部分展开，
      left 的 right 链恰好就是"已展开部分的末尾"。
"""
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:          # 沿右链找尾（O(左子树高度)，非整棵树）
                    p = p.right
                p.right = cur.right     # 原右子树接到左链尾
                cur.right = cur.left    # 左子树搬到右边
                cur.left = None
            cur = cur.right