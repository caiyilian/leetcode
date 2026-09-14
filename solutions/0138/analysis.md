# 138. 随机链表的复制 · 解析

## 题目简述

给你一个长度为 n 的链表，每个节点除了 `next` 还有一个**随机指针 `random`**（可以指向链表中的任意节点或 null）。要求**深拷贝**：构造一个全新链表，值相同、结构相同，但节点完全是新建的（random 指向新链的对应节点）。

> 深拷贝 vs 浅拷贝：浅拷贝复用原节点（改一处影响两边）；深拷贝必须全部新建。

## 核心套路一：哈希映射两遍法（O(n) 空间，标准答案）

**难点**：第一遍建链时，新节点的 `random` 该指向谁？——原链的 random 指向原节点，但拷贝必须指向**新链**的对应节点，而这个节点可能还没建出来。

**解法**：先不管 random，第一遍建链时记录 `原节点 → 新节点` 映射表；第二遍用映射表把 random "翻译"成新节点：

```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0)
        p_d = dummy
        p = head
        hash_dict = {}
        while p:                              # 第一遍：建链 + 映射
            p_d.next = Node(p.val)
            p_d = p_d.next
            hash_dict[p] = p_d                # 原节点 → 新节点
            p = p.next
        for key, value in hash_dict.items():  # 第二遍：补 random
            value.random = hash_dict.get(key.random, None)   # get(..., None) 处理 random=None
        return dummy.next
```

**要点**：`hash_dict.get(key.random, None)`——`key.random` 为 None 时返回 None（新节点 random 就是 None），否则返回对应的新节点。**原节点用哈希（引用相等）而非值相等**——链表可能含重复值，必须按节点身份映射。

## 核心套路二：节点交错法（O(1) 额外空间，满足 follow-up）

不用哈希表，利用"拷贝插在原节点后面"的位置关系：

```
① 插入拷贝：A → A' → B → B' → ...（每个原节点后紧跟它的拷贝）
② 补 random：A'.random = A.random.next（原 random 的拷贝就在它后面！）
③ 拆开：奇数位还原原链，偶数位组成新链
```

```python
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        # ① 插入拷贝
        cur = head
        while cur:
            clone = Node(cur.val)
            clone.next = cur.next
            cur.next = clone
            cur = clone.next
        # ② 补 random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next   # 原 random 的拷贝紧跟在后面
            cur = cur.next.next
        # ③ 拆开
        new_head = head.next
        cur = head
        while cur:
            clone = cur.next
            cur.next = clone.next
            clone.next = clone.next.next if clone.next else None
            cur = cur.next
        return new_head
```

**为什么 ② 成立**：`A.random` 指向原链的 X，而 X 的拷贝 X' 就在 X 后面（`X.next`）——所以 `A'.random = A.random.next = X'` ✅。这就是"交错"的妙处：**拷贝天然能通过一步找到目标拷贝**。

## 两版对比

| | 哈希映射法 | 节点交错法 |
|--|-----------|-----------|
| 空间 | O(n)（哈希表） | **O(1)** ✅ follow-up |
| 思路 | 显式映射表 | 隐式位置关系（拷贝在右侧） |
| 代码 | 简洁直观 | 三步较绕（拆开那步易错） |
| 首选场景 | 面试快速实现 | 面试官追问 O(1) 空间时 |

## 深拷贝的三验证点（面试官判题标准）

1. **值序列一致**（每个节点 val 相同）；
2. **结构一致**（random 的相对索引相同——如原链第 0 个的 random 指向第 2 个，新链也必须如此）；
3. **完全独立**（新链节点是新对象；random 指向新链节点，不指向原链——`id()` 对比验证）。

光"跑通"不够，**第 3 点才是深拷贝的灵魂**（错误实现会直接复用原节点）。

## 复杂度

- 哈希法：O(n) 时间 + O(n) 空间；
- 交错法：O(n) 时间 + **O(1) 空间**（满足 follow-up）。

## 考点

- 深拷贝语义（三验证点）
- **引用映射**（哈希键用节点对象本身，不用值）
- 位置关系利用（交错法的"拷贝在右侧"）
- 与 133 克隆图、148 排序链表（都涉及"节点对应关系"）的联系

## 易错点

1. 哈希键必须是节点对象（`hash_dict[p]`），不能用 `p.val`（重复值会冲突）；
2. 第二遍遍历 `hash_dict.items()` 时 key 是**原节点**（不是新节点）——`key.random` 取的是原链的 random；
3. 交错法拆开时：先保存 `clone.next` 再改，否则断链；
4. random 为 None 时不能访问 `.next`（`if cur.random:` 守卫）。