# 138. 随机链表的复制 · 解析（二刷）

## 一、核心思路：难点只在 random，解法是"映射"

普通链表复制 = 跟着 next 走一遍、一节点造一节点，简单。**难在 random**：它指向"原链表的某个节点"，而你要返回的是一批**全新的节点**——random 不能照抄（照抄就指回原链了），必须回答"原节点的 random 对应哪个新节点"。

**答案：哈希映射"原节点 → 新节点"。**

```
原链:  7 → 13 → 11 → 10 → 1
       ↑    ↑↑    ↑     ↑
hash_map: {7→新7, 13→新13, 11→新11, 10→新10, 1→新1, None→None}
```

- 复制 next 时顺手建映射（每个原节点对应一个新节点）；
- 第二遍遍历，`new.random = hash_map[p.random]`——按原节点的 random 查表，拿到对应的新节点。

## 二、两遍法代码骨架

```python
hash_map = {None: None}        # ★ 预置：random=None 也能查
p = head
dummy = Node(0)
prev = dummy
while p:                        # ① 复制 next 链 + 建映射
    new = Node(p.val)
    prev.next = new
    prev = new
    hash_map[p] = new
    p = p.next                  # ★ 别忘前进！忘了会死循环 MLE
p = head
new = dummy.next
while p:                        # ② 按映射补 random
    new.random = hash_map[p.random]
    new = new.next
    p = p.next
return dummy.next
```

## 三、深拷贝三验证点（面试可能追问怎么测）

| 验证点 | 方法 |
|--------|------|
| 值链一致 | 走一遍副本，值与原链相同 |
| 非同一对象 | `copy is not orig`（新节点是独立对象） |
| random 相对位置一致 | `copy.random` 与 `orig.random` 指向的**相对位置**相同（不能指回原链） |

## 四、两个坑（用户踩过，已修复）

1. **`{None: None}` 预置**：`p.random` 可能是 None，hash_map 没有 None 键会 KeyError——空值映射先放进去；
2. **忘 `p = p.next`**：第一个 while 死循环，同一节点无限复制 → 内存超限（MLE）。链表遍历，"前进"是保命行。

## 五、进阶：交错法 O(1) 空间（力扣 follow-up）

哈希表版空间 O(n)，力扣追问 O(1)。**核心：用"位置"代替哈希表**——新节点直接插在原节点后面，`原.next` 就是它的拷贝，映射关系由链表结构本身承载。

**第 1 步：穿插**

```
原链:  1 → 2 → 3
交错:  1 → 1' → 2 → 2' → 3 → 3'
```

每遍历一个原节点，就在它后面插一个拷贝：`clone.next = cur.next; cur.next = clone; cur = clone.next`。

**第 2 步：补 random**（最关键的一行）

```
1.random = 3   交错后：1' 在 1 后面，3' 在 3 后面
cur.next.random = cur.random.next
```

`cur.next` 是 cur 的拷贝，`cur.random.next` 是"cur.random 指向的节点"的拷贝（就在它后面）。所以一行搞定，无需查表。**random = None 时守卫**（`if cur.random:`）。

**第 3 步：拆链**

```
交错:  1 → 1' → 2 → 2' → 3 → 3'
原链:  1 → 2 → 3        （奇数位，恢复原样）
新链:  1' → 2' → 3'      （偶数位，返回值）
```

**拆链坑**：先保存 `clone.next` 再断开（`cur.next = clone.next; clone.next = clone.next.next`），否则拆着拆着另一条链也断了。

**为什么能 O(1)**：找拷贝 = 走一步 next（结构承载映射），不再需要哈希表。

## 六、复杂度

- 哈希版：时间 O(n) / 空间 O(n)
- 交错法：时间 O(n) / 空间 O(1)

## 七、一刷 vs 二刷

- 一刷（9-14）：同样哈希两遍法，AC ×2；另归档 O(1) 交错法版；
- 二刷（10-20）：无思路 → 提示后独立写出，一次 AC，还踩了两个新坑（None 键、忘前进）；**本次把交错法补进二刷归档**——"用结构代替哈希"的范例。

## 八、关联题目

| 套路 | 相关题 |
|------|--------|
| 深拷贝 | 133 克隆图（同样"原→新映射"，图版） |
| 哈希映射"原→新" | 148 排序链表（借助 map 的变体）、437 路径总和（前缀和映射） |
| 交错法（O(1)） | 本题进阶；同类"结构代替哈希"：287 寻找重复数（Floyd 判圈） |

## 九、一句话记住

> **随机链表复制 = 哈希表记"原节点→新节点"（O(n) 空间）；进阶 O(1) 用交错法——新节点插在原节点后（位置即映射），`cur.next.random = cur.random.next` 补 random，最后拆成两条链。**
