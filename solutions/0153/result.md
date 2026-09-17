# 153. 寻找旋转排序数组中的最小值 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 153. 寻找旋转排序数组中的最小值（Find Minimum in Rotated Sorted Array）· 中等（二分查找分类第 5 题） |
| 链接 | https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 150/150 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）+ 内存击败 80%** |

## ⚠️ 本次失败记录（用户要求：力扣 749753993 WA）

**失败版 vs 通过版只差一个字符**：

```python
# 失败版（WA）：注释写了"最小值在 [mid, right)" 但代码却——
else: right = mid - 1     # ❌ mid 可能是最小值，被 -1 跳过了

# 通过版（AC）：
else: right = mid         # ✅ mid 在小段 → 最小值可能是 mid 本身，必须保留
```

**反例**：`[3,1,2]` 失败版：mid=1(值 1) 是最小值 → `right=mid-1=0` 跳过 → 返回 nums[0]=3 ❌（应为 1）。

## 解法（用户通过版）

```python
class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1       # mid 在大段 → 最小值在右，mid 可排除
            else:
                right = mid          # ★ mid 在小段 → 最小值可能=mid，保留（不是 mid-1）
        return nums[left]
```

## 验证

- 对拍 **5 万组随机旋转数组（含未旋转/全旋转/单元素）vs min() 参照 0 不一致**；
- 官方样例：`[3,4,5,1,2]→1`、`[4,5,6,7,0,1,2]→0`、`[11,13,15,17]→11`（未旋转）、`[1]→1`、`[2,1]→1`。

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**。

## ⚡ 通用规律（比这题本身值钱）

**"找最小值/找第一个满足条件"的二分，mid 可能是答案 → 区间收缩必须保留它**：
- 右侧收缩 `right = mid`（保留 mid）
- 左侧收缩 `left = mid + 1`（排除 mid——只有当确认 mid 不是答案才排除）

这就是 35 模板三件套 `right=mid / left=mid+1` 的深层原因（lower_bound 规律）；33 那种"找精确值"才用 `mid±1`。**两套别混**——本次失败就是把"精确值的 mid-1 习惯"套到了"找最小值"上。