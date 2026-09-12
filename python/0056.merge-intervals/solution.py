# Created by Chono-Hina at 2026/09/12 20:12
# leetgo: 1.4.18
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(length-1):
            if intervals[i+1][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i+1][1], result[-1][1])
            else:
                result.append(intervals[i+1])
        return result
        

# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))
