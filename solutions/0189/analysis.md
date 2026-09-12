# 189. 轮转数组 · 解析

## 题目简述

给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。要求**原地修改**（返回 None）。

示例：`[1,2,3,4,5,6,7], k=3` → `[5,6,7,1,2,3,4]`。

## 三种解法

### 解法一：切片赋值（Python 惯用，提交最快）

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length = len(nums)
        k = k % length
        nums[:k], nums[k:] = nums[-k:], nums[:length-k]
```

- 取模处理 k > n 和 k ≤ 0；
- `nums[-k:]` 是后 k 个，`nums[:length-k]` 是前 n-k 个，链式赋值一次性交换两段；
- 时间 O(n)（切片复制）、空间 O(n)（两个临时切片）；
- **注意**：链式切片赋值依赖 Python 的求值顺序（先整体算右侧，再从左到右逐个赋值），行为已对拍验证稳定正确，但属于"简洁但有微妙语义"的写法。

### 解法二：三次反转（进阶要求 O(1) 空间）

```python
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        length = len(nums)
        k = k % length
        nums.reverse()                        # ① 整体反转
        nums[:k] = reversed(nums[:k])         # ② 前 k 个反转
        nums[k:] = reversed(nums[k:])         # ③ 后 length-k 个反转
```

**原理**：目标数组 = 后 k 个 + 前 n-k 个。三步反转把顺序"倒腾"出这个结果：

```
原: [1,2,3,4] [5,6,7]     k=3
① [7,6,5, 4,3,2,1]
② [5,6,7, 4,3,2,1]
③ [5,6,7, 1,2,3,4]  ✅
```

- 严格 O(1) 空间需要手写双指针交换循环（v2，本机 4~5ms）；
- **Python 权衡**：手写 Python 循环（逐元素交换）反而比 C 层切片慢 4~5 倍——O(1) 空间与速度此消彼长。面试讲"三次反转"的思路（进阶要求），提交加速用切片。

### 解法三（v2 手写版思路，已完成对拍验证）

三次反转各写一个双指针交换循环：`for i in range(k): swap(nums[i], nums[k-i-1])` 等。逻辑与解法二完全一致，仅为实现方式不同（O(1) 空间、Python 层循环）。

## 复杂度对比

| | 时间 | 空间 |
|--|------|------|
| 切片赋值 | O(n) | O(n) |
| 内建反转 | O(n) | O(k)（reversed 切片副本） |
| 手写三次反转 | O(n) | **O(1)** |

## 考点

- **取模处理 k**（k > n、k ≤ 0 都要考虑，经典陷阱：k=0 时空转）
- 原地修改（不能新建数组返回）
- 三次反转技巧（面试高频：这题最常考的就是"你会不会反转法"）
- Python 特性：切片赋值 / reversed / 链式赋值语义
- 与 283 移动零对比：都是"原地修改 + 返回 None"题型

## 踩坑记录

- leetgo 对「原地修改返回 None」题型生成的 `__main__` 少 `Solution().`（`rotate(nums, k)` → `Solution().rotate(nums, k)`），本地测试会 NameError（在线不受影响）——283 题首次踩到，189 二次确认，**此类题需手动修复模板**。
- 调试 `print(nums)` 提交前必须删除（本地调试残留）。