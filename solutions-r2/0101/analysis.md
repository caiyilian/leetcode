# 101. 对称二叉树 · 解析（二刷）

## 一、核心思路：镜像交叉递归

对称 = 左子树 和 右子树 互为**镜像**。判断两棵树是否互为镜像：

- 都空 → 镜像 ✅
- 一个空一个不空 → 不是镜像 ❌
- 值不同 → 不是镜像 ❌
- 否则递归：**左子 ↔ 右子** + **右子 ↔ 左子**（交叉！）

```
    1
   / \
  2   2        fun(左2, 右2):
 / \ / \         val 相等 → fun(左2.left=3, 右2.right=3)  ✓
3 4 4 3                   → fun(左2.right=4, 右2.left=4)  ✓
          对称 → True
```

**交叉是关键**：对称比较的是 `tree1.left` vs `tree2.right`（不是 `tree1.left` vs `tree2.left`）——前者是镜像，后者是相同。

## 二、用户版代码（修复后）

```python
def fun(tree1, tree2):
    if tree1 or tree2:                                    # 有一个非空才比
        if (tree1 is None) or (tree2 is None) or (tree1.val != tree2.val):
            return False                                   # 空/值不等 → False
        result1 = fun(tree1.left, tree2.right)             # 左 ↔ 右
        if result1 is False:
            return False                                   # 剪枝：左先错直接返回
        result2 = fun(tree1.right, tree2.left)             # 右 ↔ 左
        return result2
    return True                                            # 都空 → True
return fun(root, root)                                     # ★ 空树也正确
```

亮点：
- `if tree1 or tree2` 把"两边都空"提前短路（都空直接 True）；
- 先查 `tree1 is None or tree2 is None` 再取 `.val`——**先判空再取值**的防御顺序正确；
- 剪枝：`result1 is False` 时提前返回，不白走右分支。

## 三、⚡ 空树边界（本次修复点）

原版 `return fun(root.left, root.right)`——`root` 为 None 时空树直接崩溃。修复改为 `return fun(root, root)`：空树时 `fun(None, None)` 走 `if tree1 or tree2:` 不成立 → 返回 True，天然正确。

**为什么容易漏**：本题约束 `1 <= 节点数`，官方无空树用例，本地不测就发现不了。**二叉树递归题，入口处空树是一想起就要问的边界**（94/98/104 都该有这个意识）。

## 四、复杂度

- 时间：O(n)——每个节点访问一次
- 空间：O(h)——递归栈

## 五、一刷 vs 二刷

- 一刷（9-14）：镜像交叉递归 AC ×2，模板留了 `if not root: return True`（⚡ 空树=True）；
- 二刷（10-23）：思路一次写对，入口简化时丢了空树边界 → 对拍抓出修复。**核心内化，边界要记牢**。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| 镜像/交叉递归 | 226 翻转二叉树（镜像对称的"反操作"）、100 相同的树（不交叉，直比） |
| 双节点递归 | 236 最近公共祖先（双节点）、572 另一棵树的子树 |
| 层序/迭代版 | 101 迭代（队列两两入队）、102 层序 |

**100 相同的树 = 101 非交叉版**（`fun(left,left)` 直比），对比着学很清晰。

## 七、一句话记住

> **对称二叉树 = 镜像交叉递归：左↔右、右↔左；先判空再取值；入口 return fun(root, root) 天然覆盖空树（⚡ 空树=True）。**