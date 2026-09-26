# 301. 删除无效的括号 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 301. 删除无效的括号（Remove Invalid Parentheses）· **困难**（v2 新增题 · BFS） |
| 链接 | https://leetcode.cn/problems/remove-invalid-parentheses/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-26 |
| 最终提交 | ✅ **ACCEPTED - 129/129 用例通过**（leetgo 复提交） |
| 运行时间 | 91 ms（击败 49%） |
| 内存 | 19.3 MB |

## ⚠️ 失败记录（用户要求记录，两次）

| 提交 | 结果 | 原因 |
|------|------|------|
| 751527042 | **RE** | `invaid`/`next_level` 辅助函数没定义（代码框漏贴） |
| 751527073 | **WA** | `is_valid` 里 `elif c == ")"` 写成 `else` → **字母也算右括号**，含字母串误判 |
| 751527225 | AC | `elif` 修正 |
| 751528490 | AC | **优化：`next_level` 只删括号**（`if s[i] in "()"`，跳过字母） |

## 解法（用户 BFS + set 去重，标准）

```python
def invaid(s):
    cnt = 0
    for c in s:
        if c == "(":
            cnt += 1
        elif c == ")":
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0

def next_level(s):
    s_set = set()
    for i in range(len(s)):
        if s[i] in "()":                  # 只删括号，跳过字母
            s_set.add(s[:i] + s[i + 1:])
    return s_set

class Solution:
    def removeInvalidParentheses(self, s):
        level = {s}
        while level:
            valid = [each for each in level if invaid(each)]
            if valid:
                return valid              # 第一个合法层 = 最少删除
            next_level_set = set()
            for x in level:
                next_level_set.update(next_level(x))
            level = next_level_set
        return [""]
```

## 核心：BFS 逐层删括号

```
第 0 层：原串 → 无合法
第 1 层：删 1 个括号的所有可能 → 有合法？有 → 返回（最少删除）
第 2 层：再删 1 个 → ...
```

**BFS 性质**：逐层扩展，第一个出现合法串的层 = 删最少括号。`level` 用 **set 去重**（删不同位置得到同一串时避免重复 + 防重复计算）。

## 奇偶洞察（用户自悟）

合法括号串长度必为偶数；原串奇数 → 删掉的也是奇数 → 合法结果只可能在第 1、3、5 层。**但 is_valid 自动过滤**（奇数层 cnt 不可能为 0），代码无需显式判断。

## 验证

- 对拍 **4000 组（纯括号 2000 + 含字母 2000）vs 暴力枚举 0 不一致**；
- 样例：`"()())()"→["(())()","()()()"]`、`"(a)())()"→["(a())()","(a)()()"]`、`")("→[""]`。

## 复杂度

- 时间 O(2^n)（最坏每层翻倍，set 去重 + 早停通常快）；空间 O(2^n)。