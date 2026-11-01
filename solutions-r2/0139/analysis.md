# 139. 单词拆分 · 解析（二刷）

## 一、核心思路：前缀可拆性 DP

**问题**：s 能否由 wordDict 中的单词拼接而成（单词可重复使用）。

**关键洞察**：`dp[i]` = s 的前 i 个字符能否被完全拆分。判断 dp[i] 时，只需要关注**最后一段切片 `s[j:i]`**——它是字典里的一个单词，且剩下的前缀 `s[0:j]` 可拆：

```
dp[i] = True  ⟺  存在 j ∈ [0, i)：dp[j] = True 且 s[j:i] ∈ wordDict
dp[0] = True（空串天然可拆）
```

**为什么是"最后一段"而不是"第一段"**：从前往后推时，dp[j]（更短前缀）已经算好，拿它当"已完成的前半"，只有"尾部"是未知——这是字符串 DP 的标准切法。

## 二、两种写法（你的反向排除版 + 标准正向版）

```python
# 用户版：反向排除（默认 True，无解才 False）
dp = [True] * (length + 1)
for i in range(1, length + 1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            break
    else:              # for-else：循环没 break
        dp[i] = False
return dp[-1]

# 标准版：正向置真
dp = [False] * (n + 1)
dp[0] = True
for i in range(1, n + 1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break
return dp[n]
```

**⚡ for-else 语法**：`for...else` 的 else 在**循环完整跑完（没被 break）**时执行。用户版利用它表达"所有 j 都试过了没有能接上的"——比标准版少写一个初始化分支，更 Pythonic。

## 三、⚡ 复杂度与剪枝（大用例防 TLE）

- 时间：O(n²·L)——内层 j 从 0 到 i，每次切片 `s[j:i]` 长度 L 参与字典哈希
- 空间：O(n)

**优化**：最后一段不可能比字典里最长单词还长，所以 j 只要从 `i - max_len` 开始扫：

```python
max_len = max(len(w) for w in wordDict)
for j in range(max(0, i - max_len), i):
    ...
```

小用例无感，遇到"长串 + 短字典"的隐藏用例能防超时（面试提一句即可）。

## 四、一刷 vs 二刷

- 一刷（9-19）：AC ×2；
- 二刷（11-01）：一次 AC 且自动选择了反向排除写法——前缀 DP 模型完全内化。

## 五、关联题目

| 套路 | 相关题 |
|------|--------|
| 前缀可拆 DP | **139 本体**、**140 单词拆分 II**（回溯求所有拆法） |
| 字符串 DP | 5 最长回文子串、**72 编辑距离**（已归档待二刷）、1143 最长公共子序列 |
| 集合判存 | **49 字母异位词分组**（已做）、**128 最长连续序列**（已做） |

**139 → 140**：139 只问能否拆（布尔 DP），140 要求列出所有拆法（DP + 回溯）——140 是 139 的上位，常说"先会 139 再碰 140"。

## 六、一句话记住

> **139 = dp[i] 前缀可拆性：存在 j 使 dp[j] 真且 s[j:i]∈字典；⚡ for-else 反向排除是 Python 加分写法；剪枝 j 从 i-max_len 起步。**