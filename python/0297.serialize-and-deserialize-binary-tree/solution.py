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
        if not root:
            return ""
        result = []
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                result.append(str(node.val if node else None))
                if node is None:
                    continue
                q.append(node.left)
                q.append(node.right)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])       # 队列存"等着接孩子的父节点"
        i = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                i += 1
                left = data[i]              # 消费左孩子
                if left != 'None':
                    left = TreeNode(int(left))
                    node.left = left
                    q.append(left)          # 左孩子也要当父 → 入队
                i += 1
                right = data[i]             # 消费右孩子
                if right != 'None':
                    right = TreeNode(int(right))
                    node.right = right
                    q.append(right)
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