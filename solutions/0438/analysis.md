# 438. 找到字符串中所有字母异位词 · 解析

## 题目简述

给定两个字符串 `s` 和 `p`，找到 `s` 中所有 `p` 的**异位词**（字母相同、顺序不同）的子串，返回这些子串的起始索引。

示例：`s = "cbaebabacd", p = "abc"` → `[0, 6]`。

## 核心思路：滑动窗口 + 计数数组

异位词的判断 = **两个字符串的字母计数完全相同**（与顺序无关）。所以：

- 固定窗口长度 = `len(p)`，统计窗口内 26 个字母的出现次数；
- 窗口计数数组 == p 的计数数组 ⟺ 是异位词。

**匹配判断**：不能直接排序/哈希字符串，唯一可靠的判断是逐字母计数相等。

## 定稿解法（增量维护 + 剪枝）

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(s)
        length_p = len(p)
        count_list = list(map(p.count, "abcdefghijklmnopqrstuvwxyz"))
        index_list = []
        last_match = False
        count_list_s = None
        for i in range(length - length_p + 1):
            if last_match:
                if s[i+length_p-1] == s[i-1]:
                    index_list.append(i)
                    last_match = True
                else:
                    last_match = False
                    count_list_s[ord(s[i-1])-97] -= 1
                    count_list_s[ord(s[i+length_p-1])-97] += 1
                continue
            if count_list_s is None:
                count_list_s = list(map(s[i: i+length_p].count, "abcdefghijklmnopqrstuvwxyz"))
            else:
                count_list_s[ord(s[i-1])-97] -= 1
                count_list_s[ord(s[i+length_p-1])-97] += 1
            if count_list_s == count_list:
                index_list.append(i)
                last_match = True
            else:
                last_match = False
        return index_list
```

### 算法逻辑

1. `count_list`：p 的 26 字母计数（只统计一次）；
2. `count_list_s`：当前窗口的计数，**首次窗口全量统计，之后增量维护**——窗口滑动只改变两个位置：
   - 移出最左字符 `s[i-1]`：对应计数 **-1**；
   - 新进最右字符 `s[i+length_p-1]`：对应计数 **+1**；
3. 比较 `count_list_s == count_list` 判断匹配；
4. **last_match 剪枝**：上一窗口匹配时，若新进字符 == 移出字符，计数不变 → 本窗口必匹配，直接记录；
5. **推理优化**：last_match 且首尾字符不同 → `新计数 = P - a + b ≠ P`，本窗口必不匹配，跳过比较只更新计数。

### 复杂度

- 时间 **O(n + 26·n) = O(n)**：单遍扫描，每步两次索引 O(1) + 一次列表比较 O(26)（常数）；
- 空间 **O(26)**：两个固定长度计数数组。

## 从 O(n·p) 到 O(n)：增量维护是灵魂

| 版本 | 每窗口做的事 | 总复杂度 |
|------|------------|---------|
| v1 | 切片 + 26 次 count（每次 O(p)） | **O(26·n·p)** |
| v3 | 同上 + last_match 剪枝（只在连续命中时生效） | 最优情况才 O(n) |
| **v4** | 只改两个计数位置 + 列表 == 比较 | **O(n)** ✅ |

**核心认知**：窗口滑动前后只有"最左移出 + 最右进入"两个字符变化，中间 p-2 个字符一个没动——**复用上一次的结果，不要从零统计**。这就是滑动窗口增量维护的全部秘密。

## 考点

- 滑动窗口固定长度版（窗口长度恒为 len(p)，左右指针同步移动）
- 字母计数的"异位词判等"（顺序无关的字符串比较 = 计数比较）
- **增量维护**（只更新变化的两个位置）
- 剪枝与推理（last_match + 首尾不同必不匹配）
- 与第 3 题对比：第 3 题是可变窗口（找最长），本题是固定窗口（找所有匹配位置）

## 顺带教训

v1 字母表 `"abcdefghijklmnopgrstuvwxyz"` 拼错（重复 g、缺 q）——因为比较的字符串等长，碰巧不影响正确性，但属于"运气好"，务必用正确的 26 字母序。