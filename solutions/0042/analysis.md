# 42. 接雨水 · 解析

## 题目简述

给定 `n` 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

## 核心公式（局部视角）

第 `i` 个位置能接的水：

```
water[i] = max(0, min(左侧最高, 右侧最高) - height[i])
```

**原因**：水是平的，左右两堵"墙"中较矮的那堵决定水位上限；低于柱顶的高度存不住水。

总和 = Σ water[i]。首尾两格必然存不住水（至少一侧没有墙）。

## 定稿解法：双指针（用户自创变体）

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        water_count = 0
        max_left = 0
        max_right = 0
        i, j = 1, length - 2
        while i <= j:
            max_left = max(max_left, height[i-1])
            max_right = max(max_right, height[j + 1])
            if i == j:
                water_count += max(0, min(max_left, max_right) - height[i])
                break
            if max_left < max_right:
                water_count += max(0, max_left - height[i])
                i += 1
            elif max_right < max_left:
                water_count += max(0, max_right - height[j])
                j -= 1
            else:
                water_count += max(0, max_left - height[i]) + max(0, max_right - height[j])
                i += 1
                j -= 1
        return water_count
```

### 算法逻辑

- `max_left` / `max_right`：当前指针外侧已见过的最高柱（不含自身）；
- 每轮先扩展两侧 max（`height[i-1]` / `height[j+1]`），再决定结算：
  - **`max_left < max_right`**：i 位置的右侧最高必然 ≥ `max_right` > `max_left`，所以 i 的水位被 `max_left` 锁死，可直接结算 i，然后 `i += 1`（j 原地等待）；
  - **`max_right < max_left`**：对称地结算 j，`j -= 1`；
  - **相等**：两侧都可结算，同时推进；
  - **`i == j` 相遇**：此刻 `max_left` 恰好覆盖 `h[0..i-1]`、`max_right` 恰好覆盖 `h[i+1..n-1]`，`min(max_left, max_right) - height[i]` 是精确值，结算后结束。

### 复杂度

- 时间 **O(n)**：每个内部位置至多被结算一次，指针总移动 O(n) 步；
- 空间 **O(1)**：只有两个指针 + 两个变量，无数组。

## 与标准双指针写法的关系

| | 标准写法 | 用户变体 |
|--|---------|---------|
| 比较对象 | `height[l]` vs `height[r]`（柱子本身） | `max_left` vs `max_right`（两侧已见最高） |
| 指针起点 | 两端 `l=0, r=n-1` | 内部 `i=1, j=n-2` |
| 收口方式 | `while l < r`（柱子本身参与比较，每根柱子自然被轮到） | `while i <= j` + 相遇分支精确结算 |

两者逻辑等价。用户变体的关键洞察：**比较"已见最高"而不是"柱子本身"时，矮侧的水位已被对侧更高的柱子锁死**——这是"移动矮侧"这一双指针灵魂的另一种表述。

## 踩坑记录（5 版演进的教训）

### 1. 暴力扫描（v1）→ 超时
每个位置都 `max(height[:i])` + `max(height[i+1:])`，O(n²)。单调递减数据（力扣隐藏用例）直接超时。**教训：别怕排序/预计算，怕的是每步都重复做全量工作。**

### 2. 预计算数组（v2/v3）→ 正确但常数大
左右最大值各预计算一遍数组（O(n) 空间），再扫一遍累计。23ms / 击败 9%。**教训：O(n) 且正确，但数组分配和三次遍历让常数变大；力扣该题 Python 提交普遍是 O(n)，击败率挤在常数上。**

### 3. 单循环"伪双指针"（v4）→ 常数反而变大
试图一个循环从两端同时向中间走，两个指针**每轮都必须走**——结果必须用两个累积数组记录两侧最高，索引计算复杂（奇偶分支），实测比 v2 还慢 15%。**教训：让两个指针"同步收缩"本质还是模拟，绕不开数组。**

### 4. 真双指针（v5）→ 正确 + 快
悟到关键：**双指针不需要每轮都同时走**。哪侧矮哪侧结算并移动，另一侧原地等待——这样每侧只需一个变量记录"已见最高"，无需数组。11ms / 击败 61.58%。

## 三个 bug 的修复细节（v4 → v5）

1. `while i < j` → `while i <= j`：相遇位置必须进循环；
2. 相遇分支必须放在**更新 max 之后**：此时 max_left/max_right 覆盖范围恰好完整（`h[0..i-1]` / `h[i+1..n-1]`），`min` 结算精确——放前面就缺一格；
3. else 分支 `height[length - i]` → `height[j]`：原写法结算了错误的柱子（`length-i` 只是镜像索引，与 j 无关）。

## 考点

- 双指针（移动矮侧：矮侧水位已被对侧锁死）
- 每位置蓄水量的局部公式（min(两侧最高) - 自身）
- 正确性证明习惯：结算矮侧 = "该侧所有剩余组合已被证明不可能更优"
- 与 11 题（盛水容器）对比：11 题算的是两柱之间的矩形面积（宽度参与）；本题算的是每个凹槽位置的水量（min 两侧最高 - 自身）。两题都是"移动矮侧"，但结算对象不同。
