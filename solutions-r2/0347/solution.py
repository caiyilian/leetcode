"""347. 前 K 个高频元素（二刷）——频次统计 + 最小堆维护前 K 高（O(n log k)/O(n) 标准解）

用户 AC 版（2026-10-31 21:44 提交 757955930，一次通过，7ms/22.7MB）
- ① Counter 统计每个数字出现频次
- ② 把 (频次, 数字) 建成大小为 k 的最小堆（按频次排序）：堆顶 = 前 K 高里频次最低的
- ③ 遍历其余：频次比堆顶高 → heappushpop 替换
- ⚡ 答案顺序任意（并列频次任选合法）；返回堆里的数字即可
"""

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1

        freq2num = []
        for key, value in count_dict.items():
            freq2num.append((value, key))          # (频次, 数字)

        heap = freq2num[:k]
        heapq.heapify(heap)
        for i in range(k, len(freq2num)):
            if freq2num[i][0] > heap[0][0]:        # 频次比堆顶高 → 替换
                heapq.heappushpop(heap, freq2num[i])
        return [n[1] for n in heap]                # 答案顺序任意


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [2, 1]（顺序任意）
    print(s.topKFrequent([1], 1))                  # [1]