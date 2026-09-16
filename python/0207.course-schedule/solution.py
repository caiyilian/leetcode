# Created by Chono-Hina at 2026/09/16 10:37
# leetgo: 1.4.18
# https://leetcode.cn/problems/course-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        count_dict = defaultdict(int)        # 入度表：课程 → 前置未学数量
        need_dict = defaultdict(list)        # 出边表：课程 → 依赖它的课程列表
        for back, before in prerequisites:
            # 先学 before 才能学 back，所以是 before->back，back 的入度 +1
            count_dict[back] += 1
            need_dict[before].append(back)
        # 初始把所有入度为 0（可以直接学）的课程入队
        q = deque([i for i in range(numCourses) if count_dict[i] == 0])
        learned = 0
        while q:
            for _ in range(len(q)):          # 快照分层：同一轮可学的（102 技巧迁移）
                num = q.popleft()
                learned += 1
                for need in need_dict[num]:
                    count_dict[need] -= 1
                    if count_dict[need] == 0:
                        q.append(need)       # 入度变 0 → 下一轮可学
        return learned == numCourses
        

# @lc code=end

if __name__ == "__main__":
    numCourses: int = deserialize("int", read_line())
    prerequisites: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().canFinish(numCourses, prerequisites)
    print("\noutput:", serialize(ans, "boolean"))
