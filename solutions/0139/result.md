# 139. 单词拆分 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 139. 单词拆分（Word Break）· 中等（动态规划分类第 6 题） |
| 链接 | https://leetcode.cn/problems/word-break/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-19 |
| 最终提交 | ✅ **ACCEPTED - 49/49 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.3 MB |

## 解法（用户记忆化递归"第一个单词" + 标准 DP"最后一个单词"）

**用户版**（top-down，从前拆）：

```python
def wordBreak(self, s, wordDict):
    mem = {'': True}
    def fun(s):
        if s not in mem:
            final = False
            for each_s in wordDict:
                if s.startswith(each_s) and fun(s[len(each_s):]):
                    final = True
                    break
            mem[s] = final
        return mem[s]
    return fun(s)
```

**标准版**（solution_readable.py，bottom-up，从后拆）：

```python
def wordBreak(self, s, wordDict):
    wd = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wd:
                dp[i] = True
                break
    return dp[len(s)]
```

## 322 → 139："凑"的字符串版

```
322：dp[i] = min(dp[i-c] + 1)           ← 凑金额
139：dp[i] = dp[j] and s[j:i] in dict   ← 拼字符串
```

**镜像视角**：322 用户用"最后一块硬币"（从后拆），139 用户用"第一个单词"（从前拆）——两个方向都对，拆分顺序无关。

## 验证

- 对拍 **2 万组随机字符串+字典 0 不一致**；
- 官方样例：`leetcode/["leet","code"]→true`、`applepenapple→true`、`catsandog→false`。

## 复杂度

- 时间 **O(n × k × L)**（n 子串 × k 单词 × startswith L）、空间 O(n)——满足要求。