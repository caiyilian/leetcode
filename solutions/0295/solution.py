# Created by Chono-Hina at 2026/09/18 15:48
# leetgo: 1.4.18
# https://leetcode.cn/problems/find-median-from-data-stream/

from typing import *
from leetgo_py import *
import heapq

# @lc code=begin

class MedianFinder:

    def __init__(self):
        self.big_heap = [float("inf")]      # 大堆（小顶堆，存较大一半）；inf 哨兵免判空
        self.small_heap = [float("inf")]    # 小堆（大顶堆，用负值）；堆顶 = 左半最大取负

    def addNum(self, num: int) -> None:
        small_heap = self.small_heap
        big_heap = self.big_heap
        # 比左半最大值还小 → 放左半（small，负值）；否则放右半（big）
        if num <= -self.small_heap[0]:      # ★ 负号！small_heap 存负值，-堆顶才是真实左半最大
            heapq.heappush(small_heap, -num)
        else:
            heapq.heappush(big_heap, num)
        # 平衡：small 比 big 多不超过 1；big 不许比 small 多
        if len(small_heap) - len(big_heap) > 1:
            heapq.heappush(big_heap, -heapq.heappop(small_heap))
        elif len(small_heap) < len(big_heap):
            heapq.heappush(small_heap, -heapq.heappop(big_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.big_heap):   # 偶数
            return (self.big_heap[0] - self.small_heap[0]) / 2
        else:                                            # 奇数（small 多一个）
            return -self.small_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MedianFinder()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addNum(num)
                output.append("null")
            case "findMedian":
                ans = serialize(obj.findMedian())
                output.append(ans)

    print("\noutput:", join_array(output))
