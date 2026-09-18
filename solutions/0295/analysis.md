# 295. 数据流的中位数 · 解析

## 题目简述

动态数据流，随时 addNum 加数、findMedian 查当前中位数。要求 addNum 和 findMedian 都高效。

## 核心套路：双堆（大顶堆 + 小顶堆对半劈开）

**把数据流分成两半**：左半（较小）放大顶堆、右半（较大）放小顶堆，中位数永远在**两个堆顶之间**：

```
small（大顶堆，负值模拟）：存较小的一半，堆顶 = 左半最大值
large（小顶堆）：          存较大的一半，堆顶 = 右半最小值

中位数 = 
  两堆等长（偶数个）→ (small顶 + large顶) / 2
  small 多一个（奇数个）→ small顶
```

```python
class MedianFinder:
    def __init__(self):
        self.big_heap = [float("inf")]      # 小顶堆：较大一半
        self.small_heap = [float("inf")]    # 大顶堆（负值）：较小一半

    def addNum(self, num):
        # ① 判断放哪边：比左半最大小 → 左半
        if num <= -self.small_heap[0]:      # ★ 负值堆：-堆顶 = 左半最大
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.big_heap, num)
        # ② 平衡：small 最多比 big 多 1；big 不许比 small 多
        if len(self.small_heap) - len(self.big_heap) > 1:
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        elif len(self.small_heap) < len(self.big_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))

    def findMedian(self):
        if len(self.small_heap) == len(self.big_heap):
            return (self.big_heap[0] - self.small_heap[0]) / 2
        return -self.small_heap[0]
```

**为什么双堆能 O(log n) 插入**：每次插入只需"放进一个堆 + 最多两次堆调整"（O(log n)），而不用像快选那样每次 findMedian 重算 O(n)。

## ⚠️ 易错点（用户 WA 实录）：负值堆比较忘取负

```python
if num <= self.small_heap[0]:     # ❌ small_heap[0] 是负数/哨兵，num 永远比它大
if num <= -self.small_heap[0]:    # ✅ 取负还原"左半最大值"
```

**根因**：`small_heap` 存 `-num`，堆顶是最小负数（左半最大的相反数）。比较时忘了"存进去取负、取出来也要取负"。

**记忆锚点**：负值最大堆两条纪律——
1. 入堆取负：`heappush(heap, -x)`；
2. 取值/比较取负：`-heap[0]` 才是真实最大值。

**两头都要记得**，漏一头就错（用户 push 记得、比较忘了 → WA）。

## 复杂度

- addNum **O(log n)**、findMedian **O(1)**、空间 **O(n)**。

## 考点

- 双堆维护中位数（数据流 Top-K 的变体）
- **负值模拟大顶堆**（Python 无内置大顶堆）
- 平衡维护（左半数量 ≥ 右半数量，差 ≤ 1）
- inf 哨兵省判空

## 易错点

1. **负值堆比较忘取负**（用户 WA 点）；
2. 平衡条件写反（small 和 big 的差 >1 的方向）；
3. 偶数时中位数忘记 `/2`，或忘加 `big_heap[0] - small_heap[0]` 里的负号；
4. 快选/排序偷懒 → findMedian O(n) 超时（TLE 点）。

## 关联题

- **215 第 K 大**（单堆 Top-K）/ **347 前 K 高频**（计数 + 堆）；
- **480 滑动窗口中位数**（双堆 + 延迟删除，进阶）；
- 双堆的"对半劈开"思想也用于：数据流 Top-K 之和、IPO 502 等。