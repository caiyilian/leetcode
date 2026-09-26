# 621. 任务调度器 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 621. 任务调度器（Task Scheduler）· 中等（v2 新增题 · 贪心 + 桶） |
| 链接 | https://leetcode.cn/problems/task-scheduler/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-26 |
| 最终提交 | ✅ **ACCEPTED - 72/72 用例通过**（leetgo 复提交） |
| 运行时间 | 43 ms |
| 内存 | 20.5 MB |

## 解法（用户贪心 + 桶公式）

```python
class Solution:
    def leastInterval(self, tasks, n):
        count_dict = defaultdict(int)
        max_len = 0
        for t in tasks:
            count_dict[t] += 1
            max_len = max(max_len, count_dict[t])     # 最高频次数 max
        cnt_max = 0
        for value in count_dict.values():
            if value == max_len:
                cnt_max += 1                          # 同频最高任务个数
        return max((max_len - 1) * (n + 1) + cnt_max, len(tasks))
```

## 核心：贪心 + 桶（用户要求讲透概念）

### 贪心 = 先排最难的

最高频任务（假设 A 出现 max 次）是**瓶颈**——它占的格数决定了总时长下界。**先把 A 排好，其他任务都能在 A 的冷却空位里插**。局部最优（先排最频）→ 全局最优（时长短）。

### 桶 = 任务 + n 个冷却位

相同任务必须隔 n 个不同任务 → A 每出现一次，后面至少要留 n 个非 A 位置。

```
桶（n+1 格）：
| A | 冷却 | 冷却 |     ← A 的每个"周期"

max 个 A → (max-1) 组完整桶 + 最后一批
总时间 = (max-1) × (n+1) + cnt_max
         ↑每桶格数         ↑最后一批（cnt_max 个同频最高任务并排）
```

**推演示例** `tasks=[A,A,A,B,B,B], n=2`：

```
桶1：A B B     （3 格）
桶2：A B B     （3 格）
最后：A B      （cnt_max=2：A、B 都是最高频，并排收尾）
总时间 = (3-1)×3 + 2 = 8
```

### clamp：`max(公式, len(tasks))`

如果其他任务足够多，能**填满**所有冷却位还富余 → 根本没有空闲 → 总时间就是 `len(tasks)`（不需要等冷却）。

## 验证

- 对拍 **2000 组 vs 模拟贪心调度 0 不一致**；
- 样例：`[A,A,A,B,B,B],n=2→8`、`[A,A,A,B,B,C],n=1→6`、`[A,A,A],n=0→3`。

## 复杂度

- 时间 **O(n)**（n = 任务数，统计一遍）；空间 O(1)（任务类型 ≤ 26）。