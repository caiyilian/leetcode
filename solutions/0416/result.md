# 416. 分割等和子集 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 416. 分割等和子集（Partition Equal Subset Sum）· 中等（动态规划分类第 9 题 / 0-1 背包） |
| 链接 | https://leetcode.cn/problems/partition-equal-subset-sum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 149/149 用例通过**（leetgo 复提交） |
| 运行时间 | 2502 ms（二维 DP；一维滚动版更快） |
| 内存 | 49.3 MB |

## ⚠️ 失败历程记录（用户要求，多次迭代）

| 迭代 | 错误 | 说明 |
|------|------|------|
| 力扣 750243519（WA） | `target = sum//2 + 1` | 多加 1，后面 `return (target-1)==...` 打补丁越补越乱 |
| 力扣 750243519（WA） | `[[0]*target]*num_obj` | **浅拷贝**（未修复） |
| 力扣 750243519（WA） | `if j > nums[i]` + `else: continue` | 应 `j >= nums[i]`；continue 让 dp[i][j] 未赋值 |
| 本地迭代 1 | `[[0]*num_arr]*num_obj` | **浅拷贝**（致命） |
| 本地迭代 2 | `if i >= nums[i]` | **量纲错误**（i 是下标、nums[i] 是重量） |
| 本地迭代 3 | ✅ 修正 | 列表推导式 + `j >= nums[i]` |

### 核心易错点（三个）

1. **浅拷贝 `[[0]*n]*m`**：m 行指向同一个列表，改一行全改——二维数组必须用列表推导式 `[[0]*n for _ in range(m)]`；
2. **量纲错误 `i >= nums[i]`**：应 `j >= nums[i]`（比较的是容量 j 和重量 nums[i]，不是下标 i）；
3. **本地/力扣不同步**：力扣网页改的版本和 test.py 分叉，本地改对、力扣还停在旧版——以后改完记得同步。

## 解法（用户二维 DP + 一维滚动版）

**用户二维版**（solution.py）：

```python
dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])   # 不放 / 放
return dp[n-1][target] == target    # 价值==重量，dp 值即凑出的重量
```

**一维滚动版**（solution_readable.py，0/1 背包标准）：

```python
dp = [0] * (target + 1)
for num in nums:
    for j in range(target, num - 1, -1):   # ★ 从后往前
        dp[j] = max(dp[j], dp[j - num] + num)
return dp[target] == target
```

## 核心思路

- 能否平分成两半 ⇔ 能否凑出 sum/2 的子集；
- 转化为 0/1 背包：物品 = 数字（重量=价值=num），容量 = sum/2；
- 价值==重量时，`dp[target] == target` 说明恰好凑出。

## 验证

- 对拍 **2 万组随机数组 vs 一维背包 0 不一致**；
- 官方样例：`[1,5,11,5]→true`、`[1,2,3,5]→false`、`[2,2,3,5]→false`、`[2,2,1,1]→true`。

## 复杂度

- 二维：时间 O(n×target)、空间 O(n×target)；
- 一维滚动：时间 O(n×target)、空间 O(target)。