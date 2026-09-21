# 297. 二叉树的序列化与反序列化 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 297. 二叉树的序列化与反序列化（Serialize and Deserialize Binary Tree）· **困难**（v2 新增题 · 前序遍历 + 队列/递归） |
| 链接 | https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-21 |
| 最终提交 | ✅ **ACCEPTED - 53/53 用例通过**（leetgo 复提交） |
| 运行时间 | 108 ms |
| 内存 | 22.2 MB |

## ⚠️ 失败记录（一次，Restrictions Failed）

| 提交 | 结果 | 根因 |
|------|------|------|
| 750706745 | **Restrictions Failed** | 代码末尾不完整（`root, _ = fun(0` 缺 `)`）——力扣的代码限制检查拦截 |

**Restrictions Failed 是力扣的"代码限制检查"**（非普通 WA/TLE/RE）。触发点：本地调试代码（`visualize_tree()`、`exit()`）或代码不完整。用户本地 test.py 的 `__main__` 里有 `visualize_tree(root)` + `exit()`，这两个是"本地能跑、力扣禁止"的典型——**提交前必须删掉本地调试代码**。

## 解法（用户前序遍历 + N 标记空节点）

```python
class Codec:
    def serialize(self, root):
        result = []
        def fun(root):
            if root:
                result.append(str(root.val) + ",")
                fun(root.left)
                fun(root.right)
            else:
                result.append("N,")
        fun(root)
        return "".join(result)[:-1]          # 先 join 再去末尾逗号

    def deserialize(self, data):
        data_list = data.split(",")
        length = len(data_list)
        def fun(index):
            if index > length - 1 or data_list[index] == 'N':
                return None, index             # 返回"最后处理的位置"
            root = TreeNode(int(data_list[index]))
            root.left, index = fun(index + 1)
            root.right, index = fun(index + 1)
            return root, index
        root, _ = fun(0)
        return root
```

## 核心：前序 + N 标记

- **serialize**：前序遍历，空节点记 `N`（带 `N` 才能唯一还原树结构）；
- **deserialize**：按前序顺序递归重建，`fun(index)` 返回"最后处理的位置"，左右子树都从 `+1` 位置开始。

## 关键调试历程（用户 3 处 bug）

1. serialize `[:-1]` 切错对象（应 `"".join(...)[:-1]` 先 join 再切，否则少一个 N + 末尾逗号）；
2. deserialize 右子树 `fun(index+1)` 多余 +1（index 语义理解）；
3. 节点值要 `int()`（力扣比较 int，字符串会 WA）。

## 验证

- 对拍往返一致（序列化再反序列化 = 原树）；
- 样例：`[1,2,3,null,null,4,5]` → 往返还原一致。

## 复杂度

- 时间 **O(n)**；空间 O(n)。