# 21. 合并两个有序链表 · 解析（二刷）

## 一、核心思路：哨兵 + 逐个挑选

两条有序链表要合成一条有序的，最直观的"归并"：

```
两个指针各指一条链的头部
每轮挑 val 较小的节点接进结果链，指针后移
某条走空 → 把另一条剩余整段接上
```

**哨兵节点（dummy）**解决"结果链头是谁"的讨论——无论第一个接的是 list1 还是 list2，都是 `dummy.next`，最后 `return dummy.next` 统一返回。

```
dummy(0) -> ...
  p  ← 游标，永远指向结果链尾部
```

## 二、代码骨架（用户版）

```python
result = ListNode(0)   # 哨兵
p = result             # 记住头，最后返回 p.next

while list1 or list2:              # 还有节点没接完
    if list1 is None:              # list1 空了 → 整段接 list2
        result.next = list2
        list2 = list2.next
    elif list2 is None:            # list2 空了 → 整段接 list1
        result.next = list1
        list1 = list1.next
    else:                          # 都没空 → 挑小的
        if list1.val <= list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
    result = result.next           # 游标前进
return p.next
```

## 三、为什么 O(1) 空间

只新建了一个哨兵节点；其余全部是**改指针指向**（把原链表的节点重新串起来），没有复制任何节点——这就是链表归并比数组归并省空间的原因。

## 四、复杂度

- 时间：O(n+m)——每个节点恰好被接一次
- 空间：O(1)

## 五、一刷 vs 二刷

| | 一刷（9-13） | 二刷（10-19） |
|---|---|---|
| 打法 | 交换头 + 插入法，无 dummy | **哨兵 + 循环逐个接** |
| 结果 | AC ×2 | **一次 AC** |
| 通用性 | 特定于"两条链" | 标准归并，23 题分治直接复用 |

**二刷换打法 = 刻意练习**：同一道题用两种思路各做一遍，覆盖的知识点更多（交换头 trick vs 哨兵范式）。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| 哨兵节点 | **23 合并 K 个升序链表**（每轮 merge 就是本题）、2 两数相加 |
| 归并思想 | 88 合并两个有序数组（数组版，需从后往前）、148 排序链表（归并排序链表版） |
| 递归版 | 本题官方还有递归写法（return list1 if list1.val < list2.val else ...），空间 O(n+m) 栈深 |

## 七、一句话记住

> **合并两个有序链表 = 哨兵 dummy + 双指针循环挑小值接上，某条空了整段接另一条，时间 O(n+m) 空间 O(1)；dummy 统一"头是谁"的讨论。**
