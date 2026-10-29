# 208. 实现 Trie (前缀树) · 解析（二刷）

## 一、Trie（前缀树/字典树）是什么

多叉树，每条**边代表一个字符**，**路径 = 单词**：

```
        (root)
        /  \
       a    b
      /      \
     p        a
    / \        \
   p   r        d
      /          \
     l            y  ← is_end
    /
   e  ← is_end
```

- insert("apple")：走 a→p→p→l→e，末尾节点 `is_end = True`；
- search("app")：走 a→p→p，**最后一个节点 is_end = False** → False（"app" 不是完整单词）；
- startsWith("app")：走 a→p→p，链走得通 → True。

**核心**：`search` 要完整单词（查 is_end），`startsWith` 只要前缀（链通即可）。

## 二、代码（用户 AC 版）

```python
class MyNode:
    def __init__(self, is_end=False):
        self.next = {}        # ⚡ 函数体内新建（别用默认参数 next={}！）
        self.is_end = is_end

class Trie:
    def __init__(self):
        self.head = MyNode()

    def insert(self, word):
        p = self.head
        for c in word:
            if c not in p.next:
                p.next[c] = MyNode()   # 缺边建节点
            p = p.next[c]
        p.is_end = True                # 末尾打标记

    def search(self, word):
        p = self.head
        for c in word:
            if c in p.next:
                p = p.next[c]
            else:
                break
        else:                          # for-else：没 break（链走通）才进
            return p.is_end            # ★ 完整单词要求
        return False

    def startsWith(self, prefix):
        p = self.head
        for c in prefix:
            if c in p.next:
                p = p.next[c]
            else:
                break
        else:
            return True                # 只要链通
        return False
```

## 三、⚡⚡ 经典坑：可变默认参数（本主题材核心）

```python
# 错误
def __init__(self, next={}, is_end=False):   # 默认参数只在定义时求值一次！
    self.next = next                          # 所有实例共享同一个 dict

# 正确
def __init__(self, is_end=False):
    self.next = {}                            # 每实例各自新建
```

**现象**：本地单用例通过，力扣多用例 WA（隐藏用例 `startsWith("a")` 等诡异错乱）。
**机制**：默认 dict 只创建一次 → 所有节点的 `next` 是同一个字典 → 跨节点/跨实例污染。
**修复**：函数体内 `self.next = {}` 或 `next=None` + 体内建。

**记忆口诀**：**可变对象绝不写默认参数**（dict/list/set/Nodes 同理）。这是 Python 高频笔试坑，Trie/链表/树节点类最容易中。

## 四、复杂度

- 时间：insert/search/startsWith 均 **O(L)**（L = 单词长度），与树中已有单词量无关（这是 Trie 相对 set 的优势）；
- 空间：O(字符总数 × 每节点 dict 开销)。

## 五、一刷 vs 二刷

- 一刷（9-16）：字典子节点，WA×3（当时也是边界/结构问题）后 AC ×2；
- 二刷（10-29）：功能逻辑一次写对，栽在**可变默认参数**——这比算法本身更值得记（力扣隐藏用例专治这种"本地没事线上炸"）。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| Trie 应用 | **211 添加与搜索单词**（DFS 通配符 .）、212 单词搜索 II（Trie+回溯剪枝）、648 单词替换 |
| 前缀思想 | 14 最长公共前缀、前缀和（560/437 的"前缀"联想） |
| 字典替代 | 哈希表 vs Trie（Trie 省空间、前缀友好） |

**208 是实现类母题**：211（search 支持 '.'）、212（Trie 加速单词搜索）都建在它上面。

## 七、一句话记住

> **Trie = 字典子节点 + is_end：insert 走链打标，search 查完整单词（is_end），startsWith 只查链通；⚡ 可变对象禁用默认参数（next={} 会共享），函数体内新建。**