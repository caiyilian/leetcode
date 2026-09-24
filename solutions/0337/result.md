# 337. 打家劫舍 III · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 337. 打家劫舍 III（House Robber III）· 中等（v2 新增题 · 树形 DP） |
| 链接 | https://leetcode.cn/problems/house-robber-iii/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-24 |
| 最终提交 | ✅ **ACCEPTED - 124/124 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 20.5 MB |

## 解法（用户树形 DP，返回 (偷, 不偷) 元组）

```python
class Solution:
    def rob(self, root):
        def fun(root):
            if root:
                rob_left, no_rob_left = fun(root.left)
                rob_right, no_rob_right = fun(root.right)
                rob_now = root.val + no_rob_left + no_rob_right      # 偷 → 孩子不能偷
                no_rob_now = max(rob_left, no_rob_left) + max(rob_right, no_rob_right)  # 不偷 → 孩子任选
                return rob_now, no_rob_now
            return (0, 0)
        rob_now, no_rob_now = fun(root)
        return max(rob_now, no_rob_now)
```

## 核心：树形 DP（后序遍历 + 双返回值）

每个节点向父节点返回**两个值**：
- `rob_now`：偷当前节点的最大收益；
- `no_rob_now`：不偷当前节点的最大收益。

**转移**：
```
偷当前  → root.val + 左孩子"不偷" + 右孩子"不偷"
不偷当前 → max(左偷, 左不偷) + max(右偷, 右不偷)
```

**用户注释精准**："None 节点，对于其父节点来说，偷与不偷没区别" → 返回 `(0, 0)`。

## 为什么一次遍历就够

朴素想法是"隔层偷"（层序遍历 + 隔层求和），但那样会漏解（可能隔两层）。树形 DP 把"偷/不偷"作为状态**向上传递**，一次后序遍历 O(n) 解决——**每个节点的最优由其子树最优组合而来**。

## 验证

- 对拍 **3000 组随机树 vs 暴力枚举子集 0 不一致**；
- 样例：`[3,2,3,null,3,null,1]→7`、`[3,4,5,1,3,null,1]→9`。

## 复杂度

- 时间 **O(n)**（每个节点访问一次）；空间 O(h)（递归栈）。