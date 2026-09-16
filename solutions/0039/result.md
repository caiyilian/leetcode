# 39. 组合总和 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 39. 组合总和（Combination Sum）· 中等（回溯家族第 4 题） |
| 链接 | https://leetcode.cn/problems/combination-sum/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 160/160 用例通过** |
| 运行时间 | **3 ms（击败 94%）** |
| 内存 | 19.3 MB（击败 76%） |

## 三次提交的演进（用户完整自驱优化闭环）

| 版本 | 实现 | 实测（target=60） | 备注 |
|------|------|-----------------|------|
| v1 | `sum(path)` 每层重算 + 从头枚举 + continue | 84.37 ms | 慢 2.6 倍 |
| v2 | `now_sum` 参数累加（O(1)） | 51.78 ms | 快 1.6 倍 ✅ |
| **v3（定稿）** | + `sort` + `range(index)` + **break 剪枝** | **33.65 ms** | **追平标准版（1.06 倍）** ✅ |

**用户自悟的关键**：`now_sum + n > target` 在排序后直接 **break**（后面更大全超）而非 continue——"一次判断终结整层"。

## 定稿（用户 v3）

```python
class Solution:
    def combinationSum(self, candidates, target):
        result = []
        length = len(candidates)
        candidates.sort()
        def fun(path, index=0, now_sum=0):
            if now_sum > target:
                return
            if now_sum == target:
                result.append(path.copy())
            for i in range(index, length):
                n = candidates[i]
                if now_sum + n > target:
                    break              # 排序 + 剪枝
                path.append(n)
                fun(path, i, now_sum+n)  # 防重复组合（只用 i 之后）+ 可重复用 i
                path.pop()
        fun([])
        return result
```

## 验证

- 对拍 **5000 组随机 vs 标准 remaining 版 0 不一致**（v1/v2/v3 均验证）；
- 性能：target=60 比值 1.06、target=120 比值 1.07（与标准版几乎一致）；
- 官方样例全对：`[2,3,6,7],7 → [[2,2,3],[7]]`、`[2,3,5],8 → 3 组`、`[2],1 → []`。

## 复杂度

- 时间 O(答案数×深度)（剪枝后远小于 2ⁿ 枚举）；空间 O(深度) 递归栈。

## 设计要点

- **防重复组合**：`fun(path, i)` 传 i 不传 i+1——允许重复选同一个数，但只往后走（组合无序）；
- **break 剪枝**：排序是 break 的前提（后面更大必超）；
- `now_sum` 累加传参 vs `sum(path)` 重算：O(1) vs O(深度)。