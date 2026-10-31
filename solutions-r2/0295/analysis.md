# 295. 数据流的中位数 · 解析（二刷·困难）

## 一、核心思路：双堆对半分

**问题**：数据不断流入，随时要查中位数。O(n) 排序查询太慢。

**双堆模型**（中位数题的"标准答案"）：
- **small**：最大堆，装**较小的一半**（Python 用 `-x` 存负数模拟最大堆）；
- **big**：最小堆，装**较大的一半**。

两个堆顶夹着"中间"——**中位数只取决于两个堆顶**：

```
数据流: 5, 3, 8, 1, 9, 6
small(最大): [-5,-3,-1] → 堆顶 5 (最大)
big(最小):   [6,8,9]   → 堆顶 6 (最小)
6 个数是偶数 → 中位数 = (5 + 6) / 2 = 5.5
```

**平衡不变量**：`len(small) >= len(big)` 且差 ≤ 1（small 恰好多 1 个或相等）。

## 二、代码（用户 AC 版：双堆 + inf 哨兵）

```python
def __init__(self):
    self.small_heap = [float("inf")]    # 最大堆（存负数）
    self.big_heap = [float("inf")]      # 最小堆

def addNum(self, num):
    if num <= self.big_heap[0]:         # 比"较大一半的最小值"小 → 进较小一半
        heapq.heappush(self.small_heap, -num)
    else:
        heapq.heappush(self.big_heap, num)
    # 平衡搬运
    if len(self.small_heap) - len(self.big_heap) > 1:
        heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
    elif len(self.small_heap) - len(self.big_heap) < 0:
        heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))

def findMedian(self):
    if (len(self.big_heap) + len(self.small_heap)) % 2 == 0:   # 偶数
        return (self.big_heap[0] - self.small_heap[0]) / 2     # 两堆顶平均
    return -self.small_heap[0]                                 # 奇数：多一个在 small
```

## 三、⚡ inf 哨兵技巧（用户独创，值得记）

**问题**：空堆时 `heap[0]` 越界，标准写法要 `if not heap` 判空。
**解法**：两个堆初始化都放一个 `float('inf')`：
- 永远不空 → `big_heap[0]`、弹堆都安全，省掉所有判空；
- 哨兵在**长度上互相抵消**（各 1 个），不影响平衡判断；
- 唯一注意：`findMedian` 长度计算里哨兵各算 1，正好抵消，奇偶判断不受影响。

## 四、复杂度

- addNum：O(logn)（push + 偶尔一次 pop/push 搬运）
- findMedian：O(1)
- 空间：O(n)

## 五、一刷 vs 二刷

- 一刷（9-18）：TLE→WA→AC ×2（边界：空堆、等长时取哪个顶）；
- 二刷（10-31）：双堆 + inf 哨兵一次 AC——模型与边界都掌握了。

## 六、关联题目（⚡ 双堆/Top-K 家族）

| 套路 | 相关题 |
|------|--------|
| 双堆对半分 | **295 本体**、**480 滑动窗口中位数**（双堆+延迟删除，hard） |
| 动态 Top-K | **215 数组第 K 大**（⚡ 已做）、**703 数据流第 K 大**（单堆） |
| 中位数变体 | 4 寻找两个正序数组的中位数（⚡ 已做，二分切分） |

**295 → 480 是升级**：滑动窗口内的中位数，双堆框架照搬，难点在"窗口移出元素时堆的延迟删除"（lazy deletion）——先吃透 295 的平衡逻辑再来。

## 七、一句话记住

> **数据流中位数 = 双堆对半分：small 最大堆存小半、big 最小堆存大半，平衡差 ≤1；奇数取 small 顶、偶数取两顶平均；⚡ inf 哨兵免判空（长度抵消）。**