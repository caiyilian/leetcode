# 96. 不同的二叉搜索树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 96. 不同的二叉搜索树（Unique Binary Search Trees）· 中等（v2 新增题 · 卡特兰数） |
| 链接 | https://leetcode.cn/problems/unique-binary-search-trees/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-21 |
| 最终提交 | ✅ **ACCEPTED - 19/19 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19 MB |

## 解法（用户卡特兰数 DP，标准）

```python
class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]   # 左 j 个 × 右 i-1-j 个
        return dp[n]
```

## 核心：以 j 为根的分解

`dp[i]` = i 个节点能构成的 BST 数量。枚举根节点 j：
- 左子树有 j 个节点（`dp[j]` 种形态）；
- 右子树有 `i-1-j` 个节点（`dp[i-1-j]` 种形态）；
- 相乘累加 → `dp[i] = Σ dp[j] * dp[i-1-j]`。

这就是**卡特兰数**的递推式，闭式解为 `C(2n,n)/(n+1)`。

## 验证

- 对拍 **n=0..19 与卡特兰数公式 C(2n,n)/(n+1) 全部一致**；
- 样例：n=3→5、n=1→1。

## 复杂度

- 时间 **O(n²)**；空间 O(n)。