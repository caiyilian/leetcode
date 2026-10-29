# Created by Chono-Hina at 2026/09/16 12:11
# leetgo: 1.4.18
# https://leetcode.cn/problems/implement-trie-prefix-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class MyNode:
    def __init__(self, is_end=False):
        self.next = {}        # ⚡ 必须函数体内新建（不能用默认参数 next={}！）
        self.is_end = is_end


class Trie:

    def __init__(self):
        self.head = MyNode()

    def insert(self, word: str) -> None:
        p = self.head
        for c in word:
            if c not in p.next:
                p.next[c] = MyNode()
            p = p.next[c]
        p.is_end = True

    def search(self, word: str) -> bool:
        p = self.head
        for c in word:
            if c in p.next:
                p = p.next[c]
            else:
                break
        else:
            # 没有break，看看有没有is_end（存了apple但找app → False）
            return p.is_end
        return False          # 存了app但找apple → False

    def startsWith(self, prefix: str) -> bool:
        p = self.head
        for c in prefix:
            if c in p.next:
                p = p.next[c]
            else:
                break
        else:
            return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Trie()

    for i in range(1, len(ops)):
        match ops[i]:
            case "insert":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                obj.insert(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)
            case "startsWith":
                method_params = split_array(params[i])
                prefix: str = deserialize("str", method_params[0])
                ans = serialize(obj.startsWith(prefix))
                output.append(ans)

    print("\noutput:", join_array(output))
