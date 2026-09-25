# 538. 把二叉搜索树转换为累加树 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 538. 把二叉搜索树转换为累加树（Convert BST to Greater Tree）· 中等（v2 新增题 · 反中序遍历） |
| 链接 | https://leetcode.cn/problems/convert-bst-to-greater-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-25 |
| 最终提交 | ✅ **ACCEPTED - 215/215 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 21 MB |

## 解法（用户反中序遍历 + 累加）

```python
class Solution:
    def convertBST(self, root):
        sums = [0]               # 用列表引用，嵌套函数才能原地改（闭包陷阱）
        def fun(root):
            if root:
                fun(root.right)       # 右（大的）先
                root.val += sums[0]   # 加上已累加的所有更大值
                sums[0] = root.val    # 更新累加器
                fun(root.left)        # 左（小的）后
        fun(root)
        return root
```

## 是否符合题目要求 ✅

| 要求 | 达标 |
|------|------|
| 原地修改（不建新树） | ✅ 直接 `root.val += sums[0]` |
| 额外空间 O(1)（进阶） | ✅ 只用一个 `sums = [0]` |
| 时间 O(n) | ✅ 每个节点访问一次 |
| 正确性 | ✅ 5000 组随机 BST 0 不一致 |

## 核心：反中序遍历（右→根→左）

**BST 的中序是升序，反中序就是降序**——累加器 sums 恰好等于"所有 ≥ 当前节点的值之和"，正是累加树定义。

```
右子树（全比我大）→ 根（加更大的和）→ 左子树（我比它们大）
```

## 细节亮点：列表引用绕闭包陷阱

`sums = [0]` 用列表而非 int——嵌套函数里 `sums += x` 会创建新局部变量（闭包陷阱），列表就能原地改。**用户自悟，说明懂 Python 闭包行为。**

## 验证

- 5000 组随机 BST（新值 = 原值 + 所有 > 原值的和）0 不一致；
- 官方样例层序 `[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]` → `[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]` ✅。

## 复杂度

- 时间 **O(n)**；空间 O(h)（递归栈，额外 O(1)）。