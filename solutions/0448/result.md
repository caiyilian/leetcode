# 448. 找到所有数组中消失的数字 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 448. 找到所有数组中消失的数字（Find All Numbers Disappeared in an Array）· 简单（v2 新增题 · 归位法） |
| 链接 | https://leetcode.cn/problems/find-all-numbers-disappeared-in-an-array/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-25 |
| 最终提交 | ✅ **ACCEPTED - 35/35 用例通过**（leetgo 复提交） |
| 运行时间 | 51 ms |
| 内存 | 30.4 MB |

## 解法（用户归位法，数组即哈希）

```python
class Solution:
    def findDisappearedNumbers(self, nums):
        length = len(nums)
        for i in range(length):
            while nums[i] != (i + 1):
                if nums[i] == nums[nums[i] - 1]:
                    break                     # 目标位置已是正确值 → 重复
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]   # 交换归位
        result = []
        for i in range(length):
            if nums[i] != (i + 1):
                result.append(i + 1)          # 错位的下标 i → 缺失 i+1
        return result
```

## 符合题目进阶要求 ✅

| 要求 | 达标 |
|------|------|
| 时间 O(n) | ✅ 每个元素最多交换一次，总 O(n) |
| 空间 O(1)（不计返回数组） | ✅ 只用两个变量 + 原地交换 |
| 允许修改数组 | ✅ 题目允许（与 41/442 同款） |

## 核心：归位法（数组当哈希）

```
值 v 应该出现在下标 v-1（值域 1..n 恰对应下标 0..n-1）
while nums[i] != i+1：把 nums[i] 换到它该在的位置
  若目标位置已是对的值 → 重复元素，break（跳过）
最后扫描：nums[i] != i+1 的位置，i+1 就是消失的数字
```

## 与 41 缺失的第一个正数的血缘（同款归位法）

```
41：同样归位法，找"第一个"错位
448：同样归位法，找"所有"错位
```

用户 9-20 已 AC 41，这次直接复用归位思想。

## 验证

- 对拍 **5 万组随机数组 vs set 差值 0 不一致**；
- 样例：`[4,3,2,7,8,2,3,1]→[5,6]`、`[1,1]→[2]`。

## 复杂度

- 时间 **O(n)**；空间 O(1)。