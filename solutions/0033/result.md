# 33. 搜索旋转排序数组 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 33. 搜索旋转排序数组（Search in Rotated Sorted Array）· 中等（二分查找分类第 4 题） |
| 链接 | https://leetcode.cn/problems/search-in-rotated-sorted-array/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 197/197 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）+ 内存击败 98%** |

## ⚠️ 本次失败史（用户要求记录：4 次提交，3 次失败）

| 提交 | 结果 | 失败原因（力扣代码逐行分析） |
|------|------|------------------------------|
| 749738051 | **WA** | "夹逼找旋转点 k"路线：`while nums[left] > nums[right]: left+=1; right-=1` 在**未旋转/非对称旋转**时 k 算错（如未旋转算成 k=length）→ 后续 `nums[mid-k]` 负索引取尾部元素、`left-k+length` 可能越界 → 答案错 |
| 749738180 | **RE** | 同上路线；未旋转时 k=0，二分找不到 target 后 `left` 收敛到 `length` → `nums[left-k] = nums[length]` **IndexError 越界** |
| 749739654 | **WA** | 用 `(left-k+length) % length` 修好了索引越界，但**夹逼算出的 k 本身还是错的**（根源未除）→ 依然 WA |
| 749743098 | **AC** | 放弃找 k，改用"一次二分判断左右段"标准解（下方） |

**共同根源（最重要的一条教训）**：**"显式求旋转点 k"这条路本身脆弱**——夹逼法无法稳定求 k（旋转点位置任意），且求出后索引映射极易越界。标准解**根本不求 k**：利用"mid 必然落在左升序段或右升序段之一"，一次二分内直接判断 target 在哪个段。

## 最终解法（用户按提示重写，标准解）

```python
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:        # 左半段递增
                if nums[left] <= target < nums[mid]:
                    right = mid - 1            # target 在左段内 → 左走
                else:
                    left = mid + 1             # 否则去断裂处（右）
            else:                               # 右半段递增
                if nums[mid] < target <= nums[right]:
                    left = mid + 1             # target 在右段内 → 右走
                else:
                    right = mid - 1            # 否则去断裂处（左）
        return -1
```

## 验证

- 对拍 **5 万组随机旋转数组（含未旋转 k=0 / 完全旋转 / 单元素）vs 线性 index 参照 0 不一致**；
- 官方样例：`[4,5,6,7,0,1,2]`+0→4、+3→-1、`[1]`+0→-1；边界 `[1,3]`+3→1、`[3,1]`+1→1。

## 复杂度

- 时间 **O(log n)**；空间 **O(1)**。