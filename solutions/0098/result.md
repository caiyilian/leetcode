# 98. 验证二叉搜索树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 98. 验证二叉搜索树（Validate Binary Search Tree）· 中等 |
| 链接 | https://leetcode.cn/problems/validate-binary-search-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 86/86 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 20.9 MB |

## 解法（用户中序递增法，已验证）

**BST 的性质：中序遍历结果是严格递增序列**——`左 < 中 < 右`。所以中序遍历时记录上一个访问值 `last`，一旦出现 `当前值 <= last`（非严格递增）就不是 BST。

```python
class Solution:
    def isValidBST(self, root):
        last_list = [float('-inf')]          # 上一个中序值（-inf 做哨兵，任何 int 都大于它）
        def fun(tree_root):
            if tree_root:
                left_bool = fun(tree_root.left)
                if tree_root.val > last_list[0]:
                    last_list[0] = tree_root.val
                else:
                    return False             # 非严格递增 → 不是 BST
                if left_bool is False:
                    return False
                right_bool = fun(tree_root.right)
                return right_bool
            return True
        return fun(root)
```

**细节**：
- `float('-inf')` 哨兵保证第一个节点必然 > last（力扣节点值范围 [-2^31, 2^31-1]，-inf 恒小于任何 int）；
- **严格递增**（`>` 更新、`<=` 判错）：重复值不算 BST（如 `[2,2,2]` → False）；
- 中序法天然处理"子树边界"陷阱（如 `[5,4,6,null,null,3,7]` 中 3 在右子树却小于 5）——中序序列 [4,5,3,6,7] 直接暴露非递增。

## 验证（三重）

- 对拍 **5 万组随机树** vs 两个参照（中序收集法 + 区间递归法）**均 0 不一致**；
- **合法 BST 专项 2 万组 0 误判**；
- 经典陷阱用例全过：`[2,1,3]→True`、`[5,1,4,null,null,3,6]→False`、`[5,4,6,null,null,3,7]→False`、`[2,2,2]→False`、空树→True、单节点→True。

## 复杂度

- 时间 **O(n)**（每节点一次）；空间 **O(h)** 递归栈。