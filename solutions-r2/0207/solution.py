"""207. 课程表（二刷）——拓扑排序 Kahn（队列）+ 环检测（O(n+e)/O(n+e) 标准解）

用户 AC 版（2026-10-28 19:39 提交 757471092，255ms/20.1MB）——多轮扫描版（正确，非最优写法）
判断依据：numCourses 门课能否学完 = 图有无环（有环则无法完成所有先修）
- 入度 0 = 无先修 = 可以学；学完后继入度 -1；学不完（有环）= False
- ⚡ 用户版"每轮全量扫 range(numCourses)" O(n²)；标准 Kahn 用队列收集零入度节点 → O(n+e)

标准 Kahn 写法（推荐，O(n+e)/O(n+e)）：
"""

from collections import defaultdict, deque
from typing import List


# ========== 标准 Kahn（队列版，推荐） ==========
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses                # 入度数组
        out = defaultdict(list)                  # 邻接表：先修课 → 后续课
        for ai, bi in prerequisites:
            indeg[ai] += 1
            out[bi].append(ai)

        q = deque([i for i in range(numCourses) if indeg[i] == 0])  # 初始零入度课程
        cnt = 0                                  # 已学课程数
        while q:
            u = q.popleft()
            cnt += 1
            for v in out[u]:
                indeg[v] -= 1
                if indeg[v] == 0:                # 减到 0 立即入队（不用全量扫描）
                    q.append(v)
        return cnt == numCourses                 # 全部学完 = 无环


# ========== 用户多轮扫描版（正确，但 O(n²)） ==========
class SolutionUser:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        每一门课都有入度和出度
        0 --> 1
        入度为0的，可以学
        """
        input_deg = defaultdict(int)
        hash_map = defaultdict(list)
        for ai, bi in prerequisites:
            input_deg[ai] += 1            # ai的入度加1
            hash_map[bi].append(ai)
        learned = set()
        while len(learned) < numCourses:
            learn_each = 0
            for i in range(numCourses):   # ★ 每轮全量扫描（O(n²) 的来源）
                if i in learned:
                    continue
                if input_deg[i] == 0:
                    learned.add(i)
                    learn_each += 1
                    for ai in hash_map[i]:
                        input_deg[ai] -= 1
            if learn_each == 0:           # 一轮什么都没学到 = 有环
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))                    # True
    print(s.canFinish(2, [[1, 0], [0, 1]]))            # False
    print(s.canFinish(5, [[1, 0], [2, 0], [3, 1], [4, 2]]))  # True
    print(s.canFinish(3, [[1, 0], [2, 1], [0, 2]]))    # False（环）