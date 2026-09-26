# 647. 回文子串 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 647. 回文子串（Palindromic Substrings）· 中等（v2 新增题 · 中心扩展法） |
| 链接 | https://leetcode.cn/problems/palindromic-substrings/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-26 |
| 最终提交 | ✅ **ACCEPTED - 132/132 用例通过**（leetgo 复提交） |
| 运行时间 | 99 ms（击败 91%） |
| 内存 | 19.1 MB |

## 解法（用户中心扩展法，奇数 + 偶数双中心）

```python
class Solution:
    def countSubstrings(self, s):
        length = len(s)
        count = 0
        # 奇数中心：单字符为中心（"aba" 型）
        for i in range(length):
            left = right = i
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1; right += 1; count += 1
        # 偶数中心：相邻字符对中间为中心（"abba" 型）
        for i in range(length - 1):
            left, right = i, i + 1
            while left >= 0 and right < length and s[left] == s[right]:
                left -= 1; right += 1; count += 1
        return count
```

## 是否符合题目要求 ✅

| 要求 | 达标 |
|------|------|
| 返回回文子串个数 | ✅ |
| 时间 | ✅ O(n²)（2n-1 个中心，每个扩展 O(n)） |
| 空间 | ✅ **O(1)**（只用指针变量） |

**中心扩展法空间 O(1)**，比 DP（O(n²) 空间）更优，是这题的主流解。

## 核心：中心扩展（与 5 同源）

每扩展成功一次（左右字符相等）= 找到一个回文子串 → count += 1。

```
奇数中心："aba" → 中心 a 向两边扩出 a、aba（2 个）
偶数中心："abba" → 中心 bb 向两边扩出 bb、abba（2 个）
```

## 与 5 最长回文子串的对比

| | 5 最长回文子串 | 647 回文子串 |
|--|--------------|-------------|
| 求 | 最长长度 | **个数** |
| 中心扩展 | 找 max | **每成功一次计数** |
| 复杂度 | O(n²)/O(1) | O(n²)/O(1) |

**用户 v1 已 AC 5（中心扩展），这次直接复用同套路，一次 AC。**

## 验证

- 对拍 **5000 组（ab 字母表 3000 + 全小写 2000）vs 暴力枚举 0 不一致**；
- 样例：`abc→3`、`aaa→6`、`ababa→9`。

## 复杂度

- 时间 **O(n²)**；空间 O(1)。