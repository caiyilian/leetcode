"""239. 滑动窗口最大值（二刷）——单调队列（存下标）

用户 AC 版（2026-10-13 23:03 提交 754650321）
核心：deque 维护窗口内"可能成为最大值"的候选（单调递减），
      队首永远是窗口最大值；只碰两端（队尾 pop 挤掉小的 + 队首 popleft 过期）
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()
        # 初始窗口 [0, k-1]
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:   # 队尾比新数小的都挤掉
                q.pop()
            q.append(i)
        result.append(nums[q[0]])                 # 队首 = 窗口最大值
        # 滑动
        for i in range(k, len(nums)):
            if q[0] == i - k:                     # ★ 队首恰好滑出窗口才弹出（不无脑 popleft）
                q.popleft()
            while q and nums[q[-1]] < nums[i]:    # 新数进来，挤掉队尾更小的
                q.pop()
            q.append(i)
            result.append(nums[q[0]])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
    print(s.maxSlidingWindow([1], 1))                          # [1]
    print(s.maxSlidingWindow([1, -1], 1))                      # [1, -1]
    print(s.maxSlidingWindow([4, 3, 1, 0], 2))                 # [4, 3, 1]