# 295. 数据流的中位数 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 295. 数据流的中位数（Find Median from Data Stream）· **困难**（堆分类收官题） |
| 链接 | https://leetcode.cn/problems/find-median-from-data-stream/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 22/22 用例通过**（leetgo 复提交） |
| 运行时间 | 204 ms（leetgo 噪声，击败 38%） |
| 内存 | 40.9 MB（击败 90%） |

## ⚠️ 三次提交演进 + 易错点（用户要求记录）

| 提交 | 结果 | 问题 |
|------|------|------|
| 749980384 | **TLE** | 快速选择版：addNum O(1) 偷懒、findMedian O(n) 每次重算 |
| 749997101 | **WA** | 双堆版：**比较时漏负号**（见下） |
| 750001380 | **AC** | 双堆版（修复负号） |

### 用户易错点：负值堆比较时忘取负

```python
if num <= self.small_heap[0]:     # ❌ WA：少了负号
if num <= -self.small_heap[0]:    # ✅ AC：取负还原真实值
```

small_heap 存**负值**（`-num`），堆顶是"左半最大值的相反数"，比较"num ≤ 左半最大"必须 `-small_heap[0]` 还原。WA 后果：`num <= 负数` 几乎恒 False → 所有元素进 big → small 空 → 中位数错。

**记忆锚点：负值最大堆的完整纪律——入堆取负（-x），比较/取值也要取负（-heap[0]），两头都要记得。**

## 解法（用户双堆 + inf 哨兵）

```python
class MedianFinder:
    def __init__(self):
        self.big_heap = [float("inf")]      # 大堆（小顶堆，较大一半）
        self.small_heap = [float("inf")]    # 小堆（大顶堆负值，较小一半）

    def addNum(self, num):
        if num <= -self.small_heap[0]:      # 比左半最大小 → 放左半
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.big_heap, num)
        if len(self.small_heap) - len(self.big_heap) > 1:
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        elif len(self.small_heap) < len(self.big_heap):
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))

    def findMedian(self):
        if len(self.small_heap) == len(self.big_heap):
            return (self.big_heap[0] - self.small_heap[0]) / 2
        return -self.small_heap[0]
```

**inf 哨兵**：两个堆初始各一个 `inf`，len 差值/相等判断中哨兵相互抵消，省去空堆判空（与 155/4 的哨兵一脉相承）。

## 验证

- 对拍 **5 万次随机操作（addNum/findMedian 交错）vs 排序参照 0 不一致**；
- 官方样例：`[1,2]→1.5`、`[1,2,3]→2.0`。

## 复杂度

- addNum **O(log n)**、findMedian **O(1)**、空间 O(n)——满足题目要求。

## 🏆 堆分类 3/3 全通关（215 → 347 → 295）