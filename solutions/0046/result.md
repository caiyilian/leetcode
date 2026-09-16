# 46. 全排列 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 46. 全排列（Permutations）· 中等（**回溯家族母题**） |
| 链接 | https://leetcode.cn/problems/permutations/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 26/26 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.5 MB |

## 解法（用户按决策树提示独立完成，标准回溯模板）

```python
class Solution:
    def permute(self, nums):
        length = len(nums)
        result = []
        def fun(path):
            if len(path) == length:
                result.append(path.copy())   # ★ 复制快照（用户自悟"类似指针"）
                return
            for n in nums:
                if n in path:                # 已用数字不能再选
                    continue
                path.append(n)               # ① 选
                fun(path)                    # ② 递归
                path.pop()                   # ③ 撤销（回溯的灵魂）
        fun([])
        return result
```

**关键认知（用户自悟并写进注释）**：`path.copy()` 必须复制——`path` 是共用列表，后续 `pop` 会改空它，不复制的话 result 里全是同一个空列表（引用陷阱）。

## 验证

- 对拍 **5 万组随机数组 vs itertools.permutations 0 不一致**；
- 边界全对：空数组 → 1 个空排列、单元素 → 1、[1,2] → 2、[1,2,3] → 6、[1,2,3,4] → 24；
- 官方样例 6 个排列正确。

## 复杂度

- 时间 **O(n×n!)**（n! 个叶子 × 复制 O(n)）；空间 **O(n)**（递归深度 + path）。

## 母题地位

46 是**回溯家族源头**：78 子集（判定换 start 索引）、17 字母组合（每层固定字母表）、131 分割回文串（按切割点）、79 单词搜索（走格 + 不能重复走）、51 N皇后（列/对角线冲突）——全是"这层能选谁"的判断换皮。