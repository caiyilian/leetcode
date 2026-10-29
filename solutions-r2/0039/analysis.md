# 39. 组合总和 · 解析（二刷）

## 一、核心思路：回溯 + 排序剪枝

**问题**：从 candidates（无重复）中选任意个数（**可重复**）使和为 target，返回所有组合（**顺序不同的算同一个**）。

两个关键约束：
1. **可重复选** → 递归时还能选当前数；
2. **去顺序重复** → 组合是"无序集合"，[2,3] 和 [3,2] 只算一个 → 递归时只能从"当前及之后"开始（不回头）。

```
candidates=[2,3,6,7] target=7（可重复、不回头）
树根选择依次为 2,3,6,7（每层从 start 开始，永远不回退到更小的数）
→ 得到 [2,2,3] 和 [7]，不会出现 [3,2,2]
```

## 二、代码（用户 AC 版）——一个 start 管两件事

```python
candidates.sort()                          # 排序（为剪枝）
result = []

def fun(path, now_sum=0, start=0):
    if now_sum == target:
        result.append(path.copy())         # ★ copy 防引用共享
        return path
    if now_sum > target:
        return path
    for n in candidates[start:]:           # 不回头 → 去顺序重复
        if now_sum + n > target:
            break                           # 已排序，后面更大 → 剪枝
        path.append(n)
        path = fun(path, now_sum + n, start)  # 递归传 start → 可重复选现在这个
        path.pop()
        start += 1                          # 本层循环自增 → 下一个数才能用
    return path
```

**start 的双重身份**（用户妙点）：
- 作为**递归参数**传给下一层 → 下一层还能选当前数（可重复）；
- 作为**本层循环推进**（start += 1）→ for 循环从更靠后的位置开始（不回头）。

## 三、两个必考细节

1. **`path.copy()` 收集**：path 是递归共享的列表，加入 result 若直接 append(path)，回溯 pop 会把已存结果改坏——**必须 copy**；
2. **排序 + break 剪枝**：`now_sum + n > target` 时 break（排序保证后面更大），省掉大量无效分支。

**标准索引版等价写法**（更易推广到 40/216）：
```python
def dfs(i, path, cur):
    if cur == target: res.append(path.copy()); return
    if i >= len(candidates) or cur > target: return
    path.append(candidates[i]); dfs(i, path, cur + candidates[i]); path.pop()  # 选（可重复）
    dfs(i + 1, path, cur)                                                       # 不选
```

## 四、复杂度

- 时间：O(指数)（组合问题本质；剪枝后只遍历可行分支）
- 空间：O(target / 最小元素)（递归深度上限）

## 五、一刷 vs 二刷

- 一刷（9-16）：回溯可重复选，AC ×7（多版演进，最后 3ms）；
- 二刷（10-29）：**一次 AC，三个要点一次写对**——start 双用途、排序剪枝、copy 收集。

## 六、关联题目（组合/子集家族）

| 套路 | 相关题 |
|------|--------|
| 可重复选 | 39 本体（⚡）、无限背包变形 |
| 不可重复选 | **40 组合总和 II**（去重剪枝）、**78 子集**、90 子集 II |
| 定长组合 | 77 组合、**216 组合总和 III** |
| 排列（可回头） | 46 全排列（used 数组） |

**一句话区分**：组合题用"start 不回头"（39/40/77/216），排列题用"used 数组"（46）——这是回溯两大模板的核心差异。

## 七、一句话记住

> **组合总和 = 回溯：递归传 start（可重复选）+ 循环 start+=1（不回头）；排序后 break 剪枝；收集必须 path.copy()。**