# 617. 合并二叉树 · 解析

## 题目简述

合并两棵二叉树：重叠节点值相加，不重叠的节点直接保留。

## 核心套路：递归三情况

```python
def fun(root1, root2):
    if root1 and root2:                # ① 都不空：值相加，递归左右
        root1.val += root2.val
        root1.left = fun(root1.left, root2.left)
        root1.right = fun(root1.right, root2.right)
    elif root2:                        # ② 只有 root2：采用 root2
        root1 = root2
    return root1                       # ③ 只有 root1：返回 root1
```

## ⚠️ 关键坑：递归返回值必须接住（用户 WA 点）

```python
fun(root1, root2)          # ❌ 调用但不接 → 当 root1 为 None 时，外面的 root1 还是 None
root1 = fun(root1, root2)  # ✅ 接住返回值
```

**为什么**：`fun` 内部执行 `root1 = root2` 时，只是把**局部变量 root1** 重新绑定到 root2——**不会改变外层变量**。要让"root1 为空时采用 root2"生效，必须让 fun **返回** root2，外层**接住**。

**通用教训**：递归函数里"对参数重新赋值"是局部操作，**结果一定要通过返回值传出来**。

## 复杂度

- 时间 **O(min(n1, n2))**；空间 O(h)。

## 考点

- 二叉树递归（三情况分治）
- **递归返回值传递**（参数赋值是局部的）
- 原地合并

## 易错点

1. 递归返回值没接住（用户 WA 点）；
2. 三情况漏掉"只有 root1"（返回 root1 即可，什么都不用做）；
3. 用 `elif root2` 而非 `if root2`（root1 为空、root2 不空时进入）。

## 关联题

- **226 翻转二叉树**（递归，已 AC）；
- **100 相同的树**（双树递归）；
- **104 最大深度**（递归，已 AC）；
- v2 新增题：85、96、221、297、309、312、337、338、399、406、448、461、494、538、581、617（均已完成）。