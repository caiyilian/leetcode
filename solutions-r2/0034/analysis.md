# 34. 在排序数组中查找元素的第一个和最后一个位置 · 解析（二刷）

## 一、核心思路：用"左边界函数"分别找首/尾

**问题**：排序数组（含重复），找 target 第一次和最后一次出现的下标。

**本质**：
- **第一个位置** = `bisect_left(target)`（第一个 ≥ target）
- **最后一个位置** = `bisect_left(target+1) - 1`（第一个 > target 的前一个）

**关键洞察**：只要会"找第一个 ≥ x 的位置"（35 的 `return left`），首尾两个位置都能用**同一个函数**算出来。

## 二、用户 AC 版：±0.5 假想值

```python
# ① 确认存在（for-else）
while left <= right:
    mid = (left+right)//2
    if nums[mid] == target: break
    elif nums[mid] < target: left = mid+1
    else: right = mid-1
else:
    return [-1, -1]

# ② 左界：二分找 target-0.5 的插入位置（= 第一个 >= target）
target1 = target - 0.5
...start = left

# ③ 右界：二分找 target+0.5 的插入位置（= 第一个 > target）
target2 = target + 0.5
...end = left

return [start, end - 1]
```

**±0.5 为什么成立**：整数数组里没有 target±0.5，所以"插入位置"恰好切在 target 段的左/右边——左界 = 首，`右界-1` = 尾。干净直观，但注意**浮点**（大数可能精度问题）。

## 三、⚡ 标准写法（更通用，面试推荐）

```python
def lower(nums, target):            # 左边界：第一个 >= target
    l, r = 0, len(nums)             # 左闭右开
    while l < r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        else:
            r = m
    return l

def searchRange(self, nums, target):
    l = lower(nums, target)                    # 首
    if l == len(nums) or nums[l] != target:    # 不存在
        return [-1, -1]
    r = lower(nums, target + 1) - 1            # 尾（target+1 的下界 - 1）
    return [l, r]
```

**要点**：
- `lower` 用**左闭右开**（`l < r`、`r = m`、`l = m+1`）——天然返回"第一个 ≥ target"；
- 复用 `lower(target+1)` 而不是再写一个右边界函数——**一个函数两用**；
- `target+1` 是整数，避免浮点（±0.5 的进阶版，两者思路同源）。

## 四、复杂度

- 时间：O(logn)（2 次二分）
- 空间：O(1)

## 五、一刷 vs 二刷

- 一刷（9-17）：二分边界 AC ×2；
- 二刷（10-30）：一次 AC，±0.5 技巧直接想到——35 的 "return left" 模板思想在"边界"场景的变体。

## 六、关联题目（二分家族）

| 套路 | 相关题 |
|------|--------|
| 左边界（lower）| **35**（⚡ 母题，插入位置 = lower）、**278** 第一个坏版本、74 |
| 边界二合一 | 34 本体（lower + lower(target+1)-1） |
| 二分答案 | 875 珂珂、1011 D 天内送达、410 分割数组 |

**34 = 35 模板的"边界应用"**：会了 35 的 `return left`，34 就是"调两次 lower"，二分家族核心闭环。

## 七、一句话记住

> **首末位置 = 左边界函数两用：lower(target) 找首，lower(target+1)-1 找尾；lower 写左闭右开（l<r、r=m），不存在判断 nums[l]==target；±0.5/log+1 同理，建议 target+1 免浮点。**