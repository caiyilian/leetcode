# 153. 寻找旋转排序数组中的最小值 · 解析

## 题目简述

升序数组在某点旋转（元素互异），找最小值。O(log n)。

## 核心套路：33 的段判断复用，比 `nums[right]` 不比 target

33 的灵魂是"判断 mid 在哪段"——153 同款，只是**基准换成 `nums[right]`（右端点必属小段）**：

```python
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:   # mid 在大段（旋转前的左侧）
                left = mid + 1            # 最小值必在右侧，mid 排除
            else:                         # mid 在小段（含最小值那段）
                right = mid               # ★ mid 可能就是最小值 → 保留
        return nums[left]
```

**直觉**：`nums[right]` 是小段的"天花板"——`nums[mid] > nums[right]` 说明 mid 还在大段（旋转前的左侧），最小值还没碰到，往右跳整段；否则 mid 已经在小段了，最小值在 [left..mid] 内往左收。

## ⚠️ 本次失败：`right = mid - 1` vs `right = mid`（力扣 749753993 WA）

**失败版**（注释都是对的，代码差一个字符）：

```python
else:                 # 用户注释："最小值在 [mid, right)"
    right = mid - 1   # ← [mid, right) 的 [ 表示包含 mid！但 -1 排除了 mid
```

**反例** `[3,1,2]`：mid=1 的 nums[1]=1 恰好是最小值 → `right = mid-1 = 0` → 最小值被跳过 → 返回 3 ❌

**该用什么收缩（记忆锚点）**：

| 二分类型 | 右侧收缩 | 左侧收缩 |
|---------|---------|---------|
| **找最小值 / lower_bound（35/153/34）** | `right = mid`（保留候选） | `left = mid+1`（排除） |
| 找精确值（33） | `right = mid-1` | `left = mid+1` |

**判断口诀**：**"mid 是不是可能答案？"是 → 保留（right=mid）；否 → 排除（mid±1）。** 找最小值时 mid 完全可能是答案，必须 `right = mid`。

**为什么 `left = mid+1` 在左边不矛盾**：`nums[right] < nums[mid]` 已确认 nums[mid] > nums[right]（且 mid 在大段）→ mid 不可能是最小值 → 排除安全。**排除的必要条件是"已证明 mid 不是答案"**，两边都要符合这个原则。

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**。

## 考点

- 段判断二分（33 同宗）
- **保留候选 vs 排除候选的收缩选择**（本次失败点）
- 未旋转（[11,13,15,17] → nums[0]）天然兼容：while 里 nums[right] < nums[mid] 恒假 → right 一路 = mid 收至 0 ✅

## 易错点

1. **`right = mid - 1` 排除掉最小值本人**（本次失败）；
2. 用 `nums[mid] >= nums[right]` 代替 `>`——元素互异时等号只在 mid==right（区间 2 元素）出现，`>` 更贴语义（81 含重复才需要 `>=` + 特殊处理）；
3. `while left < right`（收敛型）配合 `right=mid`，别混成 `left <= right + mid±1` 另一套；
4. 忘了未旋转 case（答案 = nums[0]）——标准解天然覆盖，别特判。

## 关联题

- **33**（同段判断，比 target）/ **35**（lower_bound 模板母题）/ **34**（两次调用）；
- **81**（含重复：`nums[mid]==nums[right]` 时 `right -= 1` 退化处理）——旋转二分进阶