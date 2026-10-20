"""138. 随机链表的复制（二刷）——哈希映射两遍法（O(n)/O(n)）

用户 AC 版（2026-10-20 20:47 提交 756008475，一次通过，43ms/19.9MB）
- 两遍：① 复制 next 链 + 建"原节点→新节点"映射；② 按映射补 random
- 关键细节：hash_map 预置 {None: None}，random=None 时也能查到
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash_map = {None: None}
        p = head
        dummy = Node(0)
        prev = dummy
        while p:
            new = Node(p.val)
            prev.next = new
            prev = new
            hash_map[p] = new
            p = p.next
        p = head
        new = dummy.next
        while p:
            new.random = hash_map[p.random]
            new = new.next
            p = p.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()

    def build(vals, randoms):
        if not vals:
            return None
        nodes = [Node(v) for v in vals]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        for i, r in enumerate(randoms):
            nodes[i].random = nodes[r] if r != -1 else None
        return nodes[0]

    def to_pairs(head):
        # 返回 [(val, random指向第几个节点)]，None 记为 -1
        idx = {}
        cur, i = head, 0
        while cur:
            idx[cur] = i
            i += 1
            cur = cur.next
        res = []
        cur = head
        while cur:
            res.append((cur.val, idx.get(cur.random, -1)))
            cur = cur.next
        return res

    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
    h = build([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
    print(to_pairs(s.copyRandomList(h)))   # [(7,-1),(13,0),(11,4),(10,2),(1,0)]
    print(to_pairs(s.copyRandomList(build([1, 2], [1, 1]))))  # [(1,1),(2,1)] 自引用
    print(to_pairs(s.copyRandomList(build([1], [-1]))))        # [(1,-1)]
    print(to_pairs(s.copyRandomList(build([], []))))           # []
