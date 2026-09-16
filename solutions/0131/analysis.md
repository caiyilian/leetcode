# 131. 分割回文串 · 解析

## 题目简述

给定字符串 `s`，分割成若干子串使每段都是回文，返回所有分割方案。

## 核心套路：切割点回溯

**与"选元素"回溯的区别**：46/78/17/39 每层从一个集合里选元素；131 **每层决定"从 index 切多长一段"**——`index` 是当前切割起点，穷举终点 `i`，回文段切进去，从 `i` 继续。

```python
class Solution:
    def partition(self, s):
        length = len(s)
        result = []
        def fun(path, index):
            if index == length:          # 切完整个字符串 → 记录
                result.append(path.copy())
                return
            for i in range(index + 1, length + 1):   # 穷举切割终点（至少 1 字符）
                if is_palindrome(s[index:i]):        # 回文段才切
                    path.append(s[index:i])
                    fun(path, i)                     # 从切割点继续切
                    path.pop()
        fun([], 0)
        return result

def is_palindrome(s):        # 双指针回文判断（用户独立写出）
    p1, p2 = 0, len(s) - 1
    while p2 >= p1:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True
```

## 回溯家族的"五种锁"凑齐（46 → 131 完整对照）

| 题 | "这层能选谁" | 锁/剪枝 |
|----|------------|---------|
| 46 全排列 | 没用过的数字 | `in path` |
| 78 子集 | start 及以后的元素 | `range(start, n)` 下标锁 |
| 17 字母组合 | 当前数字的字母表 | index 固定表 |
| 39 组合总和 | 可重复选 + 排序 | `fun(i)` + break 剪枝 |
| **131 分割回文串** | **从 index 切任意长度** | **is_palindrome 才能切** |

**用户已全部独立完成——模板内化的实证**。

## 三个细节（为什么这么写）

1. **`range(index+1, length+1)` 的边界**：切割终点 `i` 至少 `index+1`（切 1 个字符）至多 `length`（切到串尾）——`s[index:i]` 左闭右开，`i == length` 正好包含最后一个字符；
2. **基线 `index == length`**：切完整个串 → 是完整方案。**79 题教训的正确应用**——基线按"目标进度"声明（切完），不靠副作用；
3. **`path.copy()`**：引用陷阱（46 题同款）——path 是共享列表，不复制会被后续 pop 改空。

## 优化位：回文预计算表（面试可提）

```python
# O(n²) 预处理：is_pal[i][j] = s[i:j+1] 是否回文
dp = [[False]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = True
for L in range(2, n+1):
    for i in range(n-L+1):
        j = i+L-1
        dp[i][j] = (s[i] == s[j]) and (L == 2 or dp[i+1][j-1])
```

→ 回溯里判断变成 `if dp[index][i-1]`，O(1) 查询。本题 n ≤ 16 用不上，但长字符串场景受益。

## 复杂度

- 时间 **O(n·2ⁿ)**（2ⁿ⁻¹ 种分割方案 × 回文判断 O(n)；预计算后可 O(2ⁿ) 不含判断）；
- 空间 **O(n)** 递归深度（+预计算表 O(n²) 可选）。

## 考点

- 切割点回溯（回溯策论的"分割"变体）
- 回文判断（双指针 or DP 表）
- 基线按目标进度声明
- 与 46/78/17/39 的选择机制对比

## 易错点

1. `range(index+1, length+1)` 写成 `range(index, length)`——空串段 `s[index:index]` 永远回文 → 死循环/重复；
2. 基线漏 `return`——index==length 后还会进 for 循环（`s[length:...]` 空串）→ 但空串 is_palindrome=True → 无限递归！**131 的 return 必须有**（和 22 不同）;
3. `path.copy()` 忘复制；
4. is_palindrome 里 `p2 >= p1` 边界（奇偶长度都要覆盖）；
5. 误以为"从任意位置切"——必须从 index 连续切（切出的段要覆盖整个串）。

## 关联题

- **51 N皇后**（回溯收官题，判断条件换成冲突检查）；
- 132 分割回文串 II（动态规划，最小切割次数）；
- 647 回文子串（计数版）。