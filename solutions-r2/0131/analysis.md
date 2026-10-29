# 131. 分割回文串 · 解析（二刷）

## 一、核心思路：切割回溯（start 的字符串用法）

**问题**：把 s 切成若干子串，每段都是回文，返回所有切法。

**关键**：这里不是"选/不选"，而是"**在哪切**"——`start` 表示当前起点，`i` 遍历所有可能的切割点：

```
s = "aab"（找所有回文切法）
                 ""
              start=0
            /    |    \
      切"a" ✓   "aa"✓  "aab"✗(非回文)
     /   |   \
 start=1        start=2
  "a"✓ "ab"✗    "b"✓
 start=2
  "b"✓
→ ["a","a","b"] 和 ["aa","b"]
```

**子串 `s[start:i+1]` 是回文才切**——这是唯一的约束条件。

## 二、代码（用户 AC 版）

```python
def isPa(s):          # 双指针判回文 O(n)
    p1, p2 = 0, len(s)-1
    while p1 < p2:
        if s[p1] != s[p2]: return False
        p1 += 1; p2 -= 1
    return True

def partition(self, s):
    result = []; length = len(s)
    def fun(path, start=0):
        if start >= length:
            result.append(path.copy())
            return path
        for i in range(start, length):
            if isPa(s[start:i+1]):           # 是回文才切
                path.append(s[start:i+1])
                path = fun(path, i+1)        # 从切点后继续
                path.pop()
        return path
    fun([])
    return result
```

**回溯三件套**照旧（append → 递归 → pop），只是"状态"从选元素变成"切一刀"。

## 三、复杂度

- 时间：O(n×2^n)——每个字符位置"切/不切"二选，最多 2^n 种切法，每种切法含 O(n) 的判回文/构造
- 空间：O(n)——递归栈 + path

## 四、优化（面试进阶）

**预计算回文 DP 表**（也是 516/647 回文子串篇的核心技巧）：
```python
dp = [[False]*n for _ in range(n)]           # dp[i][j]: s[i..j] 是否回文
for i in range(n-1, -1, -1):                 # 从下往上填
    for j in range(i, n):
        dp[i][j] = (s[i]==s[j]) and (j-i <= 2 or dp[i+1][j-1])
```
之后判回文 O(1)。131 用不用都行（n 小），但面试主动提这个能加分。

## 五、一刷 vs 二刷

- 一刷（9-16）：切割回溯 AC ×3；
- 二刷（10-29）：一次 AC——**39/78 的 start 模板迁移到字符串切割，直接写对**。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| 切割/子串回溯 | 131 本体、**93 复原 IP 地址**（定长 4 段切分） |
| 回文 DP | 5 最长回文子串、516 最长回文子序列、647 回文子串 |
| start 模板 | 39 组合、78 子集、77 组合（⚡ 同款"不回头"） |

**131 → 93 是顺路**：93 也是"切分字符串"，只是固定 4 段 + 每段合法 IP 段（前导 0/范围校验），模板完全一样。

## 七、一句话记住

> **分割回文串 = 切割回溯：start 起点 + i 枚举切点，子串回文才切；切完收集；⚡ 可加回文 DP 表把判回文降 O(1)（93 IP 同模板）。**