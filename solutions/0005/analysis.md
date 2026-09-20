# 5. 最长回文子串 · 解析

## 题目简述

求字符串中最长的回文子串。`babad` → `bab`（或 `aba`）。

## 核心套路：中心扩展法

回文有**两种中心**，都要枚举：

```
奇数回文：aba   中心是单个字符 b
偶数回文：abba  中心是两个字符 bb
```

```python
def longestPalindrome(self, s):
    n = len(s)
    best = s[0]
    for i in range(n):
        # 奇数中心 (i, i)
        l = r = i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > len(best): best = s[l:r+1]
            l -= 1; r += 1
        # 偶数中心 (i, i+1)
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > len(best): best = s[l:r+1]
            l -= 1; r += 1
    return best
```

## 多退一步的边界

while 退出时 `left`/`right` 已经**越界一步**（或字符不等），所以真实回文：
- 长度 = `right - left - 1`
- 内容 = `s[left+1 : right]`

这是中心扩展法最容易错的地方，用户拿捏准确。

## 三种解法

| 方法 | 复杂度 | 说明 |
|------|--------|------|
| 中心扩展 | O(n²) / O(1) | 最直观，面试首选 |
| DP | O(n²) / O(n²) | `dp[i][j] = s[i]==s[j] and dp[i+1][j-1]`（子串长度递增填表） |
| Manacher | O(n) / O(n) | 竞赛技巧，不要求 |

## 复杂度

- 时间 **O(n²)**；空间 O(1)。

## 考点

- 中心扩展（奇数/偶数双中心）
- 字符串回文判断
- "多退一步"边界

## 易错点

1. 只写奇数中心，漏偶数回文（`cbbd`）；
2. while 退出后 left/right 多退一步，长度/切片算错；
3. 空串或单字符的边界；
4. `best` 初始化为 s[0]（至少一个字符）。

## 关联题

- **647 回文子串**（数所有回文子串，同中心扩展）；
- **516 最长回文子序列**（DP）；
- 1143 最长公共子序列 / 72 编辑距离（字符串 DP 进阶）。