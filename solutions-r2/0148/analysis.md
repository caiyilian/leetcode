# 148. 排序链表 · 解析（二刷）

## 一、核心思路：链表版归并排序

数组排序能用快排/堆排，但链表**随机访问是 O(1) 步进**，快排的"选 pivot 分区"不方便（要多次遍历）。归并排序只需要"切两半 + 合并两条有序链"，**天然适配链表**。

```
sortList([4,2,1,3])
  切两半：[4,2] | [1,3]
  递归：[2,4] | [1,3]
  合并：[1,2,3,4]
```

三步：
1. **快慢指针找中点** → 把链表从中间切断成两条（`prev.next = None`）；
2. **递归排序左右两半**；
3. **merge_node 合并两条有序链**（= 21 题，哨兵归并）。

## 二、组件全是做过的题（刷题复利）

| 组件 | 来自哪题 |
|------|---------|
| 快慢指针找中点 + 切断 | 141/142/234 的 find_mid，加一行 `prev.next = None` |
| 合并两个有序链 | **21 题**（merge_node 几乎原样复用） |
| 分治（切半递归） | **23 题**分治合并、归并排序的通用骨架 |

**148 = 141(找中点) + 21(合并) + 递归分治**——没有新知识，全是旧套路拼装。

## 三、切中点的细节（和"找中点"题的区别）

普通找中点（141/234）不需要切断，快慢指针停在中点即可；**排序需要切断**，所以：

```python
def get_half(p):
    p_slow = p
    p_fast = p
    prev = p
    while p_fast and p_fast.next:
        p_fast = p_fast.next.next
        prev = p_slow
        p_slow = p_slow.next
    prev.next = None        # ★ 切断：左半 [p..prev]，右半 [p_slow..]
    return p, p_slow
```

`prev` 记录慢指针前驱，循环结束 `prev` 正是左半的最后一个节点，`prev.next = None` 一断两半。

## 四、空链表守卫（本次插曲）

`fun` 的递归基是 `if p.next is None: return p`——只处理**单节点**。空链表（`p = None`）会直接 `None.next` 崩溃。所以入口必须有：

```python
def sortList(self, head):
    if not head:      # ★ 空链表守卫（默认开场动作）
        return head
    ...
```

**共性**：递归/分治类链表题，入口空守卫 + 递归基单节点，是两个必须同时写对的边界（一刷 148 也踩过 RE）。

## 五、复杂度与进阶

- 时间：O(n log n)
- 空间：**递归版 O(log n)**（递归栈）——力扣进阶要求 O(1)，严格说不满足；
- **进阶 O(1) 解法：自底向上归并**——从"1 个节点一组"开始两两合并、2 个一组、4 个一组……迭代完成，不用递归栈。

## 五点五、自底向上归并详解（O(1) 空间）

**核心区别**：递归版"先切到底再拼上来"（空间 O(log n)），自底向上版"从一开始就拼、段长逐层翻倍"（纯迭代 O(1)）。

```
step=1:  [4] [2] [1] [3]     单节点天然有序
         → merge 两两 → [2,4] [1,3]
step=2:  [2,4] [1,3]
         → merge → [1,2,3,4]
step=4:  整链 1 段，完成
```

代码骨架：
```python
n = 数长度()
dummy = ListNode(0, head)
step = 1
while step < n:                     # 段长 1,2,4,... 直到 >= n
    prev, cur = dummy, dummy.next
    while cur:
        left = cur                  # 第一段
        right = split(cur, step)    # 第二段（切出 step 个，断开）
        cur = split(right, step)    # 剩余链头
        prev.next = merge(left, right)
        while prev.next:            # prev 移到合并结果末尾
            prev = prev.next
    step *= 2
return dummy.next
```

两个灵魂细节：
1. **`split` 里 `head.next = None`（断开）**——每切一段必须物理断开，否则 `merge` 顺着 next 并到整条链尾，把后面没处理的段卷进来；
2. **`prev` 推进到合并结果末尾**——`prev` 是"已合并完部分"的尾巴，下一段结果要接到它后面，忽略就断链。

## 六、一刷 vs 二刷

- 一刷（9-14）：RE 一次 → 递归归并 AC → 协助写自底向上 O(1) 版（空间 O(logn) 不满足进阶的教训）；
- 二刷（10-20）：独立完成，组件复用到位（21 的 merge_node 直接搬）；空链表守卫小坑补上后 AC。

## 七、一句话记住

> **排序链表 = 链表归并排序：快慢指针切两半（prev.next=None 断开）→ 递归排两半 → 21 题哨兵归并合并；O(n log n)/O(log n) 递归栈，进阶 O(1) 用自底向上迭代归并。**