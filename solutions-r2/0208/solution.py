"""208. 实现 Trie (前缀树)（二刷）——字典子节点（O(L)/O(节点数) 标准解）

用户 AC 版（2026-10-29 15:01 提交 757596938，WA→AC 修复，47ms/33.9MB）
- 每个节点：next 字典（字符→子节点）+ is_end 标记
- search 要求完整单词（查 is_end）；startsWith 只要求链走得通
- ⚡⚡ 经典踩坑：MyNode(next={}) 可变默认参数 → 所有实例共享同一个 dict（跨实例污染）
  修复：def __init__(self, is_end=False): self.next = {}（在函数体内新建）
"""


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

if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))        # True
    print(t.search("app"))          # False
    print(t.startsWith("app"))      # True
    t.insert("app")
    print(t.search("app"))          # True
    # 跨实例隔离验证（修复可变默认参数的标志）
    t2 = Trie()
    print(t2.startsWith("a"))       # False（修复前会 True——共享dict污染）