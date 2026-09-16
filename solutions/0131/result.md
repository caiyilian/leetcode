# 131. 分割回文串 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 131. 分割回文串（Palindrome Partitioning）· 中等（回溯家族第 7 题） |
| 链接 | https://leetcode.cn/problems/palindrome-partitioning/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 32/32 用例通过** |
| 运行时间 | 79 ms（击败 5%，Python 常规范围；本地 1 万组对拍秒级） |
| 内存 | 33.6 MB |

## 解法（用户独立完成：切割点回溯 + 双指针回文判断）

```python
def is_palindrome(s):
    p1, p2 = 0, len(s) - 1
    while p2 >= p1:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True

class Solution:
    def partition(self, s):
        length = len(s)
        result = []
        def fun(path, index):
            if index == length:          # 切完整个字符串 → 记录
                result.append(path.copy())
                return
            for i in range(index + 1, length + 1):   # 穷举切割终点
                if is_palindrome(s[index:i]):        # 这段是回文才切
                    path.append(s[index:i])
                    fun(path, i)                     # 从切割点继续
                    path.pop()
        fun([], 0)
        return result
```

**用户独立完成**（回溯家族 7 连第 7 题），且**正确用上了 79 题教训**：基线 `index == length` 按"目标进度"声明（切完整个串），不靠副作用。

## 验证

- 对拍 **1 万组随机串（aab 字母集）vs 独立参照 0 不一致**；
- 官方样例：`"aab" → [["a","a","b"],["aa","b"]]`、`"a" → [["a"]]`；
- 补充：`"abac" → [["a","b","a","c"],["aba","c"]]`。

## 复杂度

- 时间 **O(n·2ⁿ)**（2ⁿ⁻¹ 种分割 × 回文判断 O(n)；可预计算回文表优化，n ≤ 16 不需要）；
- 空间 **O(n)** 递归深度。

## 优化位（面试可提）

- **回文预计算表** `dp[i][j]`（区间是否回文，O(n²) 预处理 → 判断 O(1)）——长串或多次查询时受益；
- 本题力扣 n ≤ 16，直接双指针判断已足够。