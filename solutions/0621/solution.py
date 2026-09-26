# Created by Chono-Hina at 2026/09/26 15:19
# leetgo: 1.4.18
# https://leetcode.cn/problems/task-scheduler/

from typing import *
from leetgo_py import *
from collections import defaultdict

# @lc code=begin

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 贪心 + 桶：最高频任务排 max 次，中间必须隔 n 个其它任务
        # 桶 = 任务 + n 个冷却位（n+1 格），排 (max-1) 个完整桶 + 最后一批
        count_dict = defaultdict(int)
        max_len = 0
        for t in tasks:
            count_dict[t] += 1
            max_len = max(max_len, count_dict[t])     # 最高频次数
        cnt_max = 0
        for value in count_dict.values():
            if value == max_len:
                cnt_max += 1                          # 有几个同频最高
        return max((max_len - 1) * (n + 1) + cnt_max, len(tasks))
        

# @lc code=end

if __name__ == "__main__":
    tasks: List[str] = deserialize("List[str]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().leastInterval(tasks, n)
    print("\noutput:", serialize(ans, "integer"))
