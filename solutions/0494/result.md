# 494. 目标和 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 494. 目标和（Target Sum）· 中等（v2 新增题 · 记忆化搜索/DP） |
| 链接 | https://leetcode.cn/problems/target-sum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-25 |
| 最终提交 | ✅ **ACCEPTED - 146/146 用例通过**（leetgo 复提交） |
| 运行时间 | 210 ms |
| 内存 | 69.9 MB |

## 解法（用户记忆化搜索，自顶向下 DP）

```python
class Solution:
    def findTargetSumWays(self, nums, target):
        mem = {}

        def fun(index, target):
            if index < 0:
                return target == 0                       # 用完所有数，恰好归零
            if (index, target) not in mem:
                mem[(index, target)] = fun(index - 1, target + nums[index]) + \
                                       fun(index - 1, target - nums[index])
            return mem[(index, target)]

        return fun(len(nums) - 1, target)
```

## 是否符合题目要求 ✅

- 返回方案数 ✅；
- 时间 **O(n×S)**（S=sum，状态数）✅；
- 空间 O(n×S)（memo）✅。

**记忆化搜索 = 自顶向下 DP**，与自底向上 DP 本质相同，复杂度达标。

## 优化方向（用户询问）

### 优化 1（推荐）：数学变换 → 01 背包

```
把数组分正(P)、负(N)两组：
  sum(P) - sum(N) = target
  sum(P) + sum(N) = sum
  → 2·sum(P) = target + sum
  → sum(P) = (target + sum) / 2   ← 转"找子集和为 x 的方案数"
```

**空间 O(2×sum) → O(sum/2)**，且是 01 背包计数（416 同款）：

```python
def findTargetSumWays(self, nums, target):
    total = sum(nums)
    if abs(target) > total: return 0
    if (total + target) % 2: return 0     # 奇偶性剪枝
    s = (total + target) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    for n in nums:
        for j in range(s, n - 1, -1):     # 逆序 = 01 背包
            dp[j] += dp[j - n]
    return dp[s]
```

### 优化 2：剪枝

`abs(target) > 剩余和` 直接返回 0（memo 已够，锦上添花）。

## 验证

- 对拍 **3000 组随机 vs DP 参照 0 不一致**；
- 样例：`[1,1,1,1,1],3→5`、`[1],1→1`。

## 复杂度

- 时间 **O(n×S)**；空间 O(n×S)（01 背包版 O(S)）。