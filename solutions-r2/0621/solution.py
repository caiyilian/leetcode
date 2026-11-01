"""621. 任务调度器（二刷）——贪心公式 + len(tasks) 兜底（O(n)/O(1) 标准解）

用户 AC 版（2026-11-01 15:17 提交 758030025，43ms/20.2MB）
- 核心公式：(max_count - 1) * (n + 1) + count_max
  - max_count       = 出现次数最多的任务的频次
  - count_max       = 有多少种任务达到这个频次
  - (max_count-1) 组完整轮（每组含 1 个最高频 + n 个冷却坑），最后剩 count_max 个最高频任务收尾
- ⚡⚡⚡ 必加兜底：max(公式结果, len(tasks)) —— 公式是"最高频任务为骨架"的下界建模，
  当其他任务种类够多把冷却坑填满时，实际排布可以紧凑到零空闲，时长不可能少于任务总数
- 反例：A,C,A,B,D,B n=1 → 公式 4，正确 6（C/D 恰好填满冷却，零 idle）
"""

from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        max_count = 0
        for c in tasks:
            count[c] = count.get(c, 0) + 1
            max_count = max(max_count, count[c])

        count_max = 0
        for value in count.values():
            if value == max_count:
                count_max += 1

        # ⚡ 兜底：公式结果不能少于任务总数（冷却是"至少 n"，不是"恰好 n"）
        return max(len(tasks), (max_count - 1) * (1 + n) + count_max)


if __name__ == "__main__":
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))   # 8
    print(s.leastInterval(["A", "C", "A", "B", "D", "B"], 1))   # 6
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 3))   # 10