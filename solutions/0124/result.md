# 124. 二叉树中的最大路径和 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 124. 二叉树中的最大路径和（Binary Tree Maximum Path Sum）· **困难** |
| 链接 | https://leetcode.cn/problems/binary-tree-maximum-path-sum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 97/97 用例通过** |
| 运行时间 | **7 ms（击败 92%）** |
| 内存 | 23.7 MB |

## 🌳 二叉树分类收官题（15/15 全通关）

## 解法（用户定稿，标准最优解，543 模式完全迁移）

```python
class Solution:
    def maxPathSum(self, root):
        max_list = [float("-inf")]                    # -inf：全负树时单节点就是答案
        def fun(root):
            if root:
                max_left = max(fun(root.left), 0)     # 左贡献（负数砍掉）
                max_right = max(fun(root.right), 0)   # 右贡献（负数砍掉）
                now_max = root.val + max_left + max_right      # 两腿：更新全局答案
                to_father = root.val + max(max_left, max_right)  # 单腿：喂父节点
                max_list[0] = max(max_list[0], now_max)
                return to_father
            return 0
        fun(root)
        return max_list[0]
```

**用户 docstring 自悟**："能组成最大的，以及上报给父节点的不是同一个数"——即 543 学的"两腿更新答案/单腿喂父节点"模式，直接迁移到 124。

## 543 → 124 迁移对照

| | 543 直径 | 124 最大路径和 |
|--|---------|--------------|
| 两腿 | left_dep + right_dep | val + left + right |
| 单腿 | max(left, right) + 1 | val + max(left, right) |
| 全局 | max_list[0] | max_list[0] |
| **新增** | — | **max(x, 0) 负数截断** |

**124 相对 543 只多一个概念**：路径贡献可为负（负分支拖累路径）→ `max(贡献, 0)` 砍掉；`max_list` 初始 `-inf` 保证全负树正确。

## 验证

- 对拍 **2 万组随机树 vs 全节点对暴力枚举（带 parent + LCA 路径和）0 不一致**；
- 官方样例全对：`[1,2,3]→6`、`[-10,9,20,null,null,15,7]→42`、`[2,-1]→2`、`[-3]→-3`（全负树边界）。

## 复杂度

- 时间 **O(n)**（每节点一次）；空间 **O(h)** 递归栈（最坏 O(n) 斜树）。