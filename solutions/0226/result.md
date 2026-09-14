# 226. 翻转二叉树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 226. 翻转二叉树（Invert Binary Tree）· 简单 |
| 链接 | https://leetcode.cn/problems/invert-binary-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-14 |
| 最终提交 | ✅ **ACCEPTED - 77/77 用例通过** |
| 运行时间 | **0 ms（击败 100%）** 网页与 leetgo 一致 |
| 内存 | 19 MB 左右 |

## 提交记录

| 时间 | 状态 | 说明 |
|------|------|------|
| 19:32 | ✅ **Accepted 0ms** | **一次提交即过**（网页记录） |
| 19:41 | ✅ Accepted 77/77 | leetgo 复现（0ms/100%） |

## 解法（用户版，已验证）

```python
class Solution:
    def invertTree(self, root):
        return self.fun(root)

    def fun(self, root):
        if root:
            root.left, root.right = self.fun(root.right), self.fun(root.left)
            return root
        return root
```

**隐藏考点——元组赋值先求值**：`root.left, root.right = fun(right), fun(left)` 中 Python 先求值右边两个递归（此时还没交换），拿到翻转后的子树再同时赋值——"先递归翻转、再交换"一步到位。若先交换再递归会翻两次抵消（经典陷阱）。

## 验证

- 对拍 **5 万组随机树 0 错误**（修复脚本后：两版独立建树）；
- **幂等性 2 万组 0 错误**（翻转两次 = 原树）——从另一个角度证明正确；
- 官方样例全过。

## 踩坑记录

- leetgo 本地 Case 2 显示 failed：`expected "[2,3,1]", got "[2, 3, 1]"`——**这是本地字符串比对的空格差异，非逻辑错误**；在线测试与提交全对，以在线为准。

## 复杂度

- 时间 **O(n)**（每节点访问一次）、空间 **O(h)** 递归栈（最坏 O(n)）。