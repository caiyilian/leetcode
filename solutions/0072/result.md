# 72. 编辑距离 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 72. 编辑距离（Edit Distance）· 中等（字符串 DP 双经典之二） |
| 链接 | https://leetcode.cn/problems/edit-distance/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 1149/1149 用例通过**（leetgo 复提交） |
| 运行时间 | 59 ms |
| 内存 | 22.4 MB |

## 解法（用户标准编辑距离 DP，注释清晰）

```python
class Solution:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1): dp[0][j] = j    # 空 → word2：全插入
        for i in range(m + 1): dp[i][0] = i    # word1 → 空：全删除
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]                 # 相等：不变
                else:
                    insert_count  = dp[i][j-1] + 1           # 插入（从左来）
                    delete_count  = dp[i-1][j] + 1           # 删除（从上文来）
                    replace_count = dp[i-1][j-1] + 1         # 替换（从左上）
                    dp[i][j] = min(insert_count, delete_count, replace_count)
        return dp[m][n]
```

## 1143 → 72：LCS 的兄弟

```
1143 LCS：相等 → 左上+1；不等 → max(上, 左)         ← 只"匹配"或"丢"
72 编辑距离：相等 → 左上；不等 → min(左+1, 上+1, 左上+1)  ← 三种操作
```

**三种操作的方向**（用户注释准确）：
- **插入** `dp[i][j-1]+1`：word1 前 i 已转成 word2 前 j-1，再插入 word2[j-1]；
- **删除** `dp[i-1][j]+1`：word1 前 i-1 已转成 word2 前 j，删掉 word1[i-1]；
- **替换** `dp[i-1][j-1]+1`：前 i-1 转前 j-1，再把 word1[i-1] 换成 word2[j-1]。

## 验证

- 对拍 **2 万组随机串 vs 记忆化递归 0 不一致**；
- 样例：`horse/ros→3`、`intention/execution→5`。

## 复杂度

- 时间 **O(m×n)**；空间 O(m×n)（可滚动到 O(n)）。

## 🎓 字符串 DP 双经典（5 / 1143 / 72）全部完成