"""406. 根据身高重建队列（二刷）——排序 + 按 k 插入（O(n²)/O(n) 标准解）

用户 AC 版（2026-10-31 23:25 提交 757969074，一次通过，4ms/19.4MB）
- 核心：先"身高降序，k 升序"排序 → 再依次 insert(k, person)
- 为什么对：较高的先放，矮的插入时不影响已经存在的"更高的人"的 k 计数；
- 等身高的人 k 小的先插 → 保证同身高内相对顺序正确（k 升序是关键！）
"""

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))   # 身高降序，k 升序
        result = []
        for p in people:
            result.insert(p[1], p)                 # 插入到下标 k 的位置
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    print(s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
    # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]