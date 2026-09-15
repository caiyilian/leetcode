# 199. 二叉树的右视图 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 199. 二叉树的右视图（Binary Tree Right Side View）· 中等 |
| 链接 | https://leetcode.cn/problems/binary-tree-right-side-view/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 217/217 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.2 MB |

## 今天两次提交的演进（用户自行优化，代码已从力扣拉取确认）

| 时间 | 版本 | 思路 | 成绩 |
|------|------|------|------|
| 16:07 | v1 | **层队列版**：list1 存"整层节点"，取每层最右 | Accepted 0ms |
| 16:14 | **定稿** | **deque 快照版**：单队列 + `len(q)` 快照分层，`for` 结束后 `node` 恰是本层最右 | Accepted 0ms |

**v1 → 定稿的变化（用户主动采纳 deque 优化）**：`list1.pop(0)`（O(层数)，列表头弹出移动元素）→ `deque.popleft()`（O(1)）+ 省掉"存层"结构。

## 定稿（力扣最终提交版）

```python
class Solution:
    def rightSideView(self, root):
        from collections import deque
        if not root:
            return []
        q = deque([root])
        result = []
        while q:
            for _ in range(len(q)):        # len(q) 快照 = 当前层节点数
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(node.val)        # for 结束 node = 本层最右 ✅
        return result
```

**妙点**：`for` 循环走完后 `node` 恰好是本层最后一个节点——直接当右视图值收进结果，连"存层"都省了。

## 验证

- 对拍 **5 万组随机树 0 不一致**（v1 与定稿等价，双双验证）；
- 官方样例全过：`[1,2,3,null,5,null,4]` → `[1,3,4]`、`[1,null,3]` → `[1,3]`、`[]` → `[]`。

## 复杂度

- 时间 **O(n)**（每节点一次）；空间 **O(w)**（队列最多存一层，w = 最大层宽）。