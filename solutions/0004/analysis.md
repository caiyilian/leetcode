# 4. 寻找两个正序数组的中位数 · 解析

## 题目简述

两个升序数组，O(log(m+n)) 找合并后的中位数。

## 核心套路：切割二分（在两个数组各切一刀，不合并）

**中位数定义**：合并数组分左右两半，左半全 ≤ 右半，且左半 = 右半（或左多 1）。**不真合并**（O(m+n) 太慢），在两个原数组各切一刀：

```
            small = [1, 3]         big = [2]
                      ↑ i=1                ↑ j=1
左半 = small[:1] + big[:1] = [1,2]   （num_half = (3+1)//2 = 2 个）
右半 = small[1:] + big[1:] = [3]

切割合法 ⇔ L1 ≤ R2 且 L2 ≤ R1（左半每个都不大于右半每个）
  L1=1 ≤ R2=+∞ ✅    L2=2 ≤ R1=3 ✅
→ 奇数：max(L1,L2)=2 ✅
```

**三个支柱**：

1. **左半数量固定**：`num_half = (m+n+1)//2`，且 `i + j == num_half`（j = num_half - i 自动跟随，**只有一个自由度 i**）；
2. **只在短数组上二分**：`small` 是较短的 → 二分 i ∈ [0, m] → **O(log(min(m,n)))**；
3. **四个边界值 + 显式哨兵**：L1/R1/L2/R2 是切割口两侧四个元素，`i=0` → L1=-∞、`i=m` → R1=+∞（j 同理）——**免疫负索引和越界**。

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m <= n:
            small, big = nums1, nums2
        else:
            small, big = nums2, nums1
            m, n = n, m                      # ★ 保证二分在短数组上
        num_half = (m + n + 1) // 2
        left, right = 0, m
        while left <= right:                 # ★ 闭区间（i=m 可取）
            i = (left + right) // 2
            j = num_half - i
            L1 = small[i-1] if i > 0 else float('-inf')
            L2 = big[j-1]   if j > 0 else float('-inf')
            R1 = small[i]   if i < m else float('inf')
            R2 = big[j]     if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:
                if (m+n) % 2: return max(L1, L2)
                return (max(L1, L2) + min(R1, R2)) / 2
            if L1 > R2:
                right = i - 1                # small 左侧取多了
            else:
                left = i + 1                 # small 左侧取少了
```

## ⚠️ v1 → v2 教训：数量语义 vs 索引语义（用户踩坑实录）

**v1（索引语义，3 个 bug）**：用户第一版把 mid 当"索引+1"，被迫推导 `index_big = num_half - mid - 2` 魔法数：

```
bug1 奇数分支 return max(small_right, ...) —— 用了右半第一个当左半最大
bug2 m==n 时 index_big=-1 → big[-1] 负索引取尾部元素（语义全错）
bug3 while left < right 无 i=m 分支 → 合法切割在边界时循环退出无 return（None）
```

**v2（数量语义，定稿）**：`i` = "small 左半有几个元素" → 边界值直接 `small[i-1]`/`small[i]`，**不再需要任何魔法数**；`while left <= right` + 显式哨兵覆盖全部边界。

**⚡ 通用教训（比 4 本身值钱）**：

> **能避免的派生下标一律避免。** "数量 → 边界值"直译（i 个元素 → small[i-1] 是左半最后、small[i] 是右半第一）永远比"索引推导数量"（num_half-mid-2 这种）少一个出错面。
> 同类警钟：74 的 `mid//n`（除数用错）——**数学推导下标 = 隐藏炸弹的工厂**。

## 复杂度

- 时间 **O(log(min(m,n)))**（在短数组二分，每次 O(1) 检查）；空间 **O(1)**。

## 考点

- 中位数的切割定义（左半数量固定）
- **单自由度二分**（i+j=half 消元）
- 显式哨兵（±inf 替代边界 if 风暴——更不易错）
- 短数组二分（log 是 min 不是 max）

## 易错点

1. **索引/数量语义混用**（v1 三个 bug 的总根源）；
2. 哨兵用 `float('-inf')/float('inf')`（`-10**9` 硬编码在极端用例会错）；
3. `while left <= right`（闭区间）才能取到 i=m——忘了空数组/全左场景会死循环或 None；
4. `(m+n+1)//2` 写成 `(m+n)//2`——奇数时左半少 1，max(L1,L2) 取错；
5. 忘记交换 small/big（二分必须落在短数组上才 O(log min)）；
6. `L1 > R2` 时 `right = i-1`（不是 i）——i 已被检查过，排除是安全的（153 的"mid 是否可能答案"原则的镜像）。

## 关联题

- 二分家族全家桶：35（母题）/ 74（展平）/ 34（双调用）/ 33（段判断）/ 153（比 right）/ 4（切割二分）；
- **295 数据流的中位数**（进阶：动态插入场景，双堆法）。