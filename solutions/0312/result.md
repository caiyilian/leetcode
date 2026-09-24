# 312. 戳气球 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 312. 戳气球（Burst Balloons）· **困难**（v2 新增题 · 区间 DP） |
| 链接 | https://leetcode.cn/problems/burst-balloons/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-24 |
| 最终提交 | ✅ **ACCEPTED - 73/73 用例通过**（leetgo 复提交） |
| 运行时间 | 2045 ms |
| 内存 | 21.7 MB |

## 解法（用户区间 DP，反向思维）

```python
class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]          # 补两端哨兵 1
        length = len(nums)
        dp = [[0] * length for _ in range(length)]
        for each_len in range(2, length):        # 区间长度从小到大
            for i in range(0, length - each_len):
                j = i + each_len
                for k in range(i + 1, j):        # k = 最后戳的气球
                    now = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    dp[i][j] = max(dp[i][j], now)
        return dp[0][length - 1]
```

## 核心：枚举"最后一个戳的气球"（反向思维）

**正向思考会死**：按"第一个戳哪个"分解，戳掉后左右连通、边界互相影响，子问题不独立。

**反向思考破局**：枚举**最后一个戳的 k**——戳 k 时其他都戳完了，k 的邻居就是边界 i、j，左右两半 `(i,k)`、`(k,j)` 完全独立：

```
dp[i][j] = max over k of  dp[i][k] + nums[i]*nums[k]*nums[j] + dp[k][j]
```

## 用户疑惑解答：`dp[i][k]` 在 k=i+1 时为 0，对吗？

**对！** `dp[i][j]` 是**开区间** `(i,j)` 内的金币（不含边界）。当 `k = i+1` 时，`dp[i][i+1]` 是长度 1 的区间，**内部没有气球**（`i < x < i+1` 无解）→ **空区间 = 0**。

**关键**：全 0 初始化 `[[0]*length]` 恰好给了所有"长度 1 空区间"正确的值 0，**不需要额外 base case**。dp 表对角线上方一格（dp[0][1]、dp[1][2]…）全是 0，正是这个道理。

## 验证

- 对拍 **5000 组随机数组 vs 记忆化递归 0 不一致**；
- 样例：`[3,1,5,8]→167`、`[1,5]→10`。

## 复杂度

- 时间 **O(n³)**（区间数 O(n²) × 枚举 k 的 O(n)）；空间 O(n²)。