"""437. 路径总和 III（二刷）——前缀和 + 哈希 + 回溯（O(n)/O(n) 标准解）⚡机考重点

用户 AC 版（2026-10-27 22:44 提交 757319167，一次通过，8ms/20.2MB）
- 前缀和：从根到当前节点的累加和 acc；路径和 = acc_j - acc_i（i<j）
- 每个节点：查哈希里 acc - targetSum 出现几次（即有几个"起点"），累加进答案
- 回溯：递归返回前 hash_map[acc] -= 1（撤销，防跨子树计数）
- ⚡ 核心：查"差值"而非枚举路径对（与 560 和为 K 的子数组同款心法）
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = [0]
        hash_map = {0: 1}            # 前缀和 → 出现次数；{0:1} 虚拟起点（路径可从根开始）

        def fun(root, acc=0):
            if root:
                acc += root.val                              # 当前前缀和
                result[0] += hash_map.get(acc - targetSum, 0)  # 查差值：有几个起点凑出 targetSum
                hash_map[acc] = hash_map.get(acc, 0) + 1     # 记录当前前缀和
                fun(root.left, acc)
                fun(root.right, acc)
                hash_map[acc] -= 1                           # ★ 回溯撤销（防跨子树）

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

    t = build([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    print(s.pathSum(t, 8))     # 3
    print(s.pathSum(build([1]), 1))   # 1
    print(s.pathSum(None, 0))         # 0