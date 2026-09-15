# 437. 路径总和 III · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 437. 路径总和 III（Path Sum III）· 中等 |
| 链接 | https://leetcode.cn/problems/path-sum-iii/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-15 |
| 最终提交 | ✅ **ACCEPTED - 130/130 用例通过** |
| 运行时间 | 7 ms（击败 64%） |
| 内存 | 20 MB（击败 74%） |

## ⚡⚡⚡ 重点复习标记（机考前一天必看）

> 用户指定：**机考前一天重点复习本题**。复习时看 analysis.md，重点：① 查差公式 `cur_sum - targetSum` ② `{0:1}` 虚拟起点 ③ **回溯撤销防跨子树** ④ 单节点路径自动覆盖。

## 解法：前缀和 + 回溯（用户思路，标准最优解 O(n)）

```python
class Solution:
    def pathSum(self, root, targetSum):
        self.count = 0
        prefix = {0: 1}                      # ① 虚拟起点：前缀和为 0 出现 1 次
        def dfs(node, cur_sum):
            if not node:
                return
            cur_sum += node.val              # ② 当前前缀和 = 根到本节点的路径和
            self.count += prefix.get(cur_sum - targetSum, 0)   # ③ 查差
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1       # ④ 记录当前前缀和
            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
            prefix[cur_sum] -= 1             # ⑤ 回溯撤销（防止跨子树——关键！）
        dfs(root, 0)
        return self.count
```

## 关键认知（用户提问精华）

1. **单节点算路径**：路径 = 任意节点到子孙（单节点是特例）——查差命中"父节点前缀和"自动覆盖，无需特判；
2. **`{0:1}` 的作用**：让"从根开始"的路径有虚拟起点可查（根本身 = targetSum 时 cur_sum - targetSum = 0）；
3. **回溯撤销的意义**：前缀和只能来自当前路径上的祖先——不撤销会把跨子树断路径算进去；
4. **与 560 的关系**：437 = 560 的树版本，"查差值而非枚举对"（560 已标复习，两题配套复习）。

## 验证

- 对拍 **5 万组随机树 × 随机 targetSum vs 暴力枚举 0 错误**；
- 官方样例全对（3 / 3）；
- solution_readable.py 收录暴力参照版（O(n²)，仅验证/理解用）。

## 复杂度

- 时间 **O(n)**（每节点一次 + 哈希 O(1)）；
- 空间 **O(n)**（哈希表）+ O(h) 递归栈。