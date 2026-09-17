# 34. 在排序数组中查找元素的第一个和最后一个位置 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 34. 在排序数组中查找元素的第一个和最后一个位置（Find First and Last Position）· 中等（二分查找分类第 3 题） |
| 链接 | https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 88/88 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 20.3 MB |

## 解法（用户补丁版：两次 lower_bound + 边界补丁）

```python
class Solution:
    def searchRange(self, nums, target):
        left, right = 0, length - 1
        while left < right:                    # ① 第一次二分：第一个 >= target
            ...
        if nums[left] != target: return [-1, -1]
        min_val = left
        while left < right:                    # ② 第二次二分：第一个 >= target+1
            ...
        return [min_val, left if nums[-1] == target else (left - 1)]  # ★ 补丁
```

**用户的补丁疑问（本次精华）**："target 是最大值时右边界直接用 left，否则 left-1"——**逻辑正确**（5 万组对拍 0 差异），根因是第二次二分用了**闭区间**（right=length-1），找不到"≥ target+1"时 left 卡在 length-1 而非哨兵 length。

**标准哨兵版**（solution_readable.py，无补丁）：lower_bound 用**开区间**（right=len(nums)），找不到时返回哨兵 length → 右边界 `lower_bound(target+1) - 1` 统一成立。

## 验证

- 对拍 **5 万组（含重复元素！）vs bisect_left/right 参照 0 不一致**；
- 官方样例：`[5,7,7,8,8,10]`+8→[3,4]、+6→[-1,-1]、`[]`→[-1,-1]；
- 边界：`[1,1,1]`→[0,2]、`[10,10]`→[0,1]、`[1]`→[0,0]。

## 复杂度

- 时间 **O(log n)**（两次二分）；空间 **O(1)**——满足题目要求 ✅。

## ⚡ 连续第三次应验"骨架对了就不需要补丁"

35 补丁版 → 74 映射版 → 34 边界补丁——每次补丁都源于模板骨架的某个偏差（`mid+1` 缺失 / 除数 m-n 混用 / 闭区间丢失哨兵）。**开区间 + mid+1 是二分模板的最稳骨架。**