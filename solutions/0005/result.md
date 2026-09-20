# 5. 最长回文子串 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 5. 最长回文子串（Longest Palindromic Substring）· 中等（字符串 DP 开张） |
| 链接 | https://leetcode.cn/problems/longest-palindromic-substring/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 144/144 用例通过**（leetgo 复提交） |
| 运行时间 | **179 ms（击败 90%）** |
| 内存 | 19.2 MB |

## 解法（用户中心扩展法）

```python
class Solution:
    def longestPalindrome(self, s):
        length = len(s)
        if length == 1:
            return s
        max_length = 1
        best = s[0]
        for i in range(length):                      # 奇数回文：中心 (i,i)
            left, right = i, i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1; right += 1
            if max_length < (right - left - 1):
                max_length = right - left - 1
                best = s[left + 1:right]
        for i in range(length - 1):                  # 偶数回文：中心 (i,i+1)
            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1; right += 1
            if max_length < (right - left - 1):
                max_length = right - left - 1
                best = s[left + 1:right]
        return best
```

## 关键理解

1. **两种中心**：奇数回文（`aba` 中心是 `b`）+ 偶数回文（`abba` 中心是 `bb`）——两个都枚举才不会漏（很多人只写奇数中心，`cbbd` 就漏了）；
2. **多退一步边界**：while 退出时 left/right 已越界一步，真实长度 = `right - left - 1`，内容 = `s[left+1:right]`。

## 三种解法对比

| 方法 | 复杂度 | 特点 |
|------|--------|------|
| **中心扩展**（用户） | O(n²) / O(1) | 最直观，面试首选 ✅ |
| DP | O(n²) / O(n²) | `dp[i][j] = s[i]==s[j] and dp[i+1][j-1]` |
| Manacher | O(n) / O(n) | 竞赛技巧，不要求 |

## 验证

- 对拍 **3 万组随机串 0 不一致**；
- 官方样例：`babad→bab`、`cbbd→bb`、`a→a`。

## 复杂度

- 时间 **O(n²)**；空间 O(1)。