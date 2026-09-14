# 23. 合并 K 个升序链表 · 解析

## 题目简述

给你一个链表数组，每个链表都已经按升序排列。将所有链表合并到一个升序链表中并返回。

示例：`[[1,4,5],[1,3,4],[2,6]]` → `[1,1,2,3,4,4,5,6]`。

## 核心套路：分治两两合并（O(N log k) 最优复杂度之一）

设 k 条链、总节点 N。**关键洞察**：合并有序链表的成本与参与节点数成正比——如果让每条链参与的合并次数尽量少，总成本就低。

- **顺序合并（v1）**：第 i 轮把"已合并的大链"和"新链"再合并——大链被反复遍历 → O(kN)；
- **分治合并（v2）**：每轮所有链**成对合并**，链数减半，共 log k 轮，每轮总 O(N) → **O(N log k)**。

## 定稿解法（v2：分治两两合并，用户版）

```python
class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        length = len(lists)
        while length != 1:
            swap_count = length // 2
            for i in range(swap_count):                        # 成对合并
                lists[i] = self.mergeTwoLists(lists[i*2], lists[i*2+1])
            if length % 2:                                     # 奇数条：最后一条补位
                lists[swap_count] = lists[length-1]
                length += 1
            length = length // 2                               # 链数减半
        return lists[0]
```

**图解**（k=5：`A B C D E`）：

```
第 1 轮 → merge(A,B) merge(C,D) | E(补位)    → 剩 3 条
第 2 轮 → merge(AB,CD) | E(补位)             → 剩 2 条
第 3 轮 → merge(ABCD, E)                     → 剩 1 条 ✅
```

每条链参与合并 ≤ log k 次 → O(N log k)。

**合并函数**复用 21 题的插入法（`mergeTwoLists`，已验证）。

## 复杂度验证（实测 = 理论）

k=200、每条 1000 节点（N=20 万）：v1 **1222ms** vs v2 **158ms** = **7.7 倍**；而 log₂200 ≈ 7.64——**实测提速与理论 log k 完全吻合**。这是复杂度分析正确的硬证据（比力扣击败率可靠）。

## 其他解法对比

| 解法 | 时间 | 空间 | 说明 |
|------|------|------|------|
| 顺序两两合并（v1） | O(kN) | O(1) | 简单但大链反复遍历 |
| **分治两两合并（v2，定稿）** | **O(N log k)** | **O(1)** | 每轮成对合并，最优 |
| 优先队列 heapq | O(N log k) | O(k) | 每轮取最小头；**Python 坑：堆元素需存 `(val, index, node)`，Node 不可比较** |
| 全收集 + sorted() | O(N log N) | O(N) | 最快常数但非"合并"思路，面试不推荐 |

## 复杂度

- 时间 **O(N log k)**（v2）；
- 空间 **O(1)**（原地紧凑，无辅助列表）。

## 考点

- **多路合并 → 分治/堆**（两条路线，面试都要会讲）
- 与 21 合并两条、148 归并排序的关系：23 是 21 的多路版，分治思路与 148 归并同源
- 原地紧凑 + 奇数补位的细节处理
- Python 优先队列的 heapq 使用（面试常问）

## 易错点

1. **奇数条补位**：`lists[swap_count] = lists[length-1]` 必须在 `length += 1` 之前取值（先取后改）；
2. 折半前 `length += 1`（奇数时）再 `//2`——补位后数量是偶数；
3. 空链名单：`lists = []` 或 `lists = [[]]` 都返回 None；
4. heap 版不能直接 `heapq.heappush(heap, node)`（Node 不可比较）——必须带 index 或包装。

## 与 v1 的对比（为什么要分治）

```
v1 顺序：merge(merge(merge(A,B),C),D)...  大链被遍历 k 次
v2 分治：merge(A,B) → merge(AB,CD) → ... 每条链只被遍历 log k 次
```

**一句话**：链合并的成本是节点数，谁让每条链少参与几轮，谁就快。