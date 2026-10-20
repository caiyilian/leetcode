"""138. 随机链表的复制（二刷）——双解法：哈希两遍法（主）+ 交错法 O(1)（进阶）

用户 AC 版（2026-10-20 20:47 提交 756008475，一次通过，43ms/19.9MB）
- 两遍：① 复制 next 链 + 建"原节点→新节点"映射；② 按映射补 random
- 关键细节：hash_map 预置 {None: None}，random=None 时也能查到

附：交错法 O(1) 空间（力扣 follow-up）——新节点插在原节点后面，"位置即映射"
① 穿插 A→A'→B→B'→…  ② cur.next.random = cur.random.next 补 random
③ 拆链：奇数位原链、偶数位新链
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# ========== 用户 AC 版：哈希两遍法（O(n)/O(n)） ==========
class SolutionHash:
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


# ========== 交错法（O(n)/O(1)，进阶） ==========
class SolutionInterleave:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # ① 插入拷贝：A -> A' -> B -> B' -> ...
        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next

        # ② 补 random：A'.random = A.random.next（原 random 的拷贝就在它后面）
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # ③ 拆开：奇数位是原链，偶数位是新链
        new_head = head.next
        cur = head
        while cur:
            clone = cur.next
            cur.next = clone.next
            clone.next = clone.next.next if clone.next else None
            cur = cur.next
        return new_head


# 默认用用户版
Solution = SolutionHash


if __name__ == "__main__":
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

    for s in (SolutionHash(), SolutionInterleave()):
        h = build([7, 13, 11, 10, 1], [-1, 0, 4, 2, 0])
        print(to_pairs(s.copyRandomList(h)))       # [(7,-1),(13,0),(11,4),(10,2),(1,0)]
        print(to_pairs(s.copyRandomList(build([1, 2], [1, 1]))))  # [(1,1),(2,1)] 自引用
        print(to_pairs(s.copyRandomList(build([1], [-1]))))        # [(1,-1)]
        print(to_pairs(s.copyRandomList(build([], []))))           # []
