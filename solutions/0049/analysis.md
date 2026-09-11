# 49. 字母异位词分组 · 解题解析

> 本题由用户独立完成（初稿写在 `test.py`，整理归档）。

## 一句话思路

两个字符串互为字母异位词 ⟺ **排序后完全相同**。于是把「排序后的字符串」当作哈希表的 key，value 收集同组的所有原串，最后返回所有分组。

## 实现

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_dict = {}
        for each_str in strs:
            sorted_str = "".join(sorted(list(each_str)))
            if sorted_str_dict.get(sorted_str) is None:
                sorted_str_dict[sorted_str] = [each_str]
            else:
                sorted_str_dict[sorted_str].append(each_str)
        return list(sorted_str_dict.values())
```

- **时间复杂度**：O(n · k log k)，n 为字符串个数，k 为字符串平均长度（每个串排序耗时 k log k）
- **空间复杂度**：O(n · k)，存储全部分组结果
- **优点**：思路直白、代码短，是最经典的解法

## 易错点

1. **不能把列表当 key**：`sorted(each_str)` 返回 list，list 不可哈希，必须 `"".join(...)` 转成字符串
2. **空串与单字符**：`[""]` → key 为 `""`，能正确分组（已由用例 2 覆盖）
3. **顺序无关**：分组之间、组内元素的顺序都不要求一致（见下方判题说明）

## 关于判题：本地测试 vs 在线提交（本题重要经验）

| 环节 | 结果 | 说明 |
|------|------|------|
| leetgo 本地测试 | ❌ Case 1 Wrong answer | 本地做**严格字符串比对**，要求输出与样例逐字符一致 |
| 力扣在线测试/提交 | ✅ Accepted | 官方对本题用 **special judge**，接受任意分组顺序 |

> 结论：**顺序无关的题目以在线判题为准**。本题本地报错属于比对机制差异，代码本身正确。
> 后续遇到类似"答案可任意顺序"的题目（如三数之和、全排列等），不必被本地红字吓到。

## 本题考点

| 考点 | 内容 |
|------|------|
| 哈希表分组 | 用「规范化的 key」把等价元素聚到一起 |
| 字符串排序 | `sorted` + `join` 构造规范化 key |

## 提交记录

- 在线测试：3/3 Accepted
- 正式提交：**129/129 通过**（16 ms / 21.7 MB）
