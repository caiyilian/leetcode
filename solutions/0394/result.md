# 394. 字符串解码 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 394. 字符串解码（Decode String）· 中等（栈分类第 3 题） |
| 链接 | https://leetcode.cn/problems/decode-string/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-17 |
| 最终提交 | ✅ **ACCEPTED - 34/34 用例通过**（leetgo 复提交） |
| 运行时间 | **0 ms（击败 100%）+ 内存击败 86%** |

## 解法（用户自创：单栈混合版）

```python
class Solution:
    def decodeString(self, s):
        result = []
        c26 = set(chr(i+97) for i in range(26))
        number = set(str(i) for i in range(10))
        num_str = ""
        for c in s:
            if c in c26:  result.append(c)          # 字母入栈
            elif c in number: num_str += c           # 多位数字累加
            elif c == '[':
                result.append(num_str); result.append("["); num_str = ""
            else:  # ]：弹到 [ 拼 each_str，再 × 数字
                each_str = ""
                while True:
                    c2 = result.pop()
                    if c2 == "[": break
                    each_str = c2 + each_str
                each_str = each_str * int(result.pop())
                result.append(each_str)
        return "".join(result)
```

**设计特点**：数字串/字母/`[` **全存一个栈**（单栈混合），`]` 时 while 弹到 `[` 再拼乘——与标准"双栈 (次数, 前缀) 元组"（solution_readable.py）结果一致（1 万组随机嵌套对拍 0 差异）。

## 验证

- 对拍 **1 万组随机嵌套表达式（含 3 层嵌套）vs 独立递归版 0 不一致**；
- 官方样例：`3[a]2[bc]→aaabcbc`、`3[a2[c]]→accaccacc`、`2[abc]3[cd]ef→abcabccdcdcdef`、`abc3[cd]xyz→abccdcdcdxyz`；
- 边界：空串、`100[leetcode]`（多位数字）、深嵌套 `3[z]2[2[y]pq4[2[jk]e1[f]]]ef` 全对。

## 复杂度

- 时间 **O(结果长度)**（重复拼接的下限）；空间 **O(结果长度)**——满足题目要求。

## 关键点（用户全踩中）

1. **多位数字**：num_str 累加（`100[leetcode]`）；
2. **嵌套**：内层 `]` 先算完入栈，外层 `]` 继续乘（`3[a2[c]]`）；
3. **`[` 时数字与分隔符都入栈**，`]` 时按序弹回。