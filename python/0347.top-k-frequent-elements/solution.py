# Created by Chono-Hina at 2026/09/18 12:52
# leetgo: 1.4.18
# https://leetcode.cn/problems/top-k-frequent-elements/

from typing import *
from leetgo_py import *
from collections import defaultdict
import heapq

# @lc code=begin

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict = {}
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1

        freq2num = []                                  # (频次, 数字)
        for key, value in count_dict.items():
            freq2num.append((value, key))

        heap = freq2num[:k]
        heapq.heapify(heap)
        for i in range(k, len(freq2num)):
            if freq2num[i][0] > heap[0][0]:            # 频次比堆顶高 → 替换
                heapq.heappushpop(heap, freq2num[i])
        return [n[1] for n in heap]                    # 答案顺序任意
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
