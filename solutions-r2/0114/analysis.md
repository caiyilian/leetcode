# 114. 二叉树展开为链表 · 解析（二刷）

## 一、核心思路：递归返回 (头, 尾) 拼接

把树展平成 right 链（前序顺序）。递归的**强大约定**：

```
fun(root) → (展平链头, 展平链尾)
```

```
    1
   / \
  2   5
 / \   \
3   4   6
```
左子树 2 展平 = 2→3→4，返回 (2, 4)
右子树 5 展平 = 5→6，返回 (5, 6)
拼接：4.right = 5；1.right = 2；1.left = None
结果：1→2→3→4→5→6 ✓

## 二、代码骨架（用户 AC 版）

```python
def fun(root):
    if root:
        root.left, left_last = fun(root.left)      # 左链 (头,尾)
        root.right, right_last = fun(root.right)   # 右链 (头,尾)
        if root.left:
            left_last.right = root.right           # ① 左链尾接右链头
            root.right = root.left                 # ② 根的右 = 左链头
            root.left = None                       # ③ 清空左
            if right_last is None:                 # ★ 右子树空 → 链尾修正为左链尾
                right_last = left_last
        return root, right_last if right_last is not None else root
    return None, None
```

## 三、⚡ WA→AC：返回 (头,尾) 的"尾"必须自洽

**复现**：`[1,2,None,3]`（节点 2 只有左孩子 3）。处理节点 2 时右子树为空：

```python
root.right, right_last = fun(None)   # right_last = None
# 拼接后：2.right = 3，但返回的"尾"却是 2（不是 3！）
return root, right_last if right_last is not None else root   # 返回 (2, 2)
```

父节点 1 拿到左链尾=2，`2.right = root.right`（1 的右子树）→ **3 被甩出链**，输出 `[1,2]`。

**修复**：右子树为空时，整条链的尾应该是**左链尾**：

```python
if right_last is None:
    right_last = left_last    # 链尾 = 左链尾（此时整链 = 左链）
```

**通用原则**：递归返回 (头,尾) 时，**"尾"必须指向展平链真正的最后一个节点**——子树为空时最容易出错，要主动问"这棵子树展平后最后一个是谁"。

## 四、复杂度

- 时间：O(n)
- 空间：O(h)（递归栈）

## 五、一刷 vs 二刷

- 一刷（9-15）：三版演进（收集 → 找尾 O(n²) → 沿 right 链 O(n)/O(1)），**深树栈溢出教训**；
- 二刷（10-24）：自创 (头,尾) 递归一次思路成型，WA 一次修复——**返回尾的约定必须自洽**。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| 返回 (头,尾) 递归 | 25 K 个一组翻转链表（reverse 返回 (新头,新尾)）、430 扁平化多级链表 |
| 原地改树 | 226 翻转二叉树、二叉树序列化 297 |
| 前序顺序 | 144 前序遍历、105 前序建树 |

## 七、一句话记住

> **二叉树展平 = 递归返回 (头,尾)：左链尾接右链头、根接左链头、清左；⚠️ 右子树为空时链尾=左链尾——返回"尾"必须永远指向真正的最后一个节点。**