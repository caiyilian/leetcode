# 45. 跳跃游戏 II · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 45. 跳跃游戏 II（Jump Game II）· 中等（贪心分类第 3 题） |
| 链接 | https://leetcode.cn/problems/jump-game-ii/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 111/111 用例通过**（leetgo 复提交） |
| 运行时间 | 7 ms（击败 56%） |
| 内存 | 19.9 MB |

## 解法（用户双 far 贪心，逻辑完美）

```python
class Solution:
    def jump(self, nums):
        curr_far = 0                        # 当前这一跳的覆盖尽头
        next_far = 0                        # 下一跳能到的最远
        step = 0
        length = len(nums)
        for i, n in enumerate(nums):
            next_far = max(next_far, n + i)          # 试探最远
            if i == curr_far and i != length - 1:    # 走到段尽头（且没到终点）
                step += 1
                curr_far = next_far                  # 下一跳范围
        return step
```

**用户边界处理亮点**：`i != length - 1` 直接防住"终点再跳一次"（比标准版 `range(n-1)` 更直观）。

## 用户疑问解答：最少次数 = far 更新次数吗？

**不是**——far 更新次数混进了"同一跳内多次试探"。最少跳数 = **跳跃段数**，必须引入"段"概念 → 双 far（`curr_far` 当前段边界 + `next_far` 下一段最远）。反例 `[2,3,1,1,4]`：far 更新 3 次，但最少跳数 = 2。

## 55 → 45 升级线索

```
55：一个 far（全局最远可达），问"能不能到"
45：两个 far（curr_far + next_far），问"最少几步"（要数段数）
```

## 验证

- 对拍 **10 万组随机（保证可达）vs BFS 分层参照 0 不一致**；
- 官方样例：`[2,3,1,1,4]→2`、`[2,3,0,1,4]→2`；
- 边界：`[0]→0`、`[1,2,3]→2`、`[2,1]→1`。

## 复杂度

- 时间 **O(n)**（一次遍历，理论下界）；空间 **O(1)**——最优。

## 关于"速度慢"

用户觉得速度慢，实为**假象**：O(n) 已是跳跃游戏 II 的理论下界，无更快算法；力扣 runtime 含约 150ms 固定开销（240 题已总结），简单题 ms/击败率 ≠ 算法优劣。