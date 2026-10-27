"""543. 二叉树的直径（二刷）——两腿更新答案/单腿喂父节点（O(n)/O(h) 标准解）

用户 AC 版（2026-10-27 20:48 提交 757292821，一次通过，3ms/22MB）
- 直径 = 任意两节点间最长路径的"边数"（可不经过根）
- 每个节点：两腿（左单链+右单链）更新全局答案；单腿（较长一侧+1）喂父节点
- 124 最大路径和同款骨架（⚡重点标记），返回值≠题目答案
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        每一个树的最长，等于左树上传+右树上传
        而这个树的最长，与上传，是不同的，
        上传只取最长的那颗树加1
        """
        result = [0]               # 全局答案：最长路径边数

        def fun(root):
            if root:
                left = fun(root.left)
                right = fun(root.right)
                result[0] = max(result[0], left + right)   # 两腿：过当前节点的路径 = 左链+右链
                return max(left, right) + 1                # 单腿：喂父节点（最长单链高度）
            return 0

        fun(root)
        return result[0]


if __name__ == "__main__":
    s = Solution()

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

    print(s.diameterOfBinaryTree(build([1, 2, 3, 4, 5])))  # 3
    print(s.diameterOfBinaryTree(build([1, 2])))           # 1
    print(s.diameterOfBinaryTree(None))                    # 0
    print(s.diameterOfBinaryTree(build([1])))              # 0