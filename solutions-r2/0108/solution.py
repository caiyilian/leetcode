"""108. 将有序数组转换为二叉搜索树（二刷）——分治 + 中点取根（O(n)/O(log n) 标准解）

用户 AC 版（2026-10-24 20:44 提交 756732192，一次通过，3ms/20MB）
- 每次取区间中点做根，左半建左子树、右半建右子树 → 天然平衡
- 用下标圈区间（start, end）避免切片复制（进阶：O(n) 空间）
- 边界：if not nums 处理空数组
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """
        平衡：左右两个数深度相差不超过1
        搜索树，左树全都小于当前节点
        """
        if not nums:
            return None
        length = len(nums)

        def fun(start, end):
            middle = (end - start) // 2 + start      # 中点：左半比右半多0/1个 → 平衡
            root = TreeNode(nums[middle])
            left_num = middle - start
            right_num = end - middle - 1
            if left_num > 0:
                root.left = fun(start, middle)
            if right_num > 0:
                root.right = fun(middle + 1, end)
            return root

        return fun(0, length)


if __name__ == "__main__":
    s = Solution()

    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    print(inorder(s.sortedArrayToBST([-10, -3, 0, 5, 9])))  # [-10,-3,0,5,9] 中序=原数组
    print(inorder(s.sortedArrayToBST([1, 3])))              # [1,3]
    print(s.sortedArrayToBST([]))                           # None
    print(inorder(s.sortedArrayToBST([1])))                 # [1]