# 3. 无重复字符的最长子串 · 解析

## 题目简述

给定一个字符串 `s`，请你找出其中**不含有重复字符的最长子串**的长度。

示例：`"abcabcbb"` → 3（`"abc"`）；`"bbbbb"` → 1（`"b"`）；`"pwwkew"` → 3（`"wke"`）。

## 核心套路：滑动窗口

维护一个窗口 `[start, i]`（当前不重复的连续子串），右边界 `i` 不断向右扩展：

- 新字符**不在窗口里** → 扩展成功，窗口变长，更新答案；
- 新字符**已在窗口里** → 冲突，把 `start` 跳到"该字符上一次出现位置 + 1"，窗口跳转收缩。

**关键优化（跳转而不是一格一格挪）**：用 dict 记录每个字符**最后一次出现的位置**，冲突时左边界直接跳到 `重复位置 + 1`——窗口收缩是 O(1) 的，整个算法单遍 O(n)。

## 定稿解法

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        max_length = 1
        start = 0
        now_length = 1
        index_dict = {s[0]: start}
        for i, c in enumerate(s[1:]):
            index_repeat = index_dict.get(c)
            if index_repeat is not None and index_repeat >= start:
                start = index_repeat + 1
                now_length = i + 2 - start
            else:
                now_length += 1
                max_length = max(now_length, max_length)
            index_dict[c] = i + 1
        return max(now_length, max_length)
```

### 逻辑细节

- `index_dict[c]`：字符 c **最后一次**出现的位置（每次遇到都更新）；
- 冲突判定 `index_repeat >= start`：**即使字符在 dict 里，如果它上次出现在窗口左侧（< start），也不算窗口内冲突**——这是这题最容易漏的边界（dict 里"有"不等于"窗口里有"）；
- `now_length = i + 2 - start`：窗口 `[start, i+1]` 的长度（`enumerate(s[1:])` 的 i 对应原串下标 i+1）；
- 结束时 `max(now_length, max_length)`：兜底最后一段窗口（可能一直没有重复，答案还没更新过）。

### 复杂度

- 时间 **O(n)**：单遍扫描，dict 查询 O(1)；
- 空间 **O(字符集大小)**：dict 最多存 128 个 ASCII 字符（或 26 个小写字母），**不随 n 增长**——严格说是 O(min(n, 字符集))。

## 常数优化三连（v1 → v2，实测快 40%）

| 优化点 | v1（慢） | v2（快） | 原理 |
|--------|---------|---------|------|
| 哈希查询次数 | `get()` + `dict[i]` 同一键查 2~3 次 | `get()` 一次取出复用 | 哈希查找有常数成本，少查一次是一次 |
| 字符访问 | `for i in range(n-1)` + `s[i+1]` | `for i, c in enumerate(s[1:])` | 循环变量直接拿到字符，免索引 + 免 +1 |
| 答案更新时机 | 冲突时才更新 max | 不冲突时更新 max | 冲突频繁的数据（如 `bbbb...`）避免每轮走重分支 |

## 考点

- **滑动窗口**（双指针的"窗口版"：右扩 + 左收缩，两个边界各自单调右移，总移动 O(n)）
- **dict 记录"最后出现位置"实现 O(1) 跳转**（比 set 版"一格一格删"更优）
- **边界易错点**：`dict` 里有 ≠ 窗口里有（要用 `>= start` 判断）；空串/单字符特判；最后一段窗口兜底
- 与 128 题的容器选型呼应：只需"在不在"用 set；需要"在哪"（位置）用 dict

## 同类题预告

滑动窗口分类还有 438（找到字符串中所有字母异位词）、76（最小覆盖子串，困难）等——都是"窗口 + 计数"的套路，本窗口/字符频次统计的思路可复用。
