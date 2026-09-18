# 215. 数组中的第 K 个最大元素 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 215. 数组中的第 K 个最大元素（Kth Largest Element in an Array）· 中等（堆分类第 1 题） |
| 链接 | https://leetcode.cn/problems/kth-largest-element-in-an-array/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 47/47 用例通过**（leetgo 复提交） |
| 运行时间 | 42 ms（击败 95%） |
| 内存 | 30.7 MB |

## 三解法（用户 4 次提交全覆盖）

| 方案 | 力扣提交 | 复杂度 | 适用 |
|------|---------|--------|------|
| **快速选择（三路分区）** | 749937509 / 749951232 | **O(n) 平均** | 进阶要求 / 面试加分 |
| **堆（heapq 最小堆）** | 749948206 | O(n log k) | 工程简洁 / 稳妥答法 |
| **手写堆（shift_up/down）** | 749954422 | O(n log k) | 理解堆机制的里程碑 |

### 快速选择版（用户自写，solution.py）

```python
def findKthLargest(self, nums, k):
    from random import choice
    def fast_choose(nums, k):
        pivot = choice(nums)              # 随机化防退化
        left, middle, right = [], [], []  # > / == / < pivot 三路
        for n in nums:
            if n > pivot: left.append(n)
            elif n < pivot: right.append(n)
            else: middle.append(n)
        if len(left) >= k:
            return fast_choose(left, k)
        elif len(left) + len(middle) >= k:
            return pivot
        else:
            return fast_choose(right, k - len(left) - len(middle))
    return fast_choose(nums, k)
```

### 堆版（solution_readable.py）

```python
def findKthLargest(self, nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]
```

## 手写堆踩坑 → 攻克记录（用户理解堆的完整路径）

1. **中途卡点**：`arr.pop()` 弹**末尾**（应为弹堆顶 = 末尾搬顶 + 下沉）、`shift_up` 传参用外层 i 而非 `len(arr)-1`、负值策略与"维护 k 个"摇摆；
2. **理解突破**：确认"堆顶一定最小，但堆数组 ≠ 排序"（堆只约束父子，不约束兄弟/全局）；
3. **攻克（749954422）**：完整手写 `shift_up`（插入上浮）+ `shift_down`（替换堆顶下沉），且正确用"`arr[0]=n` + shift_down"实现"替换堆顶"——正是之前卡住的操作。

**关键认知：替换堆顶 = 直接覆盖 arr[0] + 下沉**（不需要真删，覆盖后调整即可），比"删顶三步"更简洁。

## 验证

- 官方样例：`[3,2,1,5,6,4]` k=2 → 5、`[3,2,3,1,2,4,5,5,6]` k=4 → 4；
- 两版均为 47/47 Accepted。

## 复杂度

- 快速选择 **O(n) 平均**（随机 pivot；最坏 O(n²) 被随机化摊掉）；空间 O(n) 递归（三路分区的额外数组）；
- 堆 **O(n log k)**；空间 O(k)。