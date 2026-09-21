# 297. 二叉树的序列化与反序列化 · 解析

## 题目简述

设计 Codec：把二叉树序列化成字符串，再从字符串反序列化还原（往返一致）。

## 核心套路：前序遍历 + N 标记空节点

```
serialize：前序 DFS，空节点记 'N'
  1,2,N,N,3,4,N,N,5,N,N

deserialize：按前序递归重建
  fun(index) 处理 data_list[index]，返回 (节点, 最后处理的位置)
```

**关键**：必须标记空节点（`N`），否则无法唯一确定树结构。

## serialize 的两个坑

```python
return "".join(fun(root)[:-1])     # ❌ 切的是列表（少一个 N）
return "".join(result)[:-1]        # ✅ 先 join 成字符串，再去末尾逗号
```

## deserialize 的 index 语义（用户卡点）

```python
def fun(index):
    if index > length-1 or data_list[index] == 'N':
        return None, index              # 返回"最后处理的位置"
    root = TreeNode(int(data_list[index]))
    root.left, index = fun(index + 1)   # 左子树从下一个位置
    root.right, index = fun(index + 1)  # 右子树从"左子树最后位置 + 1"
    return root, index
```

**index 的两种语义**（都可，但要自洽）：
- 语义 A「下一个待处理位置」：左子树 `fun(index+1)`，右子树 `fun(index)`，return 不加 1；
- 语义 B「最后处理的位置」（用户用的）：左/右子树都 `fun(index+1)`，return 返回 index。

**关键是理解 `fun(index)` 返回什么**——用户一开始的 bug 就是两种语义混用（左子树用 A、右子树用 B）。

## ⚠️ 力扣 Restrictions Failed（用户踩坑）

**Restrictions Failed = 力扣的代码限制检查失败**，不是算法错误。常见触发：

| 禁止项 | 说明 |
|--------|------|
| `exit()` / `quit()` | 本地能退出程序，力扣禁止 |
| 本地自定义模块 | 如 `from tree_utils import ...`（力扣没有） |
| 文件/网络操作 | `open()`、socket 等 |
| `os` / `sys` / `subprocess` | 被限制 |
| 代码不完整 | 语法残缺（缺括号等） |

**用户的坑**：本地 test.py 的 `__main__` 里有 `visualize_tree(root)`（本地可视化）+ `exit()`，提交前没删干净 → Restrictions Failed。

**教训：提交力扣前，删掉所有本地调试代码（可视化、exit、本地 import）。**

## 复杂度

- 时间 **O(n)**；空间 O(n)。

## 考点

- 前序遍历序列化
- 空节点标记
- 递归重建 + index 传递
- **力扣沙箱限制**（提交规范）

## 关联题

- **105 从前序与中序遍历构造二叉树**（重建，已 AC）；
- **449 序列化与反序列化 BST**（BST 版，可用范围）；
- v2 新增题：85、96、221、297（均已完成）。