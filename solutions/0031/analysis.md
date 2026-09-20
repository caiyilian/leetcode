# 31. 下一个排列 · 解析

## 题目简述

原地把数组重排成"字典序的下一个更大排列"（不存在则重排成最小排列）。

## 核心套路：三步算法

```
① 从右往左找第一个升序对 nums[index] < nums[index+1]
   （index 是"要变大的位置"，它右边都是降序）
② 在右边降序区找"最小的大于 nums[index] 的数"，与 nums[index] 交换
③ 反转 index+1 到末尾（降序 → 升序，得到最小的更大排列）
```

```python
# ①
for i in range(length):
    index = length - 1 - i
    if index < length - 1 and nums[index] < nums[index+1]:
        break
else:
    index = -1     # 完全降序

# ② 右边降序，找"最小的大于 nums[index] 的数"（= 第一个 <= index 的前一个）
for j in range(index+1, length):
    if nums[j] <= nums[index]:
        nums[index], nums[j-1] = nums[j-1], nums[index]
        break
else:
    nums[index], nums[length-1] = nums[length-1], nums[index]

# ③ 反转
left, right = index+1, length-1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1; right -= 1
```

## 为什么第②步必须是 `<=`（用户 WA 点）

右边是降序，要找"最小的大于 nums[index] 的数"= 第一个 `nums[j] <= nums[index]` 的**前一个位置**。右边含**等于** nums[index] 的元素时：

```
[1,2,1]：index=0，右边 [2,1]
  <= ：j=2 时 nums[2]=1 <= 1 → j-1=1 交换 → [2,1,1] ✅
  <  ：j=2 时 nums[2]=1 < 1? 否 → 走 else 交换 nums[0]↔nums[2] → [1,1,2] ❌
```

**记忆锚点：找"最小的大于"用 `<=` 找第一个"不大于"的，取它前一个。**

## 复杂度

- 时间 **O(n)**；空间 O(1)。

## 考点

- 字典序下一个排列的三步法
- 原地重排
- "最小的大于"用 `<=` 的细节

## 易错点

1. 第②步 `<=` 写成 `<`（右边含相等元素时错位，用户 WA 点）；
2. 完全降序时 index=-1，反转整个数组；
3. 交换后要反转后半段（不是排序，因为后半段是降序，反转即升序）。

## 关联题

- **46 全排列**（生成所有排列，已 AC）；
- **75 颜色分类**（原地重排，已 AC）；
- 556 下一个更大元素 III（同思路数字版）。