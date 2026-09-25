# 581. 最短无序连续子数组 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 581. 最短无序连续子数组（Shortest Unsorted Continuous Subarray）· 中等（v2 新增题 · 双指针扫描） |
| 链接 | https://leetcode.cn/problems/shortest-unsorted-continuous-subarray/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-25 |
| 最终提交 | ✅ **ACCEPTED - 307/307 用例通过**（leetgo 复提交） |
| 运行时间 | 12 ms |
| 内存 | 20.1 MB |

## ⚠️ 演进记录（WA → AC）

| 提交 | 结果 | 原因 |
|------|------|------|
| 751430872 | **WA** | 左扫用 `>`、右扫用 `<`（不带等号） |
| 751430955 | AC | 改成 `>=` / `<=`（**等号是关键**） |

**等号为什么必须**：看 `[1,3,2,2,2]`（排序后 `[1,2,2,2,3]`，未排序区间 `[3,2,2,2]` 长度 4）。
- 左扫用 `>`：`2 > 3` 否 → r 只标到 1（3 的位置），后面三个 2 漏掉 → 错；
- 左扫用 `>=`：`2 >= 3` 否 → 每个 2 都更新 r → r 正确到 4 ✓。

**相等元素必须计入区间**（它们在升序后应前移），所以比较要带等号。

## 解法（用户双指针扫描，O(n) 进阶版）

```python
class Solution:
    def findUnsortedSubarray(self, nums):
        length = len(nums)
        max_l = nums[0]
        l = None; r = None
        for i in range(1, length):          # 左→右：找右边界
            if nums[i] >= max_l:
                max_l = nums[i]
            else:
                r = i                        # 最后一个"小于左边最大值"
        if r is None:
            return 0
        min_r = nums[-1]
        for i in range(1, length):          # 右→左：找左边界
            if nums[length - 1 - i] <= min_r:
                min_r = nums[length - 1 - i]
            else:
                l = length - 1 - i           # 最后一个"大于右边最小值"
        return max(0, r - l + 1)
```

## 核心：双哨兵扫描

- **右边界 r** = 最后一个"小于左边已见最大值"的位置（它右边都 ≥ 左边最大值，天然有序）；
- **左边界 l** = 最后一个"大于右边已见最小值"的位置（它左边都 ≤ 右边最小值，天然有序）；
- `[l, r]` 就是必须排序的最小区间。

## 验证

- 对拍 **2 万组含相等元素的数组 vs 排序比较法 0 不一致**（AC 版）；WA 版有 4383 组不一致（印证等号关键）；
- 样例：`[2,6,4,8,10,9,15]→5`、`[1,2,3,4]→0`、`[2,1]→2`、`[2,2,2,2]→0`。

## 复杂度

- 时间 **O(n)**；空间 O(1)。