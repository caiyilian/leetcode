# 24. 两两交换链表中的节点 · 解析（二刷）

## 一、核心思路：三指针 + dummy

每轮要交换 `p1` 和 `p2`（相邻一对），用 `prev` 记住"这对节点之前的那个节点"：

```
dummy → 1 → 2 → 3 → 4
  ↑prev    ↑p1  ↑p2

交换后：
dummy → 2 → 1 → 3 → 4
        ↑p2  ↑p1
prev 前进到 p1（交换后的"下一对的前驱"）
```

三个赋值完成交换（顺序不能乱）：

```python
prev.next = p2      # 1. 前驱指向 p2（2）
p1.next = p2.next   # 2. p1 指向 p2 后面的（3）
p2.next = p1        # 3. p2 指向 p1（完成 2↔1）
prev = p1           # 4. 前驱前进到 p1（=下一轮的 dummy）
```

## 二、为什么用 dummy

交换头两个节点时，头节点没有"前驱"——dummy 虚拟一个，让每轮交换的逻辑完全一致，`return dummy.next` 统一返回新头。**链表头会变的题目，dummy 是标配**（2/19/21/23/25 同理）。

## 三、循环条件：把 break 吸收进来（本次优化点）

用户 AC 版：

```python
while prev and prev.next:
    p1 = prev.next
    p2 = p1.next
    if p2 is None:    # 没有完整一对 → 退出
        break
    ...
```

优化版：

```python
while prev.next and prev.next.next:   # 有 p1 且有 p2 才进
    p1 = prev.next
    p2 = p1.next
    ...
```

- `prev.next` 存在 = 有 p1；`prev.next.next` 存在 = 有 p2；
- `prev` 本身永不为 None（dummy 起步，之后是 p1），无需检查；
- **"否条件提前 break" → "正条件进入循环"**，同一个意思，但后者免去循环内的分支判断，代码结构更平。

## 四、奇数长度怎么办

奇数个节点时，最后一轮 `prev.next.next` 为 None，循环自然退出——**末尾孤单个节点保持不动**，天然正确，无需特判（`[1,2,3]` → `[2,1,3]`）。

## 五、复杂度

- 迭代版：时间 O(n) / 空间 O(1)
- 递归版：时间 O(n) / 空间 O(n)（栈深 n/2，约等于 O(n)）

## 六、一刷 vs 二刷

- 一刷（9-13）：四指针 + `while True`，跳出靠 `break`（"先干再问用 break"）；
- 二刷（10-19）：dummy + 三指针 + `while prev.next and prev.next.next` 条件化——**一刷的 break 这次自己吸收进条件了**，还主动提出"break 可能能优化"，代码嗅觉在进步。

## 七、关联题目

| 套路 | 相关题 |
|------|--------|
| dummy + 三指针改链接 | **25 K 个一组翻转链表**（本题的 k=2 特例，翻倍难度）、206 反转链表 |
| 递归交换 | 21 合并两个有序链表（递归版）、25（递归+迭代混合） |
| 头会变的链表 | 2 / 19 / 21 / 23 / 25（全都要 dummy） |

## 八、一句话记住

> **两两交换 = dummy + 三指针三连改（prev→p2, p1→p2.next, p2→p1），prev 前进到 p1；循环条件 `while prev.next and prev.next.next` 把"没有一对就退出"吸收进来，奇数末尾自动不动。**