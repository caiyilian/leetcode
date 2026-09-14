# 138. 随机链表的复制 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 138. 随机链表的复制（Copy List with Random Pointer）· 中等 |
| 链接 | https://leetcode.cn/problems/copy-list-with-random-pointer/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-14 |
| 最终提交 | ✅ **ACCEPTED - 19/19 用例通过** |
| 运行时间 | 55 ms（leetgo 提交） |
| 内存 | 20 MB（击败 18%） |

## 解法

用户独立的**哈希映射两遍法**（138 标准答案之一）：

1. **第一遍**：建新链表（只连 `next`），同时记录 `原节点 → 新节点` 映射表；
2. **第二遍**：`value.random = hash_dict.get(key.random, None)`——把原链的 random 引用翻译成新链节点。

- 时间 **O(n)**、空间 **O(n)**（哈希表）；
- **深拷贝三验证点全过**（5 万组随机含自指/交叉 random）：
  ① 值序列一致 ② 结构（random 相对索引）一致 ③ 新节点完全独立、random 全指向新链节点。

## 版本记录（本目录）

| 文件 | 版本 |
|------|------|
| `solution.py` | **哈希映射两遍法**（本次定稿，用户版） |
| `solution_readable.py` | **节点交错法**（O(1) 额外空间，满足 follow-up；5 万组与哈希法等价） |

## 踩坑记录

- leetgo manual question：模板 `__main__` 用 `ListNode` 反序列化（实际是 `Node`），本地测试必然失败——**以在线为准**（19/19 通过）。