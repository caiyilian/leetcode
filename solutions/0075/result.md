# 75. 颜色分类 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 75. 颜色分类（Sort Colors）· 中等（荷兰国旗三指针） |
| 链接 | https://leetcode.cn/problems/sort-colors/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-20 |
| 最终提交 | ✅ **ACCEPTED - 90/90 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.1 MB |

## 解法（用户荷兰国旗三指针，标准）

```python
class Solution:
    def sortColors(self, nums):
        low = 0
        curr = 0
        high = len(nums) - 1
        while curr <= high:
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                curr += 1
                low += 1
            elif nums[curr] == 2:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1          # curr 不动（换来的还没检查）
            else:
                curr += 1
```

## 三指针的含义

- `low`：0 区域的右边界（下一个 0 放这里）；
- `curr`：当前扫描位置；
- `high`：2 区域的左边界（下一个 2 放这里）。

**关键细节**：遇到 2 交换后 `curr` **不前进**——因为从 high 换过来的元素还没检查过，可能是 0 或 1，需要下一轮再判断。

## 验证

- 对拍 **5 万组随机数组 vs sorted 0 不一致**；
- 样例：`[2,0,2,1,1,0]→[0,0,1,1,2,2]`、`[2,0,1]→[0,1,2]`。

## 复杂度

- 时间 **O(n)**；空间 O(1)。

## 备注

- leetgo 对「原地修改 + 返回 None」题型，`__main__` 缺少 `Solution().`，归档时已手动补上（与 283 moveZeroes 同款坑）。