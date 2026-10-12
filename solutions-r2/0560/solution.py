"""560. 和为 K 的子数组（二刷）——前缀和 + 哈希计数一遍遍历

用户 AC 版（2026-10-12 21:05 提交 754367559）
"""

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 -> 该前缀和出现过的次数
        hash_dict = defaultdict(int)
        hash_dict[0] = 1        # 虚拟前缀和 0：覆盖"从头开始"的子数组
        pre = 0                 # 当前前缀和
        result = 0
        for i in range(len(nums)):
            pre += nums[i]                              # 更新前缀和
            result += hash_dict[pre - k]                # ★ 查差值：之前出现过多少个 pre-k
            hash_dict[pre] += 1                         # ★ 后记账：把自己记进去（先查后记，防 k=0 自算）
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))          # 2
    print(s.subarraySum([1, 2, 3], 3))          # 2
    print(s.subarraySum([1, -1, 0], 0))         # 3
    print(s.subarraySum([1, -1, 1, -1], 0))     # 4