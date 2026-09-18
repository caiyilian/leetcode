# 45. 跳跃游戏 II · 解析

## 题目简述

求从起点到终点（保证可达）的**最少跳跃次数**。`[2,3,1,1,4]` → 2（0→1→4）。

## 核心套路：双 far 贪心（段计数）

**从 55 升级**：55 问"能不能到"（一个 far），45 问"最少几步"——**步数 = 段数**，必须引入"段"的概念：

```
curr_far = 当前这一跳能覆盖的最远边界（段尽头）
next_far = 下一跳能到的最远（在 curr_far 范围内试探）

遍历 i：
  next_far = max(next_far, i + nums[i])   # 试探：这段里能跳到最远哪
  if i == curr_far:                        # 走到段尽头
      step += 1                            # 必须再跳一次
      curr_far = next_far                  # 下一段的范围
```

```python
class Solution:
    def jump(self, nums):
        curr_far = next_far = step = 0
        length = len(nums)
        for i, n in enumerate(nums):
            next_far = max(next_far, n + i)
            if i == curr_far and i != length - 1:   # 段尽头（且没到终点）
                step += 1
                curr_far = next_far
        return step
```

## 为什么"far 更新次数 ≠ 跳数"（用户疑问）

far 在**同一跳覆盖范围内**会连续更新（多次试探），更新次数混进了"同一跳内的反复试探"。跳数 = "段数" = `i == curr_far` 触发的次数。反例 `[2,3,1,1,4]`：far 更新 3 次，跳数 = 2。

## 手推 [2,3,1,1,4]（感受"段"）

```
cur_end=0, next_far=0, step=0
i=0: next_far=max(0,2)=2; i==cur_end → step=1, cur_end=2   ← 第1跳覆盖[1,2]
i=1: next_far=max(2,4)=4; i(1)!=cur_end(2)
i=2: next_far=max(4,3)=4; i==cur_end(2) → step=2, cur_end=4 ← 第2跳覆盖[3,4]
i=3: next_far=max(4,4)=4; i(3)!=cur_end(4)
i=4: 终点，i==length-1 跳过
答案 = 2 ✅
```

## 与 55 的关系（一句话）

```
55：一个 far → 问"能不能到"（bool）
45：两个 far → 问"最少几步"（要分段数）
```

**"最少"必然引入段**——这是从"可行性"到"最优性"的贪心升级。

## 复杂度

- 时间 **O(n)**（理论下界：每个位置至少看一次）；空间 **O(1)**。

## 考点

- 双 far 贪心（段计数）
- 从"可行性"到"最优性"的升级（55 → 45）
- `i == cur_end` 段边界触发

## 易错点

1. 终点再跳一次（需 `i != length-1` 或 `range(n-1)`）；
2. 用 far 更新次数当跳数（用户疑问，错）；
3. `curr_far = next_far` 忘更新（cur_end 卡死 → 死循环/多算）；
4. `next_far` 更新位置错（应在段内每个 i 都试探，不能只在段尽头）。

## 关联题

- **55 跳跃游戏**（一个 far 版）/ **121**（同骨架：全局最优 + 一次扫描）；
- **763 划分字母区间**（贪心维护最远出现位置，同"最远可达"思想）；
- 贪心分类全家桶：121、55、45、763。