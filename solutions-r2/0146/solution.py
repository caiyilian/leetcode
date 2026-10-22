"""146. LRU 缓存（二刷）——哈希 + 双向链表 + 哨兵头尾（get/put 均 O(1) 最优解）

主版（标准）：节点带 key 字段，单哈希表（key→node）
- 用户 AC 版（2026-10-22 19:54 提交 756403025）最初用双哈希表（hash_map + hash_map2[node]=key）
- 标准写法：节点自己记住 key，驱逐时 tail.key 直接拿 key，省一张表
- 结构：hash_map: key → 节点；双向链表维护访问顺序（头=最近使用，尾=最久未用）
- 哨兵 forward/backward 消除空链表/头尾特判
- get：命中则移到最前（摘除 → 插 forward 后）并返回值；put：已有则更新+前移，新键插入最前、满则删尾
- 空间 O(capacity)
"""


class ListNode2:
    def __init__(self, val=0, key=None, next=None, before=None):
        self.val = val
        self.key = key          # ★ 节点记住自己的 key
        self.next = next
        self.before = before


# ========== 主版：节点带 key 标准版（单哈希表） ==========
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.forward = ListNode2()          # 哨兵头（next 指向最近使用）
        self.backward = ListNode2()         # 哨兵尾（before 指向最久未用）
        self.forward.next = self.backward
        self.backward.before = self.forward
        self.hash_map = {}                 # key → 节点（唯一一张表）
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self._move_to_head(node)
        else:
            node = ListNode2(value, key=key)
            self.hash_map[key] = node
            self._insert_to_head(node)
            if self.count == self.capacity:
                # 驱逐最久未用（backward 前一个）
                delete_node = self.backward.before
                delete_node.before.next = self.backward
                self.backward.before = delete_node.before
                self.hash_map.pop(delete_node.key)   # ★ 直接用节点里的 key
            else:
                self.count += 1

    def _move_to_head(self, node):
        """摘除 + 插到头（get 命中 / put 更新时用）"""
        before_node = node.before
        next_node = node.next
        before_node.next = next_node
        next_node.before = before_node
        self._insert_to_head(node)

    def _insert_to_head(self, node):
        """插到 forward 后（最新）"""
        node.before = self.forward
        node.next = self.forward.next
        self.forward.next.before = node
        self.forward.next = node


# ========== 对照版：用户 AC 版（双哈希表 hash_map + hash_map2[node]=key） ==========
class LRUCacheUserTwoMaps:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.forward = ListNode2()
        self.backward = ListNode2()
        self.forward.next = self.backward
        self.backward.before = self.forward
        self.hash_map = {}
        self.hash_map2 = {}                # node → key（驱逐时反向找 key）
        self.count = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        before_node = node.before
        next_node = node.next
        before_node.next = next_node
        next_node.before = before_node
        node.before = self.forward
        node.next = self.forward.next
        self.forward.next.before = node
        self.forward.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            before_node = node.before
            next_node = node.next
            before_node.next = next_node
            next_node.before = before_node
            node.before = self.forward
            node.next = self.forward.next
            self.forward.next.before = node
            self.forward.next = node
        else:
            node = ListNode2(value)
            self.hash_map[key] = node
            self.hash_map2[node] = key
            node.before = self.forward
            node.next = self.forward.next
            self.forward.next.before = node
            self.forward.next = node
            if self.count == self.capacity:
                delete_node = self.backward.before
                delete_node.before.next = self.backward
                self.backward.before = delete_node.before
                self.hash_map.pop(self.hash_map2[delete_node])
            else:
                self.count += 1


if __name__ == "__main__":
    for cls in (LRUCache, LRUCacheUserTwoMaps):
        print(f"--- {cls.__name__} ---")
        # 官方示例：["LRUCache","put","put","get","put","get","put","get","get","get"]
        cache = cls(2)
        cache.put(1, 1)
        cache.put(2, 2)
        print(cache.get(1))      # 1（1 被刷新到最前）
        cache.put(3, 3)          # 驱逐 2
        print(cache.get(2))      # -1
        cache.put(4, 4)          # 驱逐 1
        print(cache.get(1))      # -1
        print(cache.get(3))      # 3
        print(cache.get(4))      # 4
