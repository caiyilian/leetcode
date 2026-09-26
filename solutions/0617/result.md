# 617. 合并二叉树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 617. 合并二叉树（Merge Two Binary Trees）· 简单（v2 新增题 · 二叉树递归） |
| 链接 | https://leetcode.cn/problems/merge-two-binary-trees/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-26 |
| 最终提交 | ✅ **ACCEPTED - 182/182 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.2 MB |

## ⚠️ 失败记录（WA → AC）

| 提交 | 结果 | 原因 |
|------|------|------|
| 751500826 | **WA** | **`fun(root1, root2)` 的返回值没接住**——内部 `root1 = root2` 只是局部绑定，外面 root1 不变（root1 为 None 时拿不到 root2） |
| 751500904 | AC | `root1 = fun(root1, root2)` ✅ 接住返回值 |

**教训**：递归函数内部对参数的赋值（`root1 = root2`）不会传到外面，必须通过返回值传递。

## 解法（用户原地合并，标准）

```python
class Solution:
    def mergeTrees(self, root1, root2):
        def fun(root1, root2):
            if root1 and root2:                # ① 都不为 None：值相加 + 递归左右
                root1.val += root2.val
                root1.left = fun(root1.left, root2.left)
                root1.right = fun(root1.right, root2.right)
            elif root2:                        # ② 只有 root2：直接采用
                root1 = root2
            return root1                       # ③ 只有 root1：返回 root1

        root1 = fun(root1, root2)              # ★ 接住返回值
        return root1
```

## 三种情况

| 情况 | 处理 |
|------|------|
| root1 和 root2 都不为 None | 值相加，递归合并左右子树 |
| root1 为 None、root2 不为 None | 用 root2（`root1 = root2`） |
| root1 不为 None、root2 为 None | 保持 root1 |

## 验证

- 对拍 **5000 组随机树（深拷贝隔离）0 不一致**；
- 样例：`[1,3,2,5] + [2,1,3,null,4,null,7] → [3,4,5,5,4,null,7]` ✅。

## 复杂度

- 时间 **O(min(n1, n2))**（重叠部分遍历）；空间 O(h)（递归栈）。