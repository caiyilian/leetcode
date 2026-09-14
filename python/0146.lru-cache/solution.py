# Created by Chono-Hina at 2026/09/14 16:36
# leetgo: 1.4.18
# https://leetcode.cn/problems/lru-cache/

from typing import *
from leetgo_py import *

# @lc code=begin

class Node2dir:
    def __init__(self, x: int, key=None, next=None, prev=None):
        self.val = int(x)
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}
        self.count = 0
        self.capacity = capacity
        self.node_head = Node2dir(0)
        self.node_tail = Node2dir(0, prev=self.node_head)
        self.node_head.next = self.node_tail

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        curr = self.to_head(key)
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_dict:
            curr = Node2dir(value, key=key)
            self.cache_dict[key] = curr
            curr.next = self.node_head.next
            curr.prev = self.node_head
            self.node_head.next = curr
            curr.next.prev = curr
            self.count += 1
            if self.count > self.capacity:
                delete_key = self.node_tail.prev.key
                self.node_tail.prev = self.node_tail.prev.prev
                self.node_tail.prev.next = self.node_tail
                del self.cache_dict[delete_key]
                self.count -= 1
        else:
            self.cache_dict[key].val = value
            self.to_head(key)

    def to_head(self, key):
        curr = self.cache_dict[key]
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        curr.next = self.node_head.next
        curr.prev = self.node_head
        self.node_head.next = curr
        curr.next.prev = curr
        return curr
        

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
