# 347. 前 K 个高频元素 · 解析

## 题目简述

数组里找出现频率最高的 k 个元素，返回任意顺序。

## 核心套路：计数 + 大小为 k 的最小堆（215 的直接应用）

**两步**：
1. **计数**：`Counter(nums)` 统计每个数字的频次；
2. **Top-K**：用大小为 k 的最小堆维护"频次最高的 k 个"——**正是 215 的套路，只是堆里比的是"频次"而非元素值**。

## 标准版（堆存 (频次, 数字) 元组）

```python
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        heap = []                               # 存 (频次, 数字)
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)             # 弹掉频次最小的
        return [num for _, num in heap]
```

**关键技巧：堆存 `(freq, num)` 元组**——元组按第一元素（频次）比较，数字自动跟着频次走。省掉"反查数字"的步骤。

## 用户版（堆存频次 + count2num 反查，桶思想）

用户堆里只存**频次**，数字另存一张 `count2num`（频次 → 数字列表）反查：

```python
count2num[count].pop()   # 堆里 count 出现几次，count2num[count] 里就有几个数字
```

**这个"频次 → 数字"的分桶结构本质是桶排序思想**（347 的 O(n) 桶解基于它）。功能正确，但比"堆存元组"多绕一个反查表。

## ⚡ 技术点：heapify 不能直接传切片

```python
heapq.heapify(count[:k])   # ❌ 原地改切片副本，返回 None，结果丢弃
heap = count[:k]; heapq.heapify(heap)   # ✅ 先落变量再原地建堆
```

`heapify` 是**原地函数**（返回 None），不能对临时对象操作后指望拿到结果。同理 `x.sort()`。**记忆锚点：Python 原地函数的通病——先有变量引用，再原地操作。**

## 复杂度

- 时间 **O(n log k)**（n = 不同数字数；每次堆操作 O(log k)）；空间 O(n)（Counter + 堆）。

## 考点

- **计数 + 堆**组合（Top-K 标准二连）
- 堆存"元组"（(排序键, 负载)）的技巧
- 原地函数（heapify）的正确用法

## 易错点

1. 堆存频次忘了数字跟着走 → 需要反查表绕圈（用户版）；
2. `heapify(count[:k])` 直接传切片（本次提问点）——原地函数不返回结果；
3. 用 `most_common(k)` 一行解决（正确但面试最好讲堆的原理）；
4. 频次相同的多个数字要都返回（count2num 列表 / 元组堆都能处理）。

## 关联题

- **215 第 K 大元素**（Top-K 模板母题，堆/快速选择）；
- **295 数据流中位数**（双堆进阶）；
- **692 前 K 个高频单词**（同题 + 字典序 tie-break）；
- 桶排序变体：347 也可 O(n)（按频次分桶，从高到低取）。