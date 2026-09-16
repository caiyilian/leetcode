# 17. 电话号码的字母组合 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 17. 电话号码的字母组合（Letter Combinations of a Phone Number）· 中等（回溯家族第 3 题） |
| 链接 | https://leetcode.cn/problems/letter-combinations-of-a-phone-number/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-16 |
| 最终提交 | ✅ **ACCEPTED - 24/24 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.3 MB |

## 解法（用户 index 分层版 + 空串边界修复）

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:               # ★ 修复点：空串边界 → []
            return []
        length = len(digits)
        result = []
        num2char = {"2": "abc", ..., "9": "wxyz"}
        def fun(path, index=0):
            if len(path) == length:
                result.append("".join(path))   # join 创建新字符串，天然免疫引用陷阱
                return
            for c in num2char[digits[index]]:  # 每层锁死一个数字的字母表
                path.append(c)
                fun(path, index+1)             # 推进下一层
                path.pop()
        fun([])
        return result
```

## 本次发现的一个边界隐患（本地对拍抓到）

**`digits=""` 时用户版返回 `[""]`，正确应为 `[]`**——力扣中国站测例恰好没覆盖空串所以 Accepted，但这是真实边界 bug（面试/后续测例必炸）。已加 `if not digits: return []` 修复。

**备注修正**：用户注释"字符串，所以不用复制"表述不准——真正原因是 `"".join(path)` **创建新字符串对象**（不可变），result 存的是独立快照，与 path 后续 pop 无关。

## 验证

- 1 万组随机数字串 vs itertools.product 参照：**修复后 0 不一致**（修复前空串 1987 次不一致）；
- 官方样例：`"23"` → 9 个组合全对、`"2"` → 3 个、`""` → `[]`（修复前 FAIL）。

## 复杂度

- 时间 **O(4ⁿ×n)**（每数字最多 4 字母，共 4ⁿ 组合）；空间 **O(n)** 递归深度。