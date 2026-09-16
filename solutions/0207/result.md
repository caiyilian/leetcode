# 207. 课程表 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 207. 课程表（Course Schedule）· 中等（图论：拓扑排序） |
| 链接 | https://leetcode.cn/problems/course-schedule/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 54/54 用例通过** |
| 运行时间 | 7 ms（击败 37%） |
| 内存 | 20.3 MB |

## 两次提交的演进（用户自驱优化：O(V²) → O(V+E)）

| 版本 | 思路 | 复杂度 | 说明 |
|------|------|--------|------|
| v1（粗暴版） | while 每轮全扫找入度 0，学到无进展为止 | **O(V²)** | 正确（5 万组对拍 0 差异）但每轮 O(V) 全扫 |
| **v2（定稿）** | 队列版 Kahn：入度 0 入队 → 出队学掉 → 依赖者入度-1 → 变 0 入队 | **O(V+E)** | 标准答案 |

## v2 定稿（用户自驱写出，102 快照分层技巧迁移）

```python
class Solution:
    def canFinish(self, numCourses, prerequisites):
        count_dict = defaultdict(int)        # 入度表
        need_dict = defaultdict(list)        # 出边表
        for back, before in prerequisites:
            count_dict[back] += 1            # back 的入度 +1
            need_dict[before].append(back)
        q = deque([i for i in range(numCourses) if count_dict[i] == 0])  # 初始入度 0 入队
        learned = 0
        while q:
            for _ in range(len(q)):          # 快照分层（102 技巧）
                num = q.popleft()
                learned += 1
                for need in need_dict[num]:
                    count_dict[need] -= 1
                    if count_dict[need] == 0:
                        q.append(need)       # 入度变 0 = 下一轮可学
        return learned == numCourses
```

**核心认知（用户优化时悟到）**："入度变 0"靠**事件触发**（前置刚被学掉）而不是每轮**全表扫描**——用队列维护"当前可学"，谁减到 0 谁入队。

## 验证

- 对拍 **5 万组随机图 vs 标准 Kahn BFS 0 不一致**（v1/v2 均验证）；
- 官方样例全对：`2, [[1,0]]→True`、`2, [[1,0],[0,1]]→False`（环）、`4, [[1,0],[2,0],[3,1],[3,2]]→True`；
- V=10000 链式图实测 **4.56ms**（v1 同规模是秒级）。

## 复杂度

- v2：时间 **O(V+E)**（每节点入队一次 + 每条边一次）；空间 **O(V+E)**（表）。

## 踩坑记录

- test.py 的 defaultdict 未 import（本地 NameError）——归档版已补 `from collections import defaultdict, deque`。