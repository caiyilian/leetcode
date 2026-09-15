# 108. 将有序数组转换为二叉搜索树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 108. 将有序数组转换为二叉搜索树（Convert Sorted Array to BST）· 简单 |
| 链接 | https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 31/31 用例通过** |

## 解法（用户分治 + 中点取根，与官方解法一致）

**思路（用户自述）**：平衡 → 左右高度差 ≤1 → **中点作为根**，把数组劈成左右两半，递归同样处理；空列表 → None。

```python
class Solution:
    def sortedArrayToBST(self, nums):
        return self.fun(nums)

    def fun(self, nums):
        if not nums:
            return None
        middle_index = len(nums) // 2
        root = TreeNode(nums[middle_index])
        root.left = self.fun(nums[:middle_index])
        root.right = self.fun(nums[middle_index + 1:])   # 切片越界自动截断，不会崩
        return root
```

**核心认知（用户提出）**："平衡靠构造，不靠检查"——中点劈半让左右子数组长度差 ≤1，数学上保证任意节点左右高度差 ≤1，无需事后验证。

## ⚡ 进阶标记：传下标区间版（O(n)，面试加分）

用户切片版每次 `nums[:mid]` 拷贝 O(k)，总 **O(n log n)**；进阶版传 `lo/hi` 下标**不拷贝**，每个元素只访问一次 → **O(n)**：

```python
class Solution:
    def sortedArrayToBST(self, nums):
        def fun(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            root = TreeNode(nums[mid])
            root.left = fun(lo, mid - 1)
            root.right = fun(mid + 1, hi)
            return root
        return fun(0, len(nums) - 1)
```

> 完整代码见 `solution_readable.py`。n ≤ 10⁴ 时切片版力扣无压力，但面试被问"能否 O(n)"时讲下标版。

## 验证

- 5 万组随机升序数组：**BST 性质（中序=原数组）0 错误 + 平衡性（高度差≤1）0 失败**；
- 官方样例：`[-10,-3,0,5,9]` → 中序正确、平衡、高度 3；`[1,3]`、`[]` 全对；
- 用户疑问确认：`nums[mid+1:]` 越界时 Python 切片静默截断为空 → fun 返回 None，不会崩。

## 踩坑记录

- leetgo 本地 Case 2 假失败（`[3,1]` vs `[3, 1]` 空格差异），在线 Accepted——以在线为准（同 226 题的坑）。

## 复杂度

- 用户切片版：时间 **O(n log n)**（每层切片拷贝）、空间 O(log n) 递归栈（不含结果）；
- 进阶下标版：时间 **O(n)**、空间 O(log n)。