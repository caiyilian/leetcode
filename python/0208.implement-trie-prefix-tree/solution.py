# Created by Chono-Hina at 2026/09/16 12:11
# leetgo: 1.4.18
# https://leetcode.cn/problems/implement-trie-prefix-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class WordNode:
    def __init__(self):
        self.children = {}      # 字符 → 子节点（普通 dict + 显式判断，最稳）
        self.is_end = False     # 是否是一个完整单词的结尾


class Trie:

    def __init__(self):
        self.root = WordNode()

    def insert(self, word: str) -> None:
        p = self.root
        for c in word:
            if c not in p.children:        # 没有这个字母，就新建节点
                p.children[c] = WordNode()
            p = p.children[c]
        p.is_end = True                    # 结尾标记

    def search(self, word: str) -> bool:
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_end                    # 要求"完整单词"（208 唯一坑）

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True                        # 只要求"链走得通"

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
