# 215. 数组中的第 K 个最大元素 · 解析

## 题目简述

数组（含重复）中找第 k 大的元素。如 `[3,2,1,5,6,4]` k=2 → 5。

## 核心套路一：快速选择（QuickSelect，进阶 O(n)）

**快排 partition 的隐藏性质**：每轮分区后 pivot 落在最终位置 → **第 k 大在左还是右直接由 pivot 位置决定，只搜一边**。

### 三路分区版（用户自写，最直观）

```python
def fast_choose(nums, k):
    pivot = random.choice(nums)         # 随机化：防有序输入退化 O(n²)
    left, middle, right = [], [], []    # 三路：> pivot / == pivot / < pivot
    for n in nums:
        if n > pivot: left.append(n)
        elif n < pivot: right.append(n)
        else: middle.append(n)

    if len(left) >= k:                             # 第 k 大在"比 pivot 大"的那堆
        return fast_choose(left, k)
    elif len(left) + len(middle) >= k:             # 第 k 大恰好 == pivot
        return pivot
    else:                                          # 第 k 大在"比 pivot 小"的那堆
        return fast_choose(right, k - len(left) - len(middle))
```

**三路分区的两个好处**：
1. **自然处理重复元素**（== pivot 单独一堆，不参与递归）；
2. **随机 pivot**：`random.choice` 保证期望 O(n)，否则最坏 O(n²)（有序数组 + 固定取头/尾）。

**为什么 O(n)**：每轮只递归一边，搜索空间平均减半 → n + n/2 + n/4 + … = O(n)。

## 核心套路二：堆（大小为 k 的最小堆）

```python
heap = nums[:k]
heapq.heapify(heap)                 # O(k) 建堆
for num in nums[k:]:
    if num > heap[0]:               # 比"第 k 大"还大 → 挤进来
        heapq.heapreplace(heap, num)  # 弹堆顶 + 插入
return heap[0]                       # 堆顶 = 第 k 大
```

**直觉**：堆里永远存"当前最大的 k 个数"，堆顶是这 k 个里最小的 → 即全局第 k 大。比堆顶小的数进来没意义。

## 堆的内部机制（用户提问重点，手写堆）

**堆 = 完全二叉树 + 数组存储**，父子下标公式：

```
父 = (i-1)//2    左子 = 2i+1    右子 = 2i+2
```

**两个操作**：
- **上浮 sift_up**（插入）：新元素放末尾，比父小就交换，往上冒；
- **下沉 sift_down**（删顶）：取堆顶，末尾搬到堆顶，和更小的儿子交换，往下沉。

**⚠️ 删除堆顶 = 取 arr[0] + 末尾搬顶 + sift_down**（用户踩坑点：直接 `pop()` 弹末尾是错的——最小值在堆顶）。

## 三种方案对比

| 方案 | 复杂度 | 备注 |
|------|--------|------|
| 排序 | O(n log n) | 保底，别当最终答案 |
| **堆** | **O(n log k)** | 工程最稳，`heapq` 10 行 |
| **快速选择** | **O(n) 平均** | 进阶要求，随机化是关键 |

## 复杂度

- 快速选择：时间 **O(n) 平均 / O(n²) 最坏**（随机化摊掉），空间 O(n)（三路数组）/ O(log n)（原地双指针版）；
- 堆：时间 **O(n log k)**，空间 **O(k)**。

## 考点

- **Top-K 问题**（堆 / 快速选择两大流派）
- 快速选择的"只搜一边"（与快排"两边都搜"的区别）
- 随机化防退化
- 堆的内部机制（手写 push/pop）

## 易错点

1. **下标换算**：第 k 大 = 第 n-k+1 小（三路分区版用"k 大"视角避免换算）；
2. `heapq` 是最小堆，求第 k 大维护"k 个最大"；求第 k 小维护"k 个最小"（方向别反）；
3. 快速选择忘随机 pivot → 有序输入 TLE；
4. 手写堆 `pop()` 弹末尾（应弹堆顶三步）；
5. 堆里 `heapreplace`（弹+插）比先 pop 再 push 高效。

## 关联题

- **347 前 K 个高频元素**（堆 + 哈希计数，Top-K 变形）；
- **295 数据流的中位数**（双堆：大顶堆 + 小顶堆，进阶）；
- 快速选择同源：169 多数元素（摩尔投票/快选）。