"""56. 合并区间（二刷）——排序 + 遍历合并

用户 AC 版（2026-10-15 16:53 提交 755012719，一次通过）
思路：按起点排序 → 相邻比较，不相交收走 / 相交则合并到下一个位置继续看
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        if length == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])        # 按起点排序
        result = []
        for i in range(length - 1):
            if intervals[i][1] < intervals[i + 1][0]:
                # 不相交 → 当前区间没有后续可合并，收进结果
                result.append(intervals[i])
            else:
                # 相交/包含 → 合并到下一个位置（先不急着进 result，可能还能继续并）
                intervals[i + 1] = [intervals[i][0], max(intervals[i][1], intervals[i + 1][1])]
        result.append(intervals[-1])              # 最后一个（可能已被合并过）
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 4], [4, 5]]))                     # [[1,5]]
    print(s.merge([[1, 4], [0, 4]]))                     # [[0,4]]
    print(s.merge([[1, 4], [2, 3]]))                     # [[1,4]]