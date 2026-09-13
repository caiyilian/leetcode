# 19. 删除链表的倒数第 N 个结点 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 19. 删除链表的倒数第 N 个结点（Remove Nth Node From End of List）· 中等 |
| 链接 | https://leetcode.cn/problems/remove-nth-node-from-end-of-list/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 208/208 用例通过** |
| 运行时间 | **0 ms（击败 100%）** |
| 内存 | 19.1 MB（击败 42%） |

## 版本演进（用户 2 版）

| 版本 | 思路 | 复杂度 | 说明 |
|------|------|--------|------|
| v1 | 两遍扫描：先数长度 → 走 length-n-1 步删节点 | O(n)/O(1) | 简单直接，需 `length == n` 特判删头 |
| **v2（定稿）** | **一遍快慢指针**：fast 先走 n 步 → 同步走，fast 到尾时 slow 在待删节点前一个 | **O(n)/O(1)** | 无 dummy，`p_fast is None` 特判删头 |

另归档 `solution_readable.py`：标准 dummy 哨兵版（删头无需特判，面试推荐写法）。

## 验证

- 两版各对拍 5 万组随机 + 全边界（删头/删尾/单节点）0 错误；
- 用户 v2 的关键细节：`while p_fast.next` 停在 fast 到**最后一个**节点（slow 在待删前一个）——与标准写法 `while p_fast`（fast 到 None）等效，自己调出来的等价变体。