# 98. 验证二叉搜索树 · 解析（二刷）

## 一、核心性质：BST ⇔ 中序遍历严格递增

**BST 定义**：左子树所有节点 < 根 < 右子树所有节点（对每个节点都成立）。
**关键等价**：对 BST 做**中序遍历**（左中右），得到的序列**严格递增**——反过来，中序严格递增的树就是 BST。

```
    5           中序: [2,5,6,8] 严格递增 → 是 BST
   / \
  2   8
     /
    6
```

所以验证 BST = **做中序遍历 + 检查每次比上一个更大**。

## 二、为什么"(每个节点)左<根<右"不够（常见误区）

只看"当前节点的左<根<右"会漏掉**跨层违反**：

```
    5
   / \
  4   6        ← 每个节点局部都满足（4<5<6），但 6 的左孩子 3 < 根 5
     / \
    3   7      中序: [4,5,3,6,7] → 3 出现在 5 后面，违反递增 → 不是 BST
```

局部检查（`node.left.val < node.val < node.right.val`）会让这种树误判为真。**必须用中序递增（全局）或上下界（全局传导）**。

## 三、用户解法：中序遍历 + last 哨兵

```python
last = [float('-inf')]          # 列表包一层：闭包内 last[0]=x 不新建局部变量
def fun(root):
    if root:
        if fun(root.left) is False:   # 左子树不合法 → 剪枝
            return False
        if last[0] >= root.val:       # 中序必须严格递增（>= 判重复值）
            return False
        last[0] = root.val
        return fun(root.right)
    return True
return fun(root)
```

四个细节：
- **`float('-inf')`** 哨兵：首节点一定 > -inf，天然放行；且能处理 val = -2³¹（int 下限）；
- **`>=`**：严格递增，相等（重复值）必须 False；
- **剪枝** `if fun(root.left) is False: return False`：左子树一错立刻停；
- **列表包 last**：Python 闭包若要修改外层普通变量需 `nonlocal`，用列表元素 `last[0]` 是更简单的替代。

## 四、另一种标准解：上下界法（递归传范围）

```python
def isValidBST(self, root, lo=float('-inf'), hi=float('inf')):
    if not root:
        return True
    if not (lo < root.val < hi):      # 当前节点必须落在 (lo, hi)
        return False
    return (self.isValidBST(root.left, lo, root.val) and   # 左子树：上界收紧为 root.val
            self.isValidBST(root.right, root.val, hi))     # 右子树：下界收紧为 root.val
```

**思想**：把"根的限制"一路传导给子树——左子树的所有节点必须 < 根（上界收紧），右子树必须 > 根（下界收紧）。跨层违反就被天然抓住（6 的左子树 3 时，上界已收紧到 6，3 不满足 3 > 5 的路径约束）。

## 五、复杂度

- 时间：O(n)
- 空间：O(h)（递归栈）

## 六、一刷 vs 二刷

- 一刷（9-14）：中序递增法 last_list 哨兵，WA 1 次（区间边界）→ AC ×2；
- 二刷（10-22）：秒掉一次 AC，四细节全对——**"中序递增"心法已内化**。

## 七、关联题目

| 套路 | 相关题 |
|------|--------|
| 中序递增 | **94 中序遍历**（上一题）、230 第 K 小（中序数到 K） |
| 上下界传导 | 98 的变形证明、538 累加树（反中序） |
| 全局约束 | 二叉树的序列化 297（先序带 Null 标记） |

## 八、一句话记住

> **验证 BST = 中序严格递增（last 哨兵 -inf + >= 判重 + 剪枝）；或上下界法 lo<val<hi 逐层收紧；千万别只查局部"左<根<右"——会漏跨层违反。**