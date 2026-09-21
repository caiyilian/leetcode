# Created by Chono-Hina at 2026/09/21 20:40
# leetgo: 1.4.18
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def fun(root):
            if root:
                result.append(str(root.val) + ",")
                fun(root.left)
                fun(root.right)
            else:
                result.append("N,")
        fun(root)
        return "".join(result)[:-1]          # 先 join 再去末尾逗号

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        length = len(data_list)
        def fun(index):
            if index > length - 1 or data_list[index] == 'N':
                return None, index             # 返回"最后处理的位置"
            root = TreeNode(int(data_list[index]))
            root.left, index = fun(index + 1)   # 左子树从下一个位置
            root.right, index = fun(index + 1)  # 右子树从"左子树最后位置 + 1"
            return root, index
        root, _ = fun(0)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().Codec(root)
    print("\noutput:", serialize(ans, "string"))
