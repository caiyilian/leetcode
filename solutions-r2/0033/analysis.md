# 33. 搜索旋转排序数组 · 解析（二刷）

## 一、核心思路：旋转数组的"半有序"性质

**问题**：数组原本有序（无重复），旋转 k 位后仍可用二分——因为**mid 把数组切成两半，必有一半是整体有序的**：

```
nums = [4,5,6,7,0,1,2]（旋转了 3 位的 [0,1,2,4,5,6,7]）
mid = 3 → 7
左半 [4,5,6,7] 有序 ✅，右半 [0,1,2] 有序（相对 mid 后段）
```

**策略**：判断哪半有序 → 再看 target 是否落在该半的有序区间 → 是则进那半，否则去另一半。**每次迭代丢弃一半，仍是 O(logn)。**

## 二、代码（标准版主解）

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[left] <= nums[mid]:               # 左半有序（含 left==mid：只有两个元素）
        if nums[left] <= target < nums[mid]:  # 区间包含判断
            right = mid - 1
        else:
            left = mid + 1
    else:                                      # 右半有序
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1
return -1
```

**要点**：
- `nums[left] <= nums[mid]` 用 `<=`（不是 `<`）——left==mid（两元素）时也落入左半有序分支，处理单元素/双元素边界；
- 区间包含 `nums[left] <= target < nums[mid]` **开闭要统一**：左闭右开（`< nums[mid]`）避免 mid 本身已被检查的重复判断；
- 右半同理 `nums[mid] < target <= nums[right]`。

## 三、⚡ 只记两路，别绕四分支

今天 WA 两次的根源：试图按 `mid vs target` 大小分四大类，边界极多。**正确心智模型只有两种**：

```
① 左半有序 → target 在 [left, mid) 吗？在→去左，不在→去右
② 右半有序 → target 在 (mid, right] 吗？在→去右，不在→去左
```

**想明白"哪半有序 + target 在不在里面"就够了**，分支数天然只有 2 组。

## 四、复杂度

- 时间：O(logn)
- 空间：O(1)

## 五、一刷 vs 二刷

- 一刷（9-17）：旋转二分，WA×2→RE→AC×2（当时也是边界多写到 RE/WA）；
- 二刷（10-30）：15:52 标准版 AC → 18:34 试写四分支 WA → 18:37 修复 AC。**经验重申：旋转数组一律用"判有序半段"模板，简单不易错。**

## 六、关联题目（旋转家族）

| 变体 | 题目 |
|------|------|
| 无重复找 target | **33 本体** |
| 有重复找 target | **81**（遇 `nums[left]==nums[mid]` 就 left++ 缩小） |
| 找最小值 | **153**（找断点）/ 154（有重复） |
| 二分答案进阶 | 875、1011（mid 作"答案"而不是"下标"） |

## 七、一句话记住

> **旋转数组二分 = mid 必切开一个有序半段：判 nums[left]<=nums[mid] 左半有序，用左闭右开区间判断 target 在不在；只记两路，别绕四分支；153 找最小 = 找断点，同模板。**