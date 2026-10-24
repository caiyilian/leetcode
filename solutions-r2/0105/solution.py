"""105. 从前序与中序遍历序列构造二叉树（二刷）——四边界递归（O(n) 预哈希 / O(n²) 裸 index）

用户 AC 版（2026-10-24 20:22 提交 756728732，一次通过，35ms/21MB）
- 前序定根（preorder[l1] 是当前子树根）、中序分界（根的左边是左子树、右边是右子树）
- 四边界 (l1,r1,l2,r2) 圈定当前子树在两数组中的范围
- 小优化点：inorder.index() 每次 O(n)，一刷用 index_dict 预哈希 → O(1) 查找、总 O(n)（本文件附优化版）
- 注意：空输入会崩，但力扣约束 preorder.length>=1，无影响
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ========== 用户 AC 版（裸 inorder.index，最坏 O(n²)） ==========
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        length1 = len(preorder)
        length2 = len(inorder)
        """
        输入[3,9,20,15,7],[9,3,15,20,7]，得到，root是3，
        left的先序和中序都是[9]，右的先序是[20,15,7]，中序是[15,20,8]
        """
        def fun(l1, r1, l2, r2):
            root_val = preorder[l1]
            index_root_inorder = inorder.index(root_val)   # O(n) 找根在中序的位置
            root = TreeNode(root_val)
            left_num = index_root_inorder - l2             # 左子树节点数
            right_num = r2 - index_root_inorder - 1        # 右子树节点数
            if left_num:
                root.left = fun(l1 + 1, l1 + 1 + left_num, l2, index_root_inorder)
            if right_num:
                root.right = fun(l1 + 1 + left_num, r1, index_root_inorder + 1, r2)
            return root

        result = fun(0, length1, 0, length2)
        return result


# ========== 优化版：index_dict 预哈希（O(n)） ==========
class SolutionHash:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        index_dict = {v: i for i, v in enumerate(inorder)}   # ★ 值→下标 预哈希

        def fun(l1, r1, l2, r2):
            if l1 >= r1:                       # 空区间 → None（比 if left_num 更通用）
                return None
            root_val = preorder[l1]
            index_root_inorder = index_dict[root_val]        # O(1) 找根
            root = TreeNode(root_val)
            left_num = index_root_inorder - l2
            root.left = fun(l1 + 1, l1 + 1 + left_num, l2, index_root_inorder)
            root.right = fun(l1 + 1 + left_num, r1, index_root_inorder + 1, r2)
            return root

        return fun(0, len(preorder), 0, len(inorder))


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

    def serialize(root):
        if not root:
            return []
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    for s in (Solution(), SolutionHash()):
        print(serialize(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))  # [3,9,20,None,None,15,7]
        print(serialize(s.buildTree([-1], [-1])))                            # [-1]
        print(serialize(s.buildTree([1, 2], [2, 1])))                        # [1,None,2]