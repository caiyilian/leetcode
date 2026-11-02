# 494. 目标和 · 解析（二刷）

## 一、题目

- 中文：目标和
- English：Target Sum
- 难度：中等
- 问题：每个数前加 `+` 或 `-`，求凑出 target 的**方案数**

## 二、核心思路：记忆化递归（用户 AC 版）

**直接模拟题意**：每个数只有 `+nums[i]` 或 `-nums[i]` 两条路，天然是 DFS。加记忆化避免重复计算：

```
fun(i, target) = 用 nums[0..i]（前 i+1 个数）凑出剩余目标 target 的方案数
边界：i < 0 时，target == 0 算 1 种，否则 0 种
转移：fun(i, target) = fun(i-1, target-nums[i]) + fun(i-1, target+nums[i])
```

**为什么记忆化有用**：不同选择路径会到达相同的 `(i, target)` 状态（如 `[1,1]` 从 `-1+1` 和 `+1-1` 都到 0），缓存后指数→多项式。

## 三、代码

```python
mem = {}
def fun(i, target):
    if i < 0:
        return target == 0
    if (i, target) not in mem:
        mem[(i, target)] = fun(i-1, target-nums[i]) + fun(i-1, target+nums[i])
    return mem[(i, target)]
return fun(len(nums)-1, target)
```

## 四、⚡ 迭代法：关键是一步数学变形（面试加分）

递归直译好写，但面试官常追问迭代。**难点**：和的范围是 `-total ~ +total`，不能直接当下标。解法：

**数学变形**（设 P = 取正号的数集合）：
```
sum(P) - sum(其余) = target
sum(P) + sum(其余) = total
→ 2·sum(P) = target + total
→ sum(P) = (target + total) / 2
```

**降维打击**：问题变成"选一个子集，和恰好 = (target+total)/2"，每个数用一次 → **0-1 背包计数**——就是 416 分割等和子集的"计数版"（416 存 bool 可行性，这里存 int 方案数）：

```python
if (target + total) % 2 != 0 or (target + total) < 0:
    return 0                      # 三个前置约束
s = (target + total) // 2
dp = [0] * (s + 1)
dp[0] = 1
for x in nums:
    for j in range(s, x - 1, -1):   # ⚡ 倒序（0-1 背包，与 416 完全同款）
        dp[j] += dp[j - x]
return dp[s]
```

（另一条路：哈希表 DP `dp[cur] += 1` 直接模拟 ±，免变形但空间更散。）

## 五、复杂度

| 解法 | 时间 | 空间 |
|------|------|------|
| 记忆化递归 | O(n × 2total) | O(n × 2total)（dict，70MB 偏高）|
| 背包变形 | O(n × S)，S=(target+total)/2 | **O(S)**（~16MB，最优）|
| 哈希 DP | O(n × 状态数) | O(状态数) |

## 六、关联题目：背包家族再扩

| 题 | 类型 | 与本题关系 |
|----|------|-----------|
| **494 本题** | 0-1 背包·**计数** | 变形后 = 416 的计数版 |
| **416 分割等和子集**（⚡ 已做）| 0-1 背包·可行性 | 同一骨架：倒序 + dp[0]=1/True |
| **322 零钱兑换**（⚡ 已做）| 完全背包·最少 | 反例：正序（可无限用）|

**识别信号**："每个数加 ±/选与不选，求凑出某值的**方案数**" → 0-1 背包计数；若要"最少/最大" → 0-1 背包最值。

## 七、一句话记住

> **494 = ± 符号 → 集合划分：2·sum(P) = target+total，子集和 (target+total)/2 的 0-1 背包计数（416 计数版，dp[0]=1、倒序、返回 dp[S]）；三个前置约束：偶数、非负、S≤total。递归版直译 ± 两条路即可。**