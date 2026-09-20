# 239. 滑动窗口最大值 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 239. 滑动窗口最大值（Sliding Window Maximum）· **困难**（单调队列） |
| 链接 | https://leetcode.cn/problems/sliding-window-maximum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 53/53 用例通过**（leetgo 复提交） |
| 运行时间 | 177 ms（击败 78%） |
| 内存 | 34.3 MB |

## ⚠️ 演进记录（4 次提交，用户主动总结）

| 提交 | 结果 | 问题 |
|------|------|------|
| 750426236 | **WA** | 初始化循环用 `if arr`（只 pop 一次），应 `while arr`（循环弹掉所有小的） |
| 750426589 | **OLE** | 改成 while 了，但 `print` 调试残留导致输出超限 |
| 750426830 | AC | list + `pop(0)`（O(n)，慢） |
| 750427941 | AC | **deque + `popleft()`（O(1)，快）** |

**关键优化（用户自悟）**：`list.pop(0)` 是 O(n)（要移动整个列表），换成 `deque.popleft()` 是 O(1)——速度大幅提升。

## 解法（用户单调队列 deque 版）

```python
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        length = len(nums)
        arr = deque()               # 存索引，维护递减（队头最大）
        result = []
        for i in range(k):
            while arr and nums[i] > nums[arr[-1]]:   # 队尾比 nums[i] 小的都弹掉
                arr.pop()
            arr.append(i)
        result.append(nums[arr[0]])
        for i in range(1, length - k + 1):
            new = i - 1 + k
            while arr and nums[new] > nums[arr[-1]]:
                arr.pop()
            arr.append(new)
            if arr[0] < i:           # 队头超出窗口 → 弹出
                arr.popleft()
            result.append(nums[arr[0]])
        return result
```

## 核心：单调队列（递减）

- deque 存**索引**，维护"递减"（队头最大，队尾最小）；
- 加入新元素：从队尾弹出所有比它小的（保证递减，且这些不可能再成为最大）；
- 队头超出窗口范围时 `popleft`；
- 队头恒为当前窗口最大值。

## 验证

- 对拍 **3 万组随机数组 vs 暴力 max 0 不一致**；
- 样例：`[1,3,-1,-3,5,3,6,7] k=3 → [3,3,5,5,6,7]`、`[1] k=1 → [1]`。

## 复杂度

- 时间 **O(n)**（每个元素入队出队各一次）；空间 O(k)。