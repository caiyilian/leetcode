# 230. 二叉搜索树中第 K 小的元素 · 解析

## 题目简述

给定一个二叉搜索树（BST）的根节点 `root` 和整数 `k`，返回其中**第 k 小**的元素（1-indexed）。

## 核心套路：BST 中序 = 升序（98/108/230 三兄弟收官）

**BST 的性质**（98 验证过、108 构造过）：**中序遍历结果就是升序序列**。所以"第 k 小" = "中序第 k 个"——不需要排序、不需要堆，中序遍历边走边数即可。

## 演进史：v1 全收集 → v2 剪枝（用户自己完成的优化）

### v1（7ms）：纯中序全收集

```python
def fun(root):
    if root:
        fun(root.left)
        result.append(root.val)
        fun(root.right)
fun(root)
return result[k-1]
```

遍历完整棵树再取第 k 个——正确，但做了大量无用功（k 很小时，后 n-k 个节点白跑）。

### v2（0ms）：剪枝提前终止（定稿）

```python
def fun(root, k):
    if root:
        fun(root.left, k)                # 左子树：必须走完（中序宿命）
        if len(result) == k:             # ★ 剪枝：收集够就刹
            return
        result.append(root.val)
        fun(root.right, k)               # 右子树：被上面的 return 跳过
```

**剪枝能力边界**（关键认知）：

```
✅ 能剪：右子树 + 所有向上的右分支（收集够了，后面全部跳过）
❌ 剪不掉：左子树（必须先走完左边才知道够不够——这是中序的宿命）
```

所以 v2 复杂度是 **O(k + h)**（不是 O(k)）：k 小时 ≈ O(h)，k 大时 ≈ O(n)。实测 k=1 时 6.55ms → 0.00ms。

## 进阶一：迭代版（彻底的 O(h + k)）

递归版剪不掉左子树，是因为递归栈里压着"未访问的祖先"；迭代版**控制入栈时机**，弹出第 k 个立即返回：

```python
class Solution:
    def kthSmallest(self, root, k):
        stack, cur = [], root
        while stack or cur:
            while cur:                      # 走到最左，路径入栈
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()               # 弹出 = 中序第 1, 2, 3... 个
            k -= 1
            if k == 0:
                return cur.val              # 数到第 k 个 → 停（真正 O(h+k)）
            cur = cur.right
        return -1
```

## 进阶二：follow-up（"频繁插入删除 + 多次查询"怎么优化）

给每个节点**维护左子树节点数 size**：第 k 小 = 左子树 size + 1 的节点，利用 BST 有序性二分定位，**单次查询 O(h)**，无需遍历。插入/删除时 O(h) 更新 size。面试加分项，知道思路即可（力扣 230 不需实现，450 删除节点时再看）。

## 复杂度对比

| 版本 | 时间 | 空间 |
|------|------|------|
| v1 全收集 | O(n) | O(n)（result） |
| **v2 递归剪枝（定稿）** | **O(k + h)** | O(h) 递归栈 + O(k) result |
| 迭代版 | O(h + k) | O(h) |
| size 维护（follow-up） | O(h) 每次查询 | O(n) 存 size |

## 考点

- BST ⇔ 中序升序（三兄弟：98 检查 / 108 构造 / 230 计数）
- **剪枝优化思维**（"够就停"——中序里只要前 k 个）
- 递归剪枝 vs 迭代终止（能力边界差异）
- 提前终止的经典模式（这道题是 124/437 等"数数/求和类"树的预演）

## 易错点

1. 剪枝判断放 append **之前**（放之后会多收一个且右子树照跑）；
2. 不要用 `set`/`sort`（BST 中序就是有序的，别绕路）；
3. k 是 1-indexed（`result[k-1]`，不是 `result[k]`）；
4. 递归版剪枝只省右子树——面试被追问复杂度时答 O(k+h)，别答 O(k)。