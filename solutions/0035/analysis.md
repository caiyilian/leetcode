# 35. 搜索插入位置 · 解析

## ⚡⚡ 机考之前必看：这是二分模板的"母题"（35/34/33/153/4 全是它换皮）

## 题目简述

有序数组（无重复）中找 target：有则返回下标，无则返回**应该插入的位置**（保持有序）。

**等价语义**：找**第一个 ≥ target** 的元素下标（`bisect_left`）。target 比全部都大时答案是 length（数组末尾之后）。

## ⚡ 标准二分模板（背住三件套）

```python
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)          # ① 左闭右开 [left, right)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:         # 找第一个 >= target → 右边界收缩
                right = mid
            else:
                left = mid + 1              # ② 唯一关键：mid+1 保证收敛
        return left                          # ③ while 结束 left==right==答案
```

**为什么三件套缺一不可**：

1. **`right = len(nums)` 开区间**：让"答案可能 = length"（target 比全部大）天然成立——闭区间写 `right = len-1` 时 length 答案要特判；
2. **`left = mid + 1`（防死循环的灵魂）**：当区间剩 2 个元素（left+1==right）时 `mid == left`，若 `left = mid` 则 left 原地不动 → 死循环；`mid+1` 保证每次至少缩小 1；
3. **`nums[mid] >= target` 时收缩 right**：边界相等也算"插入点"（找第一个 ≥），配合 `bisect_left` 语义。

**记忆锚点：二分模板的骨架不能省——`left = mid + 1` 少了它，就得用三个 return 补丁来救（用户版的真实经历）。**

## 用户版（补丁版）剖析：为什么它也正确

```python
while left < right:
    middle = (right + left) // 2
    if nums[middle] == target: return middle
    if nums[middle] > target:
        if right == middle: return right - 1   # 提前 return
        right = middle
    else:
        if left == middle: return left + 1     # 提前 return
        left = middle
return 0                                        # 兜底（仅 target 最小才到这）
```

- 用户写 `left = middle`（没 +1）→ 区间不能自然收敛 → 被迫在 `left == middle`（区间剩 1 元素）时提前 return `left+1`；right 侧靠 `right = middle` 收敛，`right == middle` 时提前 return；
- **`return 0` 之谜**：while 能正常退出的唯一路径是 right 一路收缩到 0（target < 全数组）→ 兜底 0 恰好正确。所有其他答案都被提前 return 接住了；
- 5 万组对拍证明它**碰巧完备**——但这是"补丁拼出来的正确"，改一处就可能漏（比如删掉某个提前 return 分支）。

**教训：先写对模板，再谈优化。骨架对了就不需要补丁。**

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**。

## 考点

- 二分"找边界"变体（≥ 而非 ==）
- **左闭右开 + mid+1 的模板**（34/33/153/4 全部依赖）

## 易错点

1. `mid = (left+right)//2` 用 `//`（取整）；`left + 1` 忘加 → 死循环；
2. 用 `>` 而不是 `>=` → 重复元素时插错位置（35 无重复不影响，但 34 首尾位置题必错）；
3. 返回 `left` 而不是 `right`（相等无所谓，但语义是 left）；
4. 闭区间写法（right = len-1）时忘了"答案=length"的特判。

## 关联题（二分模板家族）

- **34 在排序数组中查找元素的第一个和最后一个位置**（两次二分：≥ 与 > 边界）；
- 33 搜索旋转排序数组 / 153 寻找旋转排序数组中的最小值（旋转二分）；
- 4 寻找两个正序数组的中位数（困难，二分进阶）。