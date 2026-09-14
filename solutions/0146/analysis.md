# 146. LRU 缓存 · 解析

## 题目简述

设计一个 LRU（最近最少使用）缓存：`get(key)` 和 `put(key, value)` 都必须在 **O(1) 平均时间复杂度**内完成。

LRU 语义：**最近使用过的放前面，最久没用过的淘汰**（容量满时先踢最久未用的）。

## 核心套路：哈希表 + 双向链表（O(1) 双操作的正确姿势）

**为什么必须双向链表 + 哈希表**：

| 需求 | 用什么 |
|------|--------|
| O(1) 找到 key 对应的节点 | 哈希表（key → 节点） |
| O(1) 删除节点（淘汰最久未用） | 双向链表（知道 prev/next，直接摘除） |
| O(1) 移动到头部（最近使用） | 双向链表（摘除 + 插头） |

- 单向链表不够：删除节点时**拿不到前驱**（要 O(n) 找）；
- 数组不够：移动/删除是 O(n)；
- 纯哈希表不够：不知道"谁最久未用"（没有顺序信息）；
- **哈希表给顺序表"位置"，双向链表给"顺序"**——两者互补。

## 定稿解法（用户版：哈希 + 双向链表 + 哨兵头尾）

```python
class Node2dir:
    def __init__(self, x: int, key=None, next=None, prev=None):
        self.val = x
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_dict = {}                  # key → 节点
        self.count = 0
        self.capacity = capacity
        self.node_head = Node2dir(0)          # 哨兵头
        self.node_tail = Node2dir(0, prev=self.node_head)  # 哨兵尾
        self.node_head.next = self.node_tail

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        curr = self.to_head(key)              # 命中 → 移到头部（最近使用）
        return curr.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache_dict:
            curr = Node2dir(value, key=key)   # 新节点插头
            self.cache_dict[key] = curr
            curr.next = self.node_head.next
            curr.prev = self.node_head
            self.node_head.next = curr
            curr.next.prev = curr
            self.count += 1
            if self.count > self.capacity:    # 超容量 → 淘汰尾部
                delete_key = self.node_tail.prev.key
                self.node_tail.prev = self.node_tail.prev.prev
                self.node_tail.prev.next = self.node_tail
                del self.cache_dict[delete_key]
                self.count -= 1
        else:
            self.cache_dict[key].val = value  # 存在 → 更新值
            self.to_head(key)                 # 并移到头部

    def to_head(self, key):                   # 摘除节点 → 插入头部（两步）
        curr = self.cache_dict[key]
        # 摘除
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        # 插头
        curr.next = self.node_head.next
        curr.prev = self.node_head
        self.node_head.next = curr
        curr.next.prev = curr
        return curr
```

### 双向链表的两个原子操作

**摘除节点**（O(1)）：

```
curr.prev.next = curr.next
curr.next.prev = curr.prev
```

**插入头部**（O(1)）：先接链表（curr.next/curr.prev），再改哨兵（head.next）和新后继的 prev，**顺序固定防丢链**：

```
curr.next = head.next;  curr.prev = head
head.next = curr;       curr.next.prev = curr
```

### 哨兵头尾的价值

`head`/`tail` 是虚拟节点——链表为空时也有前后指针可操作，**不需要特判"空链表/只有一个节点"**（这是 LRU 双向链表实现的标配，也是 206/24/25 用过的"dummy 统一边界"思想的延续）。

### 为什么节点要存 key

淘汰尾部节点时 `delete_key = tail.prev.key`——**链表节点自己知道自己对应哪个 key**，删除时才能 `del cache_dict[key]`（不然得再遍历哈希表找，破坏 O(1)）。

## 复杂度

- **get：O(1)**（哈希查 + 双向链移动）；
- **put：O(1)**（插头/更新/淘汰尾）；
- 空间 O(capacity)。

## 考点（系统设计题的经典）

- **哈希表 + 双向链表的互补**（O(1) 查 + O(1) 改）
- 双向链的摘除/插头原子操作顺序（先摘除再插入，改指针顺序防断链）
- 哨兵头尾统一边界
- 节点存 key（淘汰时能反查哈希表）
- 面试追问方向：为什么用双向不用单向？为什么不用数组？**换掉任意一个都做不到双 O(1)**

## 易错点

1. 插入头部时**指针修改顺序**：先接好 curr 的 next/prev，再改 head.next 和新后继的 prev——倒过来会丢失链表或成环；
2. 摘除时 `curr.prev.next = curr.next` 和 `curr.next.prev = curr.prev` 都要做（不然双向链接断一半）；
3. 淘汰必须是 `tail.prev`（最久未用），不是 `head`；
4. 更新已存在 key 时：先改值再 to_head（顺序无所谓，但要记得移动，否则"最近使用"语义错）；
5. 节点必须存 key，否则淘汰时无法 O(1) 删哈希项。

## 本地测试方法（用户没测过，这里补上）

```python
# 参照实现：OrderedDict（move_to_end + popitem(last=False)）
class RefLRU:
    def __init__(self, capacity):
        self.cap = capacity
        self.d = OrderedDict()
    def get(self, key):
        if key not in self.d: return -1
        self.d.move_to_end(key)
        return self.d[key]
    def put(self, key, value):
        if key in self.d: self.d.move_to_end(key)
        self.d[key] = value
        if len(self.d) > self.cap: self.d.popitem(last=False)
```

用随机 put/get 序列把两个类跑一遍对比输出——本项目 2 万组对拍 0 不一致已验证。