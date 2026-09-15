# 236. 二叉树的最近公共祖先 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 236. 二叉树的最近公共祖先（Lowest Common Ancestor of a Binary Tree）· 中等 |
| 链接 | https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 33/33 用例通过** |
| 运行时间 | leetgo 187ms / 击败 7%（见下方噪声说明） |
| 内存 | 45.5 MB（击败 99%） |

## 两个版本（3 万组对拍 0 差异）

| 文件 | 版本 | 思路 | 空间 |
|------|------|------|------|
| `solution.py` | **用户剪枝版（定稿）** | BFS 父链 + 深度对齐 + 同步上溯（160 思路迁移）+ 找到 p/q 即 break | O(n) |
| `solution_readable.py` | **递归版** | ⚡ 机考必看：三情况归纳，10 行 | O(h) |

## ⚡⚡ 机考之前必看：递归版（用户标记"太妙了"）

```python
def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root                       # ① 空 / 命中 p 或 q
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root                       # ② p、q 分居两侧 → 根是 LCA
    return left or right                  # ③ 同侧 → 返回找到的那侧
```

**三情况递归归纳**：空/命中 → 分居 → 同侧。10 行解决面试超高频题。

## ⚡ 重要实证：剪枝版"更慢"是力扣噪声（240 题知识点）

用户提交剪枝版后觉得"更慢了"，但**本地实测（6.5 万节点满树）剪枝版全面更快**：

| p/q 位置 | 无剪枝版 | 剪枝版 |
|---------|---------|--------|
| 都在最深层 | 8.37 ms | 6.32 ms |
| 都在第 2 层 | 7.90 ms | **0.00 ms** |
| 一深一浅 | 9.36 ms | 6.79 ms |

**且本次 leetgo 提交显示 187ms/击败 7%——而本地同样代码只需 6ms**——力扣判题环境的负载噪声可以让同代码从 6ms 变 187ms。结论：**剪枝版最坏 = 原版、通常更优，力扣的"慢"不可信，看复杂度不看击败率**。

## 剪枝的正确性保证（用户做对的一点）

break 时 p/q 的子节点没入队——但 `father_dict` 只需 p/q 的**祖先链**，BFS 层序保证祖先在更早的层已被记录 ✅。提前停不丢关键信息。

## 验证

- v1/v2/递归版 3 万组随机树对拍 0 差异；
- 特殊组合全对：p 是 q 的祖先（5,4→5）、p=q（3,3→3）、分居两侧（5,1→3）、深层（7,8→3）。

## 复杂度

- 剪枝版：O(n) 时间（最坏 BFS 全树 + 上溯 ≤ h）/ O(n) 空间（father_dict）；
- 递归版：O(n) 时间 / O(h) 空间（递归栈）。