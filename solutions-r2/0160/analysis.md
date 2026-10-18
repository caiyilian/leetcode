# 160. 相交链表 · 解析（二刷）

## 一、核心思路：双指针换边（路程相等）

两个指针同时出发：
- `pA` 从 headA 走，走到 None 换到 headB 继续；
- `pB` 从 headB 走，走到 None 换到 headA 继续。

**关键**：两个指针最终都走了 `lenA + lenB` 步（路程相等）：

```
A = 4 → 1 → 8 → 4 → 5     B = 5 → 0 → 1 → 8 → 4 → 5
pA: 4 1 8 4 5(None) 5 0 1 8 → 相遇在 8 ✅
pB: 5 0 1 8 4 5(None) 4 1 8 → 相遇在 8 ✅
```

- **相交**：进入共享段后两指针同路，必然相遇（交点即答案）；
- **不相交**：两指针同时走到 None，返回 None。

**为什么必须换边**：直接走"本链"的话，长度差让两指针永远错位；换边后**路程差被抹平**——pA 多走的 lenB 恰好补在 B 上，pB 多走的 lenA 补在 A 上，两人"汇合"。

## 二、两种写法

```python
# 写法 A（用户 AC 版）：
pA, pB = headA, headB
while pA or pB:
    if pA is None: pA = headB
    if pB is None: pB = headA
    if pA is pB: return pA      # ★ 先判断再移动
    pA = pA.next; pB = pB.next
return None

# 写法 B（标准版，更稳）：
if not headA or not headB: return None
pA, pB = headA, headB
while pA is not pB:
    pA = pA.next if pA else headB
    pB = pB.next if pB else headA
return pA
```

B 的好处：空链表天然安全（不用特判也能正确返回 None），循环退出条件就是答案，代码更短。

## 三、两个坑（二刷实证）

### 坑 1：判断 vs 移动的顺序（WA→AC 根因）

**必须"先检查当前节点、再前进"**——若先 `next`，交点恰好在当前节点（尤其换边后的第一节点）时会被跳过。22% 的随机用例会错。

### 坑 2：空链表隐藏 bug（力扣没测到）

`headA=None` 时，写法 A 会在第一轮把 pA 换成 headB，而此时 pB 还是 headB → 误判相交。**先判空或用写法 B 的 `while pA is not pB` 免疫**。

## 四、复杂度

- 时间：O(m+n)（两指针各走满 lenA+lenB）
- 空间：O(1)

## 五、一刷 vs 二刷

- 早期/一刷：双指针换边定稿（多次提交）；
- 二刷（10-18）：WA（先移动）→ AC（先判断），**"判断与移动顺序"这个链表通用坑自己踩出**。

## 六、关联题目（配套复习）

- **141 环形链表 / 142 环形链表 II**：同款快慢指针"相遇"思想；
- **19 删除链表的倒数第 N 个结点**：快慢指针 + 先走 N 步（同款指针节奏控制）；
- **链表的通用心法**：指针题先明确"检查当前 vs 前进"的时机。

## 七、一句话记住

> **相交链表 = 双指针换边抹平长度差（路程相等必相遇）；先判断当前节点再移动；空链表先判空或 while pA is not pB 免疫。O(m+n)/O(1)。**