# 105. 从前序与中序遍历序列构造二叉树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 105. 从前序与中序遍历序列构造二叉树（Construct Binary Tree from Preorder and Inorder）· 中等 |
| 链接 | https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 203/203 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 21 MB（击败 74%） |

## 解法（用户定稿，标准最优解）

**核心思路（用户 docstring 总结）**："前序是根左右，中序是左根右"——**前序给"根是谁"，中序给"根的左右各有几个"**。

```python
class Solution:
    def buildTree(self, preorder, inorder):
        index_dict = {i: v for v, i in enumerate(inorder)}   # 值 → 中序索引
        length = len(preorder)
        left1, right1, left2, right2 = 0, length-1, 0, length-1
        def fun(left1, right1, left2, right2):
            if left1 > right1:
                return None
            root = TreeNode(preorder[left1])          # 前序第一个 = 根
            index = index_dict[preorder[left1]]       # 根在中序的索引
            left_count = index - left2                # 左子树节点数
            root.left = fun(left1+1, left1+left_count, left2, index-1)
            root.right = fun(left1+left_count+1, right1, index+1, right2)
            return root
        return fun(left1, right1, left2, right2)
```

**两个细节评价**：
- `index_dict` 预哈希：O(1) 定位根的索引（不预计算则 `inorder.index()` O(n) → 总 O(n²)）；
- 基线只查前序边界 `left1 > right1` 即可（两个序的子树范围同步变化）。

## 验证

- 对拍 **5 万组随机树**：重建后**前序/中序/结构三重一致** 0 错误；
- 官方样例：`[3,9,20,15,7] + [9,3,15,20,7]` → 重建正确；`[-1]+[-1]` → 正确。

## 踩坑记录

- leetgo 本地 Case 1 假失败（`[3, 9, 20, ...]` vs `[3,9,20,...]` 空格差异），在线 Accepted——以在线为准。

## 复杂度

- 时间 **O(n)**（每节点一次 + hash 定位 O(1)）；
- 空间 **O(n)**（index_dict）+ **O(h)** 递归栈。