# -*- coding: utf-8 -*-
"""
第 208 题 实现 Trie（前缀树）· set 模拟版（用户 v1，仅作对比）
逻辑正确（5 万步随机操作对拍 0 差异），但 startsWith 每次 O(N×L) 全量扫描。
实测：5 万单词量下 2000 次前缀查询 —— 树版 0.73ms vs 本版 489.96ms（慢 667 倍）。
Trie 的价值 = 共享前缀，前缀查询与词库大小无关。
"""


class Trie:

    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        for word in self.words:
            if word.startswith(prefix):
                return True
        return False