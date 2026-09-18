# 118. 杨辉三角 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 118. 杨辉三角（Pascal's Triangle）· 简单（动态规划分类第 2 题 / 二维 DP 入门） |
| 链接 | https://leetcode.cn/problems/pascals-triangle/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 30/30 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.1 MB |

## 解法（用户二维 DP + 补零法）

```python
class Solution:
    def generate(self, numRows):
        result = [[1]]
        for i in range(1, numRows):
            result.append([])
            for j in range(i+1):
                v_im1_jm1 = result[i-1][j-1] if j-1 >= 0 else 0   # 左上（越界补 0）
                v_im1_j   = result[i-1][j]   if j < i   else 0   # 正上（越界补 0）
                result[-1].append(v_im1_jm1 + v_im1_j)
        return result
```

**用户命名亮点**：`v_im1_jm1` / `v_im1_j` / `val_i_j` 对应 dp[i-1][j-1] / dp[i-1][j] / dp[i][j]，与 70 的 `val_im2/val_im1/val_i` 一脉相承的"下标语义化命名"。

**补零法**：`j-1 < 0 或 j >= i 时取 0`——用"虚拟 0"补齐左右两侧，让每个数走同一个公式 `左上 + 正上`，不用单独处理每行首尾的 1。

## 用户疑问解答：用了 DP 吗？——用了，标准二维 DP

```
① 状态：dp[i][j] = 第 i 行第 j 个数
② 转移：dp[i][j] = dp[i-1][j-1] + dp[i-1][j]（左上 + 正上）
③ 填表：第 i 行由第 i-1 行推出来（从底向上）
```

**70 → 118：一维 DP → 二维 DP**（状态多一维，骨架不变）。

## 复杂度

- 时间 **O(n²)**、空间 **O(n²)**——杨辉三角固有复杂度（必须输出 n²/2 个数）。

## 验证

- 对拍 **numRows=1..30 全量 vs 组合数 C(n,k) 0 不一致**。