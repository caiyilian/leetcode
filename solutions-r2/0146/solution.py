"""146. LRU 缓存（二刷）——哈希 + 双向链表 + 哨兵头尾（get/put 均 O(1) 最优解）

用户 AC 版（2026-10-22 19:54 提交 756403025，RE→AC，19ms/29.1MB）
- hash_map: key → 节点（O(1) 定位）；双向链表维护访问顺序（头=最近使用，尾=最久未用）
- 哨兵 forward/backward 头尾节点，消除"空链表/头尾节点"特判
- get：命中则把节点移到最前（摘除 → 插到 forward 后）并返回值
- put：已有则更新值并前移；新键则插入最前，若满则删 backward 前一个（最久未用）
- 空间 O(capacity)：hash_map 最多 capacity 个键 + 链表 capacity 个节点
"""


class ListNode2:
    def __init__(self, val=0, next=None, before=None):
        self.val = val
        self.next = next
        self.before = before


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.forward = ListNode2()          # 哨兵头（next 指向最近使用）
        self.backward = ListNode2()         # 哨兵尾（before 指向最久未用）
        self.forward.next = self.backward
        self.backward.before = self.forward
        self.hash_map = {}
        self.hash_map2 = {}                # node → key（驱逐时反向找 key）
        self.count = 0

    def get(self, key: int) -> int:
        # 如果不在
        if key not in self.hash_map:
            return -1
        # 在的话，首先，更新一下顺序
        node = self.hash_map[key]
        before_node = node.before
        next_node = node.next

        before_node.next = next_node       # ① 摘除 node
        next_node.before = before_node

        node.before = self.forward         # ② 插到 forward 后（最新）
        node.next = self.forward.next

        self.forward.next.before = node
        self.forward.next = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            # 移动到最开头
            node = self.hash_map[key]
            before_node = node.before
            next_node = node.next

            before_node.next = next_node
            next_node.before = before_node

            node.before = self.forward
            node.next = self.forward.next

            self.forward.next.before = node
            self.forward.next = node
        else:
            # 不在的话
            node = ListNode2(value)
            self.hash_map[key] = node
            self.hash_map2[node] = key
            node.before = self.forward
            node.next = self.forward.next

            self.forward.next.before = node
            self.forward.next = node
            if self.count == self.capacity:   # 超过阈值，提出最不常用的
                delete_node = self.backward.before

                delete_node.before.next = self.backward
                self.backward.before = delete_node.before

                self.hash_map.pop(self.hash_map2[delete_node])
            else:
                self.count += 1


if __name__ == "__main__":
    # 官方示例：["LRUCache","put","put","get","put","get","put","get","get","get"]
    #          [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))      # 1（1 被刷新到最前）
    cache.put(3, 3)          # 驱逐 2
    print(cache.get(2))      # -1
    cache.put(4, 4)          # 驱逐 1
    print(cache.get(1))      # -1
    print(cache.get(3))      # 3
    print(cache.get(4))      # 4