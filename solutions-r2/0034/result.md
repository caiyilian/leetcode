# 34. 在排序数组中查找元素的第一个和最后一个位置 · 二刷结果

## 提交记录（力扣账号 tomoya-w9）

| 日期 | 结果 | 提交 ID | 说明 |
|------|------|---------|------|
| 2026-09-17 | AC ×2 | 749723573 / 749725349 | 一刷（二分边界） |
| **2026-10-30 14:40** | **AC** | **757761608** | 二刷：三个二分 + ±0.5 假想值，**一次通过**（0ms / 20.2MB） |

## 是否最优解？✅ 是（O(logn) + O(1)）

| 考察点 | 结论 |
|--------|------|
| 时间复杂度 | ✅ O(logn)——3 次二分（合并写法可 2 次） |
| 空间复杂度 | ✅ O(1) |
| 正确性 | ✅ 官方示例 + 空数组 + **3 万组随机对拍**（vs bisect 参照，含重复/全同/首尾/边界外）0 不一致 |
| 思路 | ✅ 二分左右边界 = 官方标准解 |

## 解法核心：±0.5 假想值把"边界"化为"插入位置"

**三连二分**：
```python
# ① 确认 target 存在（for-else，不存在返回 [-1,-1]）
while left <= right:
    mid = (left+right)//2
    if nums[mid] == target: break
    elif nums[mid] < target: left = mid+1
    else: right = mid-1
else:
    return [-1, -1]

# ② 左边界：把 target-0.5 当"插入点"二分 → start = 第一个 >= target 的下标
target1 = target - 0.5
... return left → start

# ③ 右边界：把 target+0.5 当"插入点" → end = 第一个 > target 的下标
target2 = target + 0.5
... return left → end

return [start, end - 1]
```

**为什么用 ±0.5**：
- 整数数组里没有 `target±0.5` 这个数 → `bisect_left(nums, target-0.5)` 恰好 = 第一个 ≥ target 的位置；
- `bisect_left(nums, target+0.5)` = 第一个 > target 的位置 → **-1 就是最后一个 target**；
- 把"找边界"化简成 35 已掌握的"找插入位置 + return left"——**35 的模板直接复用**。

## 更标准的写法（二合一，面试推荐）

```python
def lower(nums, target):            # 第一个 >= target
    l, r = 0, len(nums)
    while l < r:
        m = (l+r)//2
        if nums[m] < target: l = m+1
        else: r = m
    return l

def searchRange(self, nums, target):
    l = lower(nums, target)
    if l == len(nums) or nums[l] != target:
        return [-1, -1]
    r = lower(nums, target+1) - 1   # 复用同一函数，target+1 找下界再 -1
    return [l, r]
```
用左边界函数 `lower(target)` 和 `lower(target+1)-1`，**只需写一个二分函数 ×2 调用**；±0.5 与 `target+1` 等价（整数域），但 `target+1` 不怕浮点——二选一，面试写 `target+1` 更通用。

## 过程回顾

一刷（9-17）：二分边界 AC ×2。
二刷（10-30）：**一次 AC，±0.5 技巧直接写对**——35 的"return left"模板在"找边界"场景的变体，二分三连主法已掌握。