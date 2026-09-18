# 763. 划分字母区间 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 763. 划分字母区间（Partition Labels）· 中等（贪心分类收官题） |
| 链接 | https://leetcode.cn/problems/partition-labels/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-18 |
| 最终提交 | ✅ **ACCEPTED - 118/118 用例通过**（leetgo 复提交） |
| 运行时间 | **3 ms（击败 93%）——速度其实很快！** |
| 内存 | 19.2 MB |

## 解法（用户标准贪心，去掉一处死代码）

```python
class Solution:
    def partitionLabels(self, s):
        hash_dict = {}
        for i, c in enumerate(s):        # ① 记录每个字母最后位置
            hash_dict[c] = i
        start = end = 0
        result = []
        for i, c in enumerate(s):        # ② 维护片段右边界，走到 end 切段
            end = max(end, hash_dict[c])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
```

**用户原版有一处死代码**：`if hash_dict[c] > end: end = hash_dict[c]`——上一行 `end = max(end, hash_dict[c])` 已保证该条件恒假，删掉不影响结果（归档时已清理）。

## 与 55/45 的"最远"骨架同源

```
55 ：far = max(far, i + nums[i])     ← 最远可达
45 ：curr_far / next_far 分段         ← 走到边界跳一段
763：end = max(end, last[c])         ← 最远结束位置，走到 end 切一段
```

**全是"维护一个最远值，走到边界就切"的贪心**——763 只是把"最远"定义成"字母最后出现位置"。

## 验证

- 对拍 **2 万组随机字符串（验证片段合法性 + 总长度）vs 标准版 0 不一致**；
- 官方样例：`ababcbacadefegdehijhklij→[9,7,8]`、`eccbbbbdec→[10]`（全部一个片段）、`a→[1]`。

## 复杂度

- 时间 **O(n)**（两次遍历）；空间 O(1)（最多 26 个字母）。

## 🏆 贪心分类 4/4 全通关（121 → 55 → 45 → 763）