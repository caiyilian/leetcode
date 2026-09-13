# 234. 回文链表 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 234. 回文链表（Palindrome Linked List）· 简单 |
| 链接 | https://leetcode.cn/problems/palindrome-linked-list/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 93/93 用例通过** |
| 运行时间 | 44 ms（leetgo 提交；链表题 Python 提交密集区） |
| 内存 | 41.6 MB（击败 88%） |

## 解法

用户独立的**三段式组合拳**（206 反转 + 快慢指针找中点）：

1. **快慢指针找中点**：`while p_fast and p_fast.next: p_fast = p_fast.next.next; p_slow = p_slow.next`
   - 偶数长度：快指针走到 `None`，慢指针在后半段起点；
   - 奇数长度：快指针 `next` 为 None 停下，慢指针在正中节点；
2. **反转后半段**（复用 206 的三指针反转）；
3. **逐节点比较**：头指针 vs 反转后的后半段头，不等即 False。

- 时间 **O(n)**：找中点 O(n) + 反转 O(n) + 比较 O(n)；
- 空间 **O(1)**：只用了指针变量（进阶要求：O(1) 额外空间 满足）。

## 用户踩坑记录（奇数长度）

提交过程中一次出错：**奇数长度链表时快指针的 `next` 是 None 就得停下**——`while p_fast and p_fast.next` 同时覆盖两种情况（偶数停在 None、奇数停在末节点），理解了这个就能写对。

对拍 5 万组随机（奇偶长度混合）+ 回文专项边界全过。