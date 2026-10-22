# Created by Chono-Hina at 2026/09/14 16:36
# leetgo: 1.4.18
# https://leetcode.cn/problems/lru-cache/

from typing import *
from leetgo_py import *

# @lc code=begin

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


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    capacity: int = deserialize("int", constructor_params[0])
    obj = LRUCache(capacity)

    for i in range(1, len(ops)):
        match ops[i]:
            case "get":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                ans = serialize(obj.get(key))
                output.append(ans)
            case "put":
                method_params = split_array(params[i])
                key: int = deserialize("int", method_params[0])
                value: int = deserialize("int", method_params[1])
                obj.put(key, value)
                output.append("null")

    print("\noutput:", join_array(output))
