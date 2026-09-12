# 238. 除自身以外数组的乘积 · 解析

## 题目简述

给你一个整数数组 `nums`，返回数组 `answer`，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积。**不能使用除法**，进阶要求 **O(1) 额外空间**。

示例：`[1,2,3,4]` → `[24,12,8,6]`。

## 核心套路：前缀积 × 后缀积（与 560 前缀和同源）

位置 i 的答案 = i 左边所有数的乘积 × i 右边所有数的乘积：

```
answer[i] = (nums[0] × ... × nums[i-1]) × (nums[i+1] × ... × nums[n-1])
```

- **前缀积**：`left[i] = nums[0..i-1]` 的乘积，从左往右累乘；
- **后缀积**：`right[i] = nums[i+1..n-1]` 的乘积，从右往左累乘。

**不能使用除法**的原因：`nums` 含 0，直接用"总乘积 / nums[i]"会在 0 处崩（×0/0）。

## 定稿解法（单数组复用，O(1) 额外空间）

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_reverse = [1] + [0] * (length)
        for i in range(length):
            if nums[length-i-1] == 0:
                break
            prefix_reverse[i+1] = prefix_reverse[i] * nums[length-i-1]
        prefix = nums[0]
        for i in range(1, length):
            prefix_reverse[length-i-1] = prefix * prefix_reverse[length-i-1]
            prefix *= nums[i]
        prefix_reverse.reverse()
        return prefix_reverse[1:]
```

### 算法逻辑（用户的单数组复用技巧）

`prefix_reverse` 数组全程只有一个，分三阶段：

1. **第一阶段（从右往左）**：`prefix_reverse[k]` 先存"从右往左 k 个数的后缀积"（`nums[n-1]×...×nums[n-k]`）；
2. **第二阶段（从左往右）**：滚动变量 `prefix` 累积"左边乘积"，**就地乘进数组**：`prefix_reverse[n-i-1] = prefix × prefix_reverse[n-i-1]`——此时每个槽位变成"左边积 × 右边积"= 最终答案（只是顺序是反的）；
3. **反转 + 切片**：`reverse()` 后 `[1:]` 取到从左往右的正确顺序。

**为什么这是 O(1) 额外空间**：输出数组本身不算额外空间，`prefix_reverse` 就是返回的答案；额外的只有滚动变量 `prefix` 和循环变量。

### 遇 0 剪枝（数学安全）

```python
if nums[length-i-1] == 0: break    # 后缀积碰到 0 就停
```

一旦某侧累积乘积为 0（说明那边存在 0），所有剩余位置的答案必然含那个 0 → 结果必为 0，提前结束不丢正确性。4 万组含 0/无 0 对拍 + 手工边界验证通过。

### 复杂度

- 时间 **O(n)**：两遍扫描 + 一次反转；
- 空间 **O(1) 额外** ✅（输出数组除外）。

## 演进中的关键决策

| 版本变化 | 学到的点 |
|---------|---------|
| v1 暴力 O(n²) | 每个位置独立乘一遍是重复劳动 |
| v2 dict 存前缀积 | dict 的键是连续下标 → 应该用 list（速度 +55%） |
| v3 list + 0 剪枝 | list 后速度快；0 剪枝数学安全 |
| v4 单数组复用 | **输出数组本身就是"额外空间"的合法内存**，复用它达到 O(1) |

**核心洞察**：所谓"O(1) 额外空间"，指的是**除了必须返回的输出数组外**不能再开数组——所以答案数组在计算过程中可以随便用，这是这类题通用的内存技巧。

## 考点

- 前缀积 / 后缀积（560 前缀和的乘法版）
- **不能用除法**（0 的陷阱：`[0,1]`、`[0,0]` 都会让除法方案崩）
- O(1) 额外空间的边界定义（输出数组不算额外）
- 单元素边界：除自身 = 空乘积 = 1（`[5]→[1]`，`[0]→[1]`）
- 遇 0 剪枝的正确性论证

## 顺带提醒

- 基准测试教训：用随机 1~10 生成 n=10⁵ 数据时，10⁵ 次乘法产生 10⁵ 位的巨型整数，prefix 数组内存爆炸（进程被 OOM 杀掉）——**基准数据要贴近真实场景（±1 等），不能只看规模**。
- Python 3.11+ 大整数转字符串有 4300 位限制（`sys.set_int_max_str_digits`），调试打印巨整数会报 ValueError。