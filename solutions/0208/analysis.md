# 208. 实现 Trie（前缀树）· 解析

## 题目简述

实现一个前缀树 `Trie`，支持 `insert`（插入单词）、`search`（查完整单词）、`startsWith`（查前缀是否存在）。

## 核心套路：Trie = 字符边 + is_end 标记

**Trie 是一棵多叉树**，但和二叉树不同——**边是字符，节点不存值**：

```
        (root)
      /   |    \
     a    b     c          ← 边是字母，节点本身不存字母
    /      \
   p        e
  / \        \
 p   r        e
 |            |
 l            r          ← apple / app / beer / appr...
 e
```

**两个设计点**：

1. **`children`：字符 → 子节点**（dict 或 26 位数组）——从根出发，每个字符走一步；
2. **`is_end`：这个节点是不是某个完整单词的结尾**——`insert("apple")` 后，只有走到最后的 `e` 节点 `is_end=True`；中间的 `a/p/p/l` 都不是完整词。

**搜索区分**（208 唯一的坑）：

```
search("app")      → 沿 a→p→p 走到 p 节点，is_end=False → False
                     （"app" 不是插入过的完整单词）
startsWith("app")  → 沿 a→p→p 能走通 → True（不管是否完整词）
```

## 完整实现（用户定稿）

```python
class WordNode:
    def __init__(self):
        self.children = {}      # 字符 → 子节点
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = WordNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:     # 没有这条"边"就新建
                p.children[c] = WordNode()
            p = p.children[c]           # 沿边走
        p.is_end = True                 # 结尾打标

    def search(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                return False
            p = p.children[c]
        return p.is_end                 # ★ 完整词才 True

    def startsWith(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p.children:
                return False
            p = p.children[c]
        return True                     # ★ 链走得通就 True
```

三个方法共享同一个"沿链走"的骨架——唯一区别在最后一行（search 看 is_end / startsWith 直接 True）。

## 演进：set 模拟版 → 树版（用户自驱，实测 667 倍）

### set 版（逻辑正确但 startsWith 是灾难）

```python
class Trie:
    def __init__(self):
        self.words = set()          # 不是树！
    def startsWith(self, prefix):
        for word in self.words:     # O(N×L)：每次全量扫描
            if word.startswith(prefix):
                return True
        return False
```

**实测**（5 万单词量，2000 次前缀查询）：set 版 **489.96ms** vs 树版 **0.73ms**——**慢 667 倍**。

**为什么树版快**：前缀查询只关心"从根出发这条链存不存在"——每走一步的查找是 dict O(1)，总 O(L)，**和词库有多少词完全无关**。set 版每次都要过一遍全部 N 个词。这就是"共享前缀"的价值：`apple` 和 `apply` 共用 `appl` 这一段。

### 为什么 children 用普通 dict 而不是 defaultdict(WordNode)

- 普通 dict + `if c not in p.children` 显式判断：行为可控，`in` 不触发默认工厂；
- `defaultdict` 的隐患：若在只读路径（如 search）误写 `p.children[c]`，会**自动创建空节点污染树**，bug 极难排查；
- 结论：显式 dict 判断是标准最优写法。

## 复杂度

- 三个操作均 **O(L)**（L = 词长/前缀长）；
- 空间 **O(总字符数)**（所有插入单词的字符数之和，共享前缀部分不重复计算）。

## 考点

- 前缀树结构（字符边 + is_end）
- **search vs startsWith 的区分**（is_end 标记）
- 共享前缀的空间/时间优势（vs set/字典）
- 数据结构的"模拟实现"与"真实现"的差距（set 版只是语义正确）

## 易错点

1. **search 不看 is_end**——`search("app")` 会错误返回 True（只插过 apple）；
2. children 用数组（26 位）时下标 = `ord(c) - ord('a')`，别忘了边界；
3. 空字符串：`insert("")` 应设 root.is_end=True（力扣测例不含，但知道更稳）；
4. startsWith 与 search 骨架相同但返回不同——别复制错最后一行；
5. 递归 vs 迭代：迭代沿链走最直接，无需递归。

## 关联题

- **211 添加与搜索单词**：Trie + 通配符 `.`（DFS 回溯）；
- **648 单词替换**：Trie 找最短前缀；
- **14 最长公共前缀**：也可用 Trie 解；
- 与 208 一起构成"Trie 三件套"。