# 75. 颜色分类 · 解析（二刷）

## 一、题目

- 中文：颜色分类
- English：Sort Colors（荷兰国旗问题 Dutch National Flag）
- 难度：中等
- 要求：只含 0/1/2 的数组原地排序；**进阶 = 一趟扫描 + 常数空间**

## 二、核心思路：荷兰国旗三指针

**为什么朴素方法不满足进阶**：计数重填 = 两趟；排序 = O(n log n)。进阶要**单遍 + 原地**——三种值需要三根指针管理三个区。

**三区不变量**（这题的灵魂）：
```
[0, left)     全 0     （0 区，已归位）
[left, i)     全 1     （1 区，已扫描）
[i, right]    未扫描
(right, n-1]  全 2     （2 区，已归位）
```

**扫描规则**：
| nums[i] | 动作 | 为什么 |
|---------|------|--------|
| 0 | 与 nums[left] 换，`left++`、`i++` | 换过来的是 1（或自己），已完成检查，可前进 |
| 1 | 只 `i++` | 本来就在 1 区位置 |
| 2 | 与 nums[right] 换，`right--`、**i 不动** | ⚡ 换过来的数**未检查**（可能是 0），必须再审视 |

**完成条件 `while i <= right`**：2 区从尾部构建、已是终态，i 扫进去纯浪费——i 越过 right 即结束。

## 三、代码（用户 AC 版 + 两个微优化）

```python
zero_bound = 0
two_bound = length - 1
while zero_bound < length and nums[zero_bound] == 0:   # ⚡ 优化① 跳过首部连续 0
    zero_bound += 1
while two_bound >= 0 and nums[two_bound] == 2:          # ⚡ 优化① 跳过尾部连续 2
    two_bound -= 1
i = zero_bound
while i <= two_bound:
    if nums[i] == 1:
        i += 1; continue
    if nums[i] == 2:
        nums[i], nums[two_bound] = nums[two_bound], nums[i]
        two_bound -= 1
        while nums[two_bound] == 2:                     # ⚡ 优化② 换完立即跳过连续 2
            two_bound -= 1
        continue
    if nums[i] == 0:
        nums[i], nums[zero_bound] = nums[zero_bound], nums[i]
        zero_bound += 1; i += 1
```

- **优化① 预处理**：循环前先跳过首部 0 / 尾部 2，减少主循环次数；
- **优化② 换 2 后 while 跳 2**：把标准版"下轮再查"提前，等价但少几轮；
- 两者均不改复杂度（仍是 O(n)/O(1)），属于常数优化。

## 四、⚡ 隐患确认（用户代码的安全性）

`while nums[two_bound] == 2: two_bound -= 1` 有 `two_bound` 减到 -1 时 Python 负索引访问 `nums[-1]` 的潜在风险。安全靠两条**不变量**：
1. 预处理已保证主循环开始时 `nums[two_bound] != 2`；
2. 2 分支只可能在 `i < two_bound` 时触发（`i == two_bound` 时该位必非 2，不会进 `nums[i]==2` 分支）——所以每次跳过 2 后，`two_bound` 停在的位置要么 ≥ i（合法），要么 < i（立即退出外层 while），**永远到不了 -1**。

**能把这两条不变量想清楚，就是这题真正吃透的标志。**

## 五、复杂度

- 时间：O(n)（单遍扫描，每个元素至多被交换 1 次）
- 空间：O(1)

## 六、关联题目

| 题 | 关系 |
|----|------|
| **75 本题** | 三指针分区——荷兰国旗原型 |
| **283 移动零**（⚡ 已做）| 双指针分两区（0 与 非 0）——三指针退化版 |
| **215 第 K 大**（⚡ 已做）| 快选 partition 也是"换 + 指针不动"思想 |

**识别信号**："只有几种固定值 + 原地排序 + 进阶单遍" → 三指针分区；两值 → 双指针（283）。

## 七、一句话记住

> **75 = 荷兰国旗三指针：left 管 0、right 管 2、i 扫描；0 换左双前进、2 换右 i 不动（换来的没检查）、1 只前进；while i<=right；两条不变量保证 two_bound 不越界。**