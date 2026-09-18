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
        hash_dict = {}
        count_list = []
        for n in nums:
            if n not in hash_dict:
                hash_dict[n] = len(count_list)   # 数字 → count_list 下标
                count_list.append(1)
            else:
                count_list[hash_dict[n]] += 1
        count2num = defaultdict(list)             # 频次 → 数字列表（桶思想）
        for key, value in hash_dict.items():
            count2num[count_list[value]].append(key)
        heap = count_list[:k]                     # 先存变量（heapify 原地，不能直接传切片）
        heapq.heapify(heap)
        for num in count_list[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        result = []
        for count in heap:
            result.append(count2num[count].pop())  # 反查数字（堆里 count 出现几次就 pop 几个）
        return result
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
