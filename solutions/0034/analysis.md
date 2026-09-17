# 34. 在排序数组中查找元素的第一个和最后一个位置 · 解析

## 题目简述

升序数组（**含重复元素**）中找 target 的首次和末次下标，不存在返回 [-1, -1]。**要求 O(log n)**。

## 核心套路：两次 lower_bound（35 模板 ×2）

**关键转化**：

```
左边界 = 第一个 ≥ target 的位置           （lower_bound(target)）
右边界 = 第一个 ≥ target+1 的位置 - 1    （lower_bound(target+1) - 1）
         ↑ 因为有重复元素，target+1 是"下一个段"的起点
```

**两次二分凑齐答案，每次都是 35 的模板**：

```python
class Solution:
    def searchRange(self, nums, target):
        def lower_bound(t):                # 找第一个 >= t 的位置
            l, r = 0, len(nums)            # ★ 开区间（35 三件套）
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= t:
                    r = mid
                else:
                    l = mid + 1
            return l                       # 找不到时 = length（哨兵）

        lo = lower_bound(target)
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
        hi = lower_bound(target + 1) - 1   # 哨兵机制自动处理 "target 是最大"
        return [lo, hi]
```

## 用户补丁版 vs 标准哨兵版（本次问答的核心）

**用户版**（正确，但带边界补丁）：

```python
right = length - 1                        # 闭区间！
...
return [min_val, left if nums[-1] == target else (left - 1)]
#                        ↑ 补丁：target 是最大时不减，否则减 1
```

**为什么需要补丁**：第二次二分（找 ≥ target+1）用闭区间 `[0, length-1]`。"第一个 ≥ target+1"**不存在**（target 是最大值）时：
- 开区间写法：left 自然收敛到 **length**（数组末尾之后的哨兵）→ `left - 1` 直接得到最后一个下标；
- 闭区间写法：left 只能走到 **length-1**（最后一个元素），并且**恰好停在那**——所以需要 `nums[-1] == target` 识别"是不是停到底了"，是就不减。

**本质**：补丁在补偿"闭区间丢失了哨兵 length 这个合法结果"。标准版用开区间（`r = len(nums)`），哨兵回归，`- 1` 永远成立。

**用户疑问的答案**："target 是最大值时右边界直接用 left，否则 left-1"——**对，且分析精确**（他甚至意识到这里有个条件分支），只是这个分支是闭区间写法的副产物。

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**——严格满足题目 O(log n) 要求。

## 考点

- **两次 lower_bound 组合**（左 = ≥target，右 = ≥target+1 减一）
- **开区间 + 哨兵**（找不到边界的统一处理）
- 含重复数组的二分边界（闭区间写法在这类题最容易出补丁）

## 易错点

1. 闭区间写法丢哨兵 → 被迫加 if 补丁（本此主题）；
2. `lower_bound(target)` 后忘查 `nums[lo] != target` → 不存在误判；
3. 重复元素下用 `bisect_left`/`bisect_right` 混用（语义要对齐）；
4. 空数组特判（`[]` → [-1,-1]，本版已处理）；
5. 两次二分忘记中间重置 right（第二次从 length-1 或 length 重新开始）。

## 关联题

- 35（模板母题）、74（矩阵展平）、33（旋转数组）、153（旋转最小值）、4（中位数）；
- 34 是"边界二分"的入口——掌握后 33/153 只是加一个"旋转判定"。