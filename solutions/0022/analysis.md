# 22. 括号生成 · 解析

## 题目简述

`n` 对括号，生成所有**合法**组合（任意前缀中右括号不多于左括号）。

## 核心套路一：回溯 + 双条件剪枝（用户定稿）

**与 46/78/17/39 的不同**：那些题"从集合里选元素"，这题"从两个符号 `(` `)` 里选 + 合法性剪枝"。

```python
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def fun(path, left, right):
            if len(path) == 2*n:
                result.append("".join(path))
                return
            if left < n:            # ① 左括号数没满才能放 (
                path.append("(")
                fun(path, left+1, right)
                path.pop()
            if left > right:        # ② 还有未匹配的左括号才能放 )
                path.append(")")
                fun(path, left, right+1)
                path.pop()
        fun([], 0, 0)
        return result
```

**两个条件的本质**：

```
① left < n    —— 左括号最多 n 个（总量限制）
② left > right —— 任意前缀右括号不能反超左括号（合法性核心）
```

条件②就是"合法括号串"的定义翻译：`()` 合法、`())` 非法（前缀 `())` 里右括号 2 > 左括号 1）。**`left > right` 即用户 docstring 说的"左括号还有至少 1 个没匹配"**。

## 核心套路二：DP（力扣"动态规划"标签的解）

**洞察**：合法串首字符必为 `(`，它和某个 `)` 配对，切成三块：

```
合法串 = "(" + a + ")" + b      （a = 内部合法串，b = 尾部合法串）
```

递推：`dp[i] = ∪_{j=0}^{i-1} { "(" + a + ")" + b | a∈dp[j], b∈dp[i-1-j] }`

```python
class Solution:
    def generateParenthesis(self, n):
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                for a in dp[j]:
                    for b in dp[i - 1 - j]:
                        dp[i].append("(" + a + ")" + b)
        return dp[n]
```

**注意**：这里的 DP **不是降复杂度型 DP**（结果本身就是卡特兰数指数级）——它和回溯复杂度相同（O(Cₙ×n)），只是换了枚举方式（构造即合法、无需剪枝）。面试被问"还有别的做法吗"时它是标准备选。

## 复杂度（卡特兰数）

- 答案数 = **卡特兰数** `Cₙ = C(2n,n)/(n+1)`：n=2→2、n=3→5、n=4→14、n=5→42、n=6→132、n=7→429；
- 时间 **O(Cₙ×n)**（生成每个答案 O(n)）；回溯空间 **O(n)**，DP 空间 **O(Cₙ×n)**；
- **剪枝的威力**：2²ⁿ 全枚举 → 剪枝后只剩合法前缀 ≈ Cₙ（n=4：256 → 14）。

## 考点

- 回溯的"合法性剪枝"（前缀约束）
- **卡特兰数**（括号/二叉树/出栈序列等计数问题共用的数）
- 同一问题的"按位置"（回溯）vs "按配对"（DP）双视角

## 易错点

1. 条件②写成 `right < n`——错！`(((` 之后右括号 3 < n 也能放？不——`left > right` 才是合法条件；
2. `len(path) == 2n` 后**忘 return**——本版不 return 也正确（此时 left=right=n，两个条件自然 False），但 return 更清晰；
3. join 成字符串（不要存字符列表）；
4. DP 的 `dp[0] = [""]`（空串是唯一 0 对解）漏了会全崩。

## 关联题

- 20 有效的括号（判断版：栈）；
- **32 最长有效括号**（困难，栈/DP）；
- 卡特兰数兄弟：95 不同的二叉搜索树 II、96 不同的二叉搜索树（Catalan 计数）。