"""297. 二叉树的序列化与反序列化（二刷）——BFS 层序 + 队列消费（O(n)/O(n) 标准解）

用户 AC 版（2026-10-25 21:26 提交 756900652，RF→RE→AC，89ms/22.2MB）
- serialize：BFS 层序，None 表示空孩子（不 trim 尾部 None 也行，deserialize 按队列消费）
- deserialize：队列存"等着接孩子的父节点"，i 指针每次消费左/右两个值
- ⚡ 与 RF 版差异：不再用 2*i+1/2*i+2 下标建树（None 位置会算错），改用队列消费天然对应层序
- 另附一刷 DFS 前序版（递归，"N," 哨兵）参考
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# ========== 用户 AC 版：BFS 层序 + 队列反序列化 ==========
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
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
        """Decodes your encoded data to tree."""
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


# ========== 一刷参考：DFS 前序 + "N," 哨兵 ==========
class CodecDFS:

    def serialize(self, root):
        result = []
        def fun(root):
            if root:
                result.append(str(root.val) + ",")
                fun(root.left)
                fun(root.right)
            else:
                result.append("N,")
        fun(root)
        return "".join(result)[:-1]

    def deserialize(self, data):
        data_list = data.split(",")
        length = len(data_list)
        def fun(index):
            if index > length - 1 or data_list[index] == 'N':
                return None, index
            root = TreeNode(int(data_list[index]))
            root.left, index = fun(index + 1)
            root.right, index = fun(index + 1)
            return root, index
        root, _ = fun(0)
        return root


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

    c = Codec()
    t = build([1, 2, 3, None, None, 4, 5])
    s = c.serialize(t)
    print("serialize:", s)
    print("roundtrip ok:", c.deserialize(s).val == 1)

    for cls in (Codec, CodecDFS):
        cc = cls()
        for vals in ([1, 2, 3, None, None, 4, 5], [], [1], [1, 2]):
            r = cc.deserialize(cc.serialize(build(vals)))
            print(cls.__name__, vals, "→", r.val if r else None)