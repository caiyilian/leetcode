# 152. 乘积最大子数组 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 152. 乘积最大子数组（Maximum Product Subarray）· 中等（动态规划分类第 8 题） |
| 链接 | https://leetcode.cn/problems/maximum-product-subarray/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 191/191 用例通过**（leetgo 复提交） |
| 运行时间 | **7 ms（击败 71%）** |
| 内存 | 20.6 MB |

## 解法（用户双状态 DP，逻辑完美）

```python
class Solution:
    def maxProduct(self, nums):
        n = len(nums)
        dp_po = [1] * (n + 1)    # 以 nums[i-1] 结尾的最大乘积
        dp_ne = [1] * (n + 1)    # 以 nums[i-1] 结尾的最小乘积
        best = float("-inf")
        for i in range(n):
            dp_po[i + 1] = max(nums[i] * dp_po[i], nums[i] * dp_ne[i], nums[i])
            dp_ne[i + 1] = min(nums[i] * dp_po[i], nums[i] * dp_ne[i], nums[i])
            best = max(dp_po[i + 1], best)
        return best
```

**用户命名亮点**：`dp_po`（positive）/`dp_ne`（negative）一眼看出两个状态含义。

## 双状态的核心：负负得正

`dp_ne`（最小乘积）看似多余，实为**关键**——`[-2,3,-4]` 中 dp_ne 一路记录最负值，最后 `-4 × dp_ne(=-6) = 24` 反超正数路径。**乘法比加法多一个"符号翻转"的坑**，所以需要同时维护最大和最小两个状态。

## 53 → 152：加法到乘法

```
53 最大子数组和：dp[i] = max(dp[i-1] + nums[i], nums[i])   ← 单状态（求和无符号问题）
152 乘积最大：  双状态（乘法负负得正，需额外维护最小值）
```

## 小优化（非必须）

dp_po/dp_ne 只依赖前一个 i，可滚动成两个变量（O(1) 空间）。但 O(n) 数组版更清晰，题目不卡空间——滚动变量是锦上添花。

## 验证

- 对拍 **5 万组随机数组（含负数/零）0 不一致**；
- 官方样例：`[2,3,-2,4]→6`、`[-2,0,-1]→0`、`[-2]→-2`、`[-2,3,-4]→24`（负负得正）。

## 复杂度

- 时间 **O(n)**；空间 O(n)（可优化到 O(1)）。