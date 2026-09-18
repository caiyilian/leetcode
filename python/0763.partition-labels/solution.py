# Created by Chono-Hina at 2026/09/18 19:03
# leetgo: 1.4.18
# https://leetcode.cn/problems/partition-labels/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        hash_dict = {}
        result = []
        for i, c in enumerate(s):        # ① 记录每个字母最后出现位置
            hash_dict[c] = i
        start = 0
        end = 0
        for i, c in enumerate(s):        # ② 维护片段右边界，走到 end 就切段
            end = max(end, hash_dict[c])   # 片段右边界 = 字母最后位置的最大值
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partitionLabels(s)
    print("\noutput:", serialize(ans, "integer[]"))
