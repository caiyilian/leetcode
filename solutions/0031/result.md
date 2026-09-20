# 31. 下一个排列 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 31. 下一个排列（Next Permutation）· 中等（原地重排） |
| 链接 | https://leetcode.cn/problems/next-permutation/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 268/268 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.2 MB |

## ⚠️ 失败记录（一次，用户主动标注）

| 提交 | 结果 | 根因 |
|------|------|------|
| 750403365 | **WA** | `if nums[j] < nums[index]`（少了等于） |
| 750404152 | AC | `if nums[j] <= nums[index]`（必须有 =） |

**为什么必须有 `=`**：右边（index+1 到末尾）是**降序**，要找"最小的大于 nums[index] 的数"= 第一个 `nums[j] <= nums[index]` 的**前一个位置 j-1**。右边含相等元素时，`<` 会跳过它导致交换错位：

```
反例 [1,2,1]（正确下一个是 [2,1,1]）：
  <  ：j=2 时 nums[2]=1 < 1? 否 → else 交换错位 → [1,1,2] ❌
  <= ：j=2 时 nums[2]=1 <= 1? 是 → j-1=1 交换 nums[0]↔nums[1] → [2,1,1] ✅
```

## 解法（用户标准算法）

```python
def nextPermutation(self, nums):
    length = len(nums)
    for i in range(length):
        index = length - 1 - i
        if index < length - 1 and nums[index] < nums[index+1]:   # 从右找升序对
            for j in range(index+1, length):
                if nums[j] <= nums[index]:                        # ★ 必须 <=
                    nums[index], nums[j-1] = nums[j-1], nums[index]
                    break
            else:
                nums[index], nums[length-1] = nums[length-1], nums[index]
            break
    else:
        index = -1    # 完全降序
    left, right = index+1, length-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1; right -= 1
```

## 算法三步

1. **从右往左**找第一个升序对 `nums[index] < nums[index+1]`（index 是"要变的位置"）；
2. 在右边（降序）找**最小的大于 nums[index] 的数**，与 nums[index] 交换；
3. **反转** index+1 到末尾（原来降序 → 变升序，得到最小的更大排列）。

完全降序时 index=-1，反转整个数组回到最小排列。

## 验证

- 对拍 **2 万组随机数组 vs itertools 全排列 0 不一致**；
- 样例：`[1,2,3]→[1,3,2]`、`[3,2,1]→[1,2,3]`、`[1,1,5]→[1,5,1]`。

## 复杂度

- 时间 **O(n)**；空间 O(1)。