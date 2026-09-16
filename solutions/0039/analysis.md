# 39. 组合总和 · 解析

## 题目简述

`candidates`（元素互异，正数）中选若干个数（**可重复选同一个**），和等于 `target`。返回所有组合。

## 核心套路：可重复选择版回溯（index 锁 + 排序剪枝）

**与 46/78 的区别**：

| | 46 排列 | 78 子集 | 39 组合总和 |
|--|--------|--------|------------|
| 能否重复选 | 否 | 否 | **是** |
| 防重复组合 | `in path` | start 索引 | `fun(path, i)`（不传 i+1） |
| 剪枝 | 无 | 无 | **排序 + break** |

**"可重复选" = `fun(path, i)` 而不是 `fun(path, i+1)`**——同一位置可以再次选择；但**只用 i 及之后的**（`range(index, len)`）保证组合不重复（{2,2,3} 只出现一次，不会出现 {2,3,2}）。

## 定稿（用户 v3，追平标准版）

```python
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        length = len(candidates)
        candidates.sort()                       # ① 排序（剪枝的前提）
        def fun(path, index=0, now_sum=0):
            if now_sum > target:
                return
            if now_sum == target:
                result.append(path.copy())
            for i in range(index, length):      # ② 只往后走（防重复组合）
                n = candidates[i]
                if now_sum + n > target:
                    break                       # ③ 排序后后面更大 → break 剪枝
                path.append(n)
                fun(path, i, now_sum+n)         # ④ 可重复选 i（不传 i+1）
                path.pop()
        fun([])
        return result
```

## 演进史：v1 → v2 → v3（用户自驱，实测数据见 result.md）

### v1 的问题：节奏对，但三个浪费

```python
if sum(path) > target:        # ① 每次递归重算 sum —— O(深度)
for i, n in enumerate(candidates):
    if i < index: continue    # ② 全量枚举 + continue 跳过 —— 排序白排
# ③ 无 break —— 超过 target 的子树照样全走
```

### v2：`now_sum` 累加传参

`fun(path, i, now_sum+n)`——把"当前总和"变成参数，O(1) 累加替代 O(深度) 重算，快 1.6 倍。

### v3：排序 + range + break（组合拳）

```
for i in range(index, length):      # 不用 continue 跳了，范围天然限定
    if now_sum + n > target: break  # 排序后后面更大，全部超 → 终结整层
```

**为什么 break 不是 continue**：continue 是"跳过这个试下一个"，但排序后下一个更大，试了也白试；break 是"这个都不行后面更不行"，一次判断剪掉整层——**排序的唯一红利就在这里**。

## 复杂度

- 时间：O(答案数 × 深度)（剪枝显著缩小搜索空间；最坏 2^(target/min) 级别，但 break 剪枝让实际远小于）；
- 空间：O(深度)（递归栈 + path）。

## 考点

- **可重复选择的回溯**（`i` 不 `i+1`）
- **排序 + break 剪枝组合**（剪枝题型的标准动作）
- `now_sum` 传参 vs `sum()` 重算（性能习惯）

## 易错点

1. `fun(path, i)` 写成 `fun(path, i+1)`——漏掉"可重复选"，组合数量错误；
2. 排序后忘记 break（或写成 continue）——剪枝失效，大 target 超时；
3. 不排序直接 break——错解（"后面更大"不成立）；
4. `== target` 后**没 return** 会继续 for 循环（虽被 break 拦下，但多走一层）——v3 里其实可去掉基线 `now_sum > target`（break 已提前挡），保留无害；
5. `path.copy()` 别忘了（引用陷阱，46 同款）。

## 关联题

- **40 组合总和 II**（candidates 含重复：排序 + 同层相邻去重 `if i > index and candidates[i]==candidates[i-1]: continue`）；
- **77 组合**（不可重复：`fun(i+1)`）；
- 22 括号生成 / 79 单词搜索（剪枝型回溯的另两题）。