# 543. 二叉树的直径 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 543. 二叉树的直径（Diameter of Binary Tree）· 简单 |
| 链接 | https://leetcode.cn/problems/diameter-of-binary-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-14 |
| 最终提交 | ✅ **ACCEPTED - 106/106 用例通过** |
| 运行时间 | 3 ms（击败 87%） |
| 内存 | 22 MB |

## ⚡⚡ 重点标记：递归返回值 ≠ 题目答案（543 的灵魂）

**`fun` 干着两件不同的活：**

```
职责①（函数体内）：left_dep + right_dep = 经过当前节点的直径 → 更新全局 max_list[0]
职责②（返回值）：  max(left_dep, right_dep) + 1 = 单腿深度 → 喂给父节点继续拼
```

- **直径是"横"的（两腿相加）**，深度是"竖"的（单腿）——fun 用两腿更新答案，用一条腿喂父节点；
- 如果 fun 返回直径，父节点就断了"往下伸多深"的信息，无法继续拼接；
- **这个模式是 124 最大路径和（二叉树 HOT100 困难题）的同款骨架**——看懂了 543，124 的"返回单边最大和"就懂一半。

## 解法（用户看视频后实现，已验证）

```python
class Solution:
    def diameterOfBinaryTree(self, root):
        max_list = [0]
        self.fun(root, max_list)
        return max_list[0]

    def fun(self, root, max_list):
        if root:
            left_dep = self.fun(root.left, max_list)
            right_dep = self.fun(root.right, max_list)
            max_list[0] = max(left_dep + right_dep, max_list[0])  # 两腿
            return max(left_dep, right_dep) + 1                    # 单腿
        return 0
```

## 验证

- 对拍 **5 万组随机树 vs 暴力 BFS**（带 parent 三方向可达）**0 错误**；
- 边界：空树 0、单节点 0、`[1,2,3,4,5]` → **3**（路径 4→2→1→3，三边）、`[1,2]` → 1 全对；
- **踩坑记录**：首次验证的暴力参照 BFS 只向下走（无 parent），跨子树路径算不出——参照本身写错，非用户代码问题；修复参照（三方向）后 0 不一致。

## 复杂度

- 时间 **O(n)**（每节点一次）；空间 **O(h)** 递归栈。