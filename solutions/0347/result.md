# 347. 前 K 个高频元素 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 347. 前 K 个高频元素（Top K Frequent Elements）· 中等（堆分类第 2 题） |
| 链接 | https://leetcode.cn/problems/top-k-frequent-elements/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 25/25 用例通过** |
| 运行时间 | 3 ms（击败 85%） |
| 内存 | 22.5 MB（击败 73%） |

## 解法（用户版：堆存频次 + count2num 反查，含桶思想）

```python
def topKFrequent(self, nums, k):
    hash_dict = {}                  # 数字 → count_list 下标
    count_list = []                 # 每个不同数字的频次
    for n in nums:
        if n not in hash_dict:
            hash_dict[n] = len(count_list); count_list.append(1)
        else:
            count_list[hash_dict[n]] += 1
    count2num = defaultdict(list)   # 频次 → 数字列表（桶思想）
    for key, value in hash_dict.items():
        count2num[count_list[value]].append(key)
    heap = count_list[:k]; heapq.heapify(heap)   # 维护 k 个最大频次
    for num in count_list[k:]:
        if num > heap[0]: heapq.heapreplace(heap, num)
    return [count2num[count].pop() for count in heap]
```

**亮点**：`count2num`（频次 → 数字列表）是"桶排序"思想；`count2num[count].pop()` 的隐式配对（堆里 count 出现几次就 pop 几个）正确但可读性差。

## 标准版（solution_readable.py，堆存元组）

```python
def topKFrequent(self, nums, k):
    count = Counter(nums)
    heap = []
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))   # 堆存 (频次, 数字) 元组
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for _, num in heap]
```

**差异**：堆存 `(freq, num)` 元组 → 数字跟着频次走，省掉 count2num 反查表和 pop 配对。

## ⚡ 技术点（用户提问：heapify 能直接传切片吗？）

**不能**——`heapq.heapify()` 是**原地操作**（原地改 x，返回 None）。`heapify(count[:k])` 会原地修改一个"一诞生就被丢弃"的切片副本，原数组不变、结果拿不到。正确写法必须先落变量：`heap = count[:k]; heapq.heapify(heap)`。**原地函数通病**：`x.sort()` / `heapq.heapify(x)` 都返回 None，不能对临时对象操作后指望拿到结果。

## 验证

- 对拍 **5 万组随机数组 vs Counter.most_common 参照 0 不一致**（频次匹配 + 无重复）；
- 官方样例：`[1,1,1,2,2,3] k=2 → {1,2}`、`[1] k=1 → [1]`、含负数 `[4,1,-1,2,-1,2,3] k=2 → {-1,2}`。

## 复杂度

- 用户版 / 标准版均 **O(n log k)**（n = 不同数字数），满足题目要求（优于 O(n log n) 排序）；空间 O(n)。