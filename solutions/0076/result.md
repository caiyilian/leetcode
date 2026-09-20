# 76. 最小覆盖子串 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 76. 最小覆盖子串（Minimum Window Substring）· **困难**（滑动窗口 + 哈希） |
| 链接 | https://leetcode.cn/problems/minimum-window-substring/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 268/268 用例通过**（leetgo 复提交） |
| 运行时间 | 123 ms |
| 内存 | 19.5 MB |

## 解法（用户滑动窗口 + 哈希，一次 AC）

```python
class Solution:
    def minWindow(self, s, t):
        need = {}      # t 中每个字符需要的次数
        windows = {}   # 窗口内每个字符的次数
        for c in t:
            need[c] = need.get(c, 0) + 1
            windows[c] = 0
        class_num = len(need)
        valid = 0      # 已达标字符种类数
        best = ''
        length = float('inf')
        left, right = 0, 0
        while right < len(s):
            if s[right] in need:                       # 扩张 right
                windows[s[right]] += 1
                if windows[s[right]] == need[s[right]]:
                    valid += 1
            if valid == class_num:                     # 全部达标
                if length > right - left + 1:
                    length = right - left + 1
                    best = s[left:right + 1]
                while True:                            # 收缩 left
                    left += 1
                    if s[left - 1] in need:
                        windows[s[left - 1]] -= 1
                        if windows[s[left - 1]] < need[s[left - 1]]:
                            valid -= 1                 # 窗口失效
                            if right == len(s) - 1:
                                return best
                            break
                    if length > right - left + 1:
                        length = right - left + 1
                        best = s[left:right + 1]
            right += 1
        return best
```

## 核心：滑窗 + 双哈希 + valid 计数

- `need`：t 的需求；`windows`：窗口的实时计数；
- `valid`：已达标的字符**种类数**（避免每次重新比较整个 need）；
- right 扩张 → 达标就收缩 left → 记录最短窗口。

## 验证

- 对拍 **2 万组随机串 vs 暴力枚举 0 不一致**；
- 样例：`ADOBECODEBANC/ABC→BANC`、`a/a→a`、`a/aa→""`。

## 复杂度

- 时间 **O(n)**；空间 O(字符集大小)。

## 🏆 HOT 100 全部 100 题通关（第 100 题）！