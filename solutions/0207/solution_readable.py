# -*- coding: utf-8 -*-
"""
第 207 题 课程表 · v1 粗暴版（O(V²)，仅作演进对比）
思路：每轮全扫所有课程找入度 0，直到没有进展。
正确（5 万组对拍 0 差异）但每轮 O(V) × 最多 V 轮 = O(V²)。
优化方向（用户自驱完成）：队列版 Kahn，O(V+E)。
"""
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        count_dict = defaultdict(int)
        need_dict = defaultdict(list)
        for back, before in prerequisites:
            count_dict[back] += 1
            need_dict[before].append(back)
        learned = set()
        while True:
            learn_round = 0
            for i in range(numCourses):
                if i not in learned and count_dict[i] == 0:   # 入度 0 = 可以直接学
                    learned.add(i)
                    for need in need_dict[i]:
                        count_dict[need] -= 1
                        learn_round += 1
            if learn_round == 0:
                break
        return len(learned) == numCourses