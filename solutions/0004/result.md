# 4. 寻找两个正序数组的中位数 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 4. 寻找两个正序数组的中位数（Median of Two Sorted Arrays）· **困难**（二分查找分类收官题） |
| 链接 | https://leetcode.cn/problems/median-of-two-sorted-arrays/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 2099/2099 用例通过**（leetgo 复提交，用户力扣原提交已过） |
| 运行时间 | 0 ms / 7 ms（leetgo 噪声，击败 19%） |
| 内存 | 19.3 MB |

## 解法（用户两版演进终成标准切割二分）

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m <= n:
            small, big = nums1, nums2
        else:
            small, big = nums2, nums1
            m, n = n, m
        num_half = (m + n + 1) // 2          # 左半元素总数（奇数左多 1）
        left, right = 0, m
        while left <= right:
            i = (left + right) // 2          # i = small 左半元素个数
            j = num_half - i                 # big 左半元素个数
            L1 = small[i-1] if i > 0 else float('-inf')   # 显式哨兵
            L2 = big[j-1]   if j > 0 else float('-inf')
            R1 = small[i]   if i < m else float('inf')
            R2 = big[j]     if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:        # 切割合法
                if (m+n) % 2:
                    return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2
            if L1 > R2:
                right = i - 1                # small 左半取多了
            else:
                left = i + 1                 # small 左半取少了
```

## v1 → v2 演进（用户自驱 + 一次关键重构）

**v1（"索引语义"，有 3 个 bug）**：mid 当"索引+1"，`index_big = num_half - mid - 2` 魔法数推导 → ① 奇数分支误用 small_right（应为 small[mid]）② m==n 时 index_big=-1 负索引 ③ while left<right 无 i=m 兜底。

**v2（"数量语义"，定稿）**：i = 左半元素个数 → L1/R1/L2/R2 四个边界值一目了然、显式哨兵免疫越界、闭区间 while left<=right 覆盖空数组。

**⚡ 教训：二分切割题，变量语义用"数量"比用"索引"少一半出错面。**

## 验证

- 对拍 **5 万组随机数组 vs sorted 合并取中位数 0 不一致**；
- 官方样例：`[1,3]+[2]→2.0`、`[1,2]+[3,4]→2.5`；
- 边界：单空数组 `[]+[1]→1`、`[2]+[]→2`、全等 `[1,1,1,1]+[1,1,1,1]→1`、`[0,0]+[0,0]→0`。

## 复杂度

- 时间 **O(log(min(m,n)))**（只在短数组上二分）；空间 **O(1)**。

## 🏆 二分查找家族 6/6 全通关！（35 → 74 → 34 → 33 → 153 → 4）