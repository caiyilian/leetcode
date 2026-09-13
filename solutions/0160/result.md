# 160. 相交链表 · 提交结果

| 项目 | 结果 |
|------|------|
| 题目 | 160. 相交链表（Intersection of Two Linked Lists）· 简单 |
| 链接 | https://leetcode.cn/problems/intersection-of-two-linked-lists/ |
| 提交账号 | tomoya-w9@leetcode.cn |
| 提交日期 | 2026-09-13 |
| 最终提交 | ✅ **ACCEPTED - 41/41 用例通过** |
| 运行时间 | 169 ms（leetgo 提交；链表题 Python 提交密集区，击败率参考价值有限） |
| 内存 | 37.4 MB |

## 解法

用户看讲解视频后独立写出**双指针换边法**（教科书最优解）：

```python
pA, pB = headA, headB
while pA != pB:
    pA = pA.next if pA else headB   # A 走完换到 B 开头
    pB = pB.next if pB else headA   # B 走完换到 A 开头
return pA
```

- **时间 O(m+n)**：两个指针各走最多两条链全长；
- **空间 O(1)**：只有两个指针——双最优，优于"set 记节点"（O(n) 空间）；
- 对拍 3 万组随机（相交/不相交/空链表）0 错误，边界全过。

## 踩坑记录

leetgo 对本题生成的模板**方法签名错误**（`getIntersectionNode(intersectVal, listA, listB, skipA, skipB)` 5 参数，标了 "manual question, generated test code may be incorrect"）——力扣实际签名是 `getIntersectionNode(headA, headB)` 2 参数，需手动修正方法签名与 `__main__` 调用。