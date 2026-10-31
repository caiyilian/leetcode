"""295. 数据流的中位数（二刷·困难）——双堆 + inf 哨兵（addNum O(logn) / findMedian O(1) 标准解）

用户 AC 版（2026-10-31 21:43 提交 757955800，一次通过，153ms/41.5MB）
- small_heap = 最大堆（存负数实现），big_heap = 最小堆，各放一个 float('inf') 哨兵（长度上相互抵消，避免判空）
- 平衡规则：|len(small)-len(big)| <= 1，且 small 总数 >= big 总数（奇数时中位数在 small 堆顶）
- addNum：num <= big 堆顶 → 进 small，否则进 big；然后搬运保持平衡
- findMedian：总数为偶 → (big堆顶 + (-small堆顶))/2；为奇 → -small堆顶
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.small_heap = [float("inf")]   # 最大堆（存负数）——需要知道最大值
        self.big_heap = [float("inf")]     # 最小堆——需要知道最小值

    def addNum(self, num: int) -> None:
        big_min = self.big_heap[0]
        if num <= big_min:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.big_heap, num)

        if len(self.small_heap) - len(self.big_heap) > 1:
            # small 多了 → 移一个给 big
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        elif len(self.small_heap) - len(self.big_heap) < 0:
            # big 多了 → 移一个给 small
            heapq.heappush(self.small_heap, -heapq.heappop(self.big_heap))

    def findMedian(self) -> float:
        if (len(self.big_heap) + len(self.small_heap)) % 2 == 0:
            return (self.big_heap[0] - self.small_heap[0]) / 2   # 小堆顶最大 + 大堆顶最小 / 2
        return -self.small_heap[0]                               # 奇数 → 小堆顶（多一个）


# ===== 标准双堆参考（无哨兵，判空版） =====
class MedianFinderStd:
    def __init__(self):
        self.small = []   # 最大堆（负数）—— 较小一半
        self.big = []     # 最小堆 —— 较大一半

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)
        # 平衡：small 比 big 最多多 1 个
        if len(self.small) > len(self.big) + 1:
            heapq.heappush(self.big, -heapq.heappop(self.small))
        elif len(self.big) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        return (-self.small[0] + self.big[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()