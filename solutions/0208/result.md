# 208. 实现 Trie（前缀树）· 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 208. 实现 Trie（前缀树）（Implement Trie Prefix Tree）· 中等（数据结构设计） |
| 链接 | https://leetcode.cn/problems/implement-trie-prefix-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 16/16 用例通过** |
| 运行时间 | 44 ms（击败 67%） |
| 内存 | 33.8 MB |

## 两个版本（树版 vs set 模拟版，5 万步随机操作对拍 0 差异）

| 文件 | 版本 | startsWith 复杂度 | 实测（5 万词量 · 2000 次前缀查询） |
|------|------|------------------|--------------------------------|
| `solution.py` | **树版（定稿）**：WordNode(children dict + is_end) | **O(L)**（沿链走） | **0.73 ms** |
| `solution_readable.py` | set 模拟版（用户 v1） | O(N×L)（全量扫描） | 489.96 ms（**慢 667 倍**） |

**667 倍差距 = Trie 存在的意义**（共享前缀，前缀查询与词库大小无关）。

## 定稿（用户自驱：set 版 → 树版）

```python
class WordNode:
    def __init__(self):
        self.children = {}      # 字符 → 子节点
        self.is_end = False     # 完整单词结尾标记

class Trie:
    def __init__(self):
        self.root = WordNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = WordNode()
            p = p.children[c]
        p.is_end = True

    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_end          # ★ search 要求"完整单词"

    def startsWith(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True              # ★ startsWith 只要求"链走得通"
```

**208 唯一坑（用户一次避开）**：`search` 看 `is_end`（`search("app")` 在只插过 apple 时是 False），`startsWith` 不看（链存在即可）。

## 验证

- 对拍 **5 万步随机操作序列 vs set 参照 0 不一致**；
- 官方样例全对；性能实测 667 倍差距。

## 复杂度

- 树版：insert/search/startsWith 均 **O(L)**（L = 词长/前缀长）；空间 O(所有词的总字符数)（共享前缀）。

## 踩坑记录

- leetgo 模板自带三个空方法体，首次替换残留导致 IndentationError——已清理（本地 + 在线首次提交均 RTE，第二次通过）。