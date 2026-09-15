# 230. 二叉搜索树中第 K 小的元素 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 230. 二叉搜索树中第 K 小的元素（Kth Smallest Element in a BST）· 中等 |
| 链接 | https://leetcode.cn/problems/kth-smallest-element-in-a-bst/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 94/94 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 22.1 MB |

## 今天两次提交的演进（用户自驱优化，代码已从力扣拉取对比）

| 时间 | 版本 | 思路 | 成绩 |
|------|------|------|------|
| 12:15 | v1 | **纯中序全收集**：`fun(root)` 收完整棵 BST → `result[k-1]` | Accepted 7ms |
| 12:22 | **v2（定稿）** | **剪枝提前终止**：append 前检查 `len(result) == k`，满了就 return，跳过右子树 | Accepted **0ms** |

**v2 唯一改动**：加了一行 `if len(result) == k: return`——收集够 k 个就"刹车"。实测剪枝效果（k=1，10 万节点 BST）：v1 全收集 6.55ms vs v2 0.00ms（快几百倍）。

## 解法（v2 定稿）

```python
class Solution:
    def kthSmallest(self, root, k):
        result = []
        def fun(root, k):
            if root:
                fun(root.left, k)
                if len(result) == k:      # 剪枝：满了就刹
                    return
                result.append(root.val)
                fun(root.right, k)
        fun(root, k)
        return result[k-1]
```

**思路（BST 性质）**：中序遍历 = 升序序列 → 第 k 小 = 中序第 k 个。边走边数，数够即停。

**剪枝边界（重要认知）**：能剪右子树 + 向上的右分支；**剪不掉左子树**（中序必须先走完左边才知够不够）→ 复杂度 **O(k + h)**。

## 进阶版（solution_readable.py）

迭代版（显式栈走中序，弹出时计数，数到第 k 个立即返回）→ 彻底的 **O(h + k)**。

## 验证

- v1/v2 各对拍 **5 万组随机 BST × 随机 k 0 错误**；
- 官方样例：`[3,1,4,null,2] k=1 → 1`、`[5,3,6,2,4,null,null,1] k=3 → 3` 全对；
- 剪枝效果实测（k=1/3，10 万节点）：v2 近乎 0ms vs v1 6.5ms。

## 复杂度

- v1：O(n) 时间 / O(n) 空间；
- v2：O(k + h) 时间 / O(h) 栈；
- 迭代版：O(h + k) 时间 / O(h) 栈。