# Created by Chono-Hina at 2026/09/25 14:39
# leetgo: 1.4.18
# https://leetcode.cn/problems/queue-reconstruction-by-height/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 贪心 + 插入：先按身高降序（同高 k 升序），再逐个按 k 插入
        # 高个子先入队定位置，矮个子插入不影响已入队的人（他们不比自己高）
        people.sort(key=lambda x: (-x[0], x[1]))
        result = []
        for h, k in people:
            result.insert(k, [h, k])   # 插到第 k 位，前面恰好 k 个 ≥ 自己身高
        return result
        

# @lc code=end

if __name__ == "__main__":
    people: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().reconstructQueue(people)
    print("\noutput:", serialize(ans, "integer[][]"))
