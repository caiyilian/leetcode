# 35. 搜索插入位置 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 35. 搜索插入位置（Search Insert Position）· 简单（二分查找分类第 1 题） |
| 链接 | https://leetcode.cn/problems/search-insert-position/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 66/66 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.7 MB |

## ⚡⚡ 机考之前必看：标准二分模板（solution_readable.py）

```python
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)          # ① 左闭右开 [left, right)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:         # 找"第一个 >= target"的位置
                right = mid
            else:
                left = mid + 1              # ② 关键：mid+1 保证收敛
        return left                          # ③ 结束时 left == right == 插入位置
```

**模板三件套**：`right = len(nums)`（开区间）/ `left = mid+1`（防死循环）/ 返回 `left`。

## 两版对照（用户补丁版 vs 标准模板）

| | 用户版（solution.py） | 标准模板（readable） |
|--|---------------------|---------------------|
| 结构 | `left = middle`（不+1）→ 被迫加 3 个提前 return + 兜底 return 0 | `left = mid+1` → 无任何补丁 |
| 正确性 | 5 万组对拍 0 差异（碰巧完备） | 教科书正确 |
| 可读性 | 低（"return 0"之谜） | 高（答案即 left） |

**核心教训（用户提问触发）**：while 退出后 `return 0` 并不是"插入位置总是 0"——用户版靠"所有非 0 答案在 while 内提前 return"+ 兜底 0（仅 target 最小才走到）碰巧正确；标准版中 left 可以是任意值（0/中间/length）。

## 验证

- 对拍 **5 万组随机数组 vs 标准版 vs bisect_left 三方一致 0 差异**；
- 官方样例：`[1,3,5,6]` + 5→2、2→1、7→4；边界 `[2]+1→0`、`[1]+2→1`。

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**。