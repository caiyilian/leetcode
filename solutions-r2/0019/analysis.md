# 19. 删除链表的倒数第 N 个结点 · 解析（二刷）

## 一、核心思路：快慢指针（"延迟 n 拍"）

删倒数第 n 个，本质是"找到它的前驱，然后 `prev.next = 待删.next`"。难点：**单链表只能从头走，不知道链表多长**。

快慢指针解法：**fast 先走 n 步**，然后两个指针**同步一步一步走**。fast 先出发 n 步，所以当 fast 走到 None（末尾）时，slow 恰好**落后 n 步 = 停在待删节点**，再用一个 `prev` 记 slow 的前驱：

```
dummy -> 1 -> 2 -> 3 -> 4 -> 5     n=2
                ↑slow           ↑fast（先走2步）
                    → 同步走 →  fast 到 None 时 slow 停在 4，prev 停在 3
prev.next = slow.next  →  3 直接指向 5 → 删掉 4
```

**为什么叫"一遍扫描"**：fast 总共走 len 步（先 n 步 + 同步 len-n 步），全程没有回退。

## 二、dummy 哨兵为什么必需

**删头节点**（n == len）时：fast 先走 n 步直接到 None，`while p_fast` 不进入，slow 停在 head（待删），此时**待删节点没有前驱**。

- 无 dummy：`prev = None`，想删头只能特判 `if prev is None: return head.next`——一不留神就写错（WA 版直接 `return prev` 把整链删了）；
- 有 dummy：`prev = dummy` 起步，**头节点也有"虚拟前驱"**，`prev.next = p_slow.next` 统一处理，`return dummy.next` 统一返回新头。

**一句话**：dummy 让"删除头节点"退化成普通删除，**消灭所有头节点特判**。

## 三、代码（AC 版）

```python
dummy = ListNode(0)
dummy.next = head
p_fast = head
p_slow = head
prev = dummy
for _ in range(n):
    p_fast = p_fast.next          # ① fast 先走 n 步
while p_fast:
    p_fast = p_fast.next
    prev = prev.next              # ② prev 跟着 slow 走（始终是 slow 的前驱）
    p_slow = p_slow.next
prev.next = p_slow.next           # ③ 删掉 slow
return dummy.next
```

注意 `prev = prev.next` 而不是 `prev = p_slow`——两者等价（prev 始终比 slow 慢一拍），但 `prev = prev.next` 在 slow 前进一步前先记录，语义更清楚。

## 四、复杂度

- 时间：O(n)，一趟扫描
- 空间：O(1)

## 五、一刷 vs 二刷

- 一刷（9-13）：一遍快慢指针 + dummy，AC ×3（**一刷就写了 dummy**）；
- 二刷（10-19）：v1 想精简掉 dummy → 删头翻车（返回 None）；v2 加回 dummy → AC。**dummy 的"消特判"价值，通过一次 WA 彻底理解。**

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| dummy 哨兵统一头处理 | **2 两数相加**、21 合并两个有序链表、23 合并 K 个、25 K 个一组翻转 |
| 快慢指针（延迟 n 拍） | 141/142 环形链表（步长 2/1）、234 回文链表（找中点） |
| 删除节点 | 237 删除链表中的节点（没有 head，直接换值）、203 移除链表元素 |

## 七、一句话记住

> **删除倒数第 N 个 = fast 先走 n 步 + 双指针同步走到 fast=None，slow 即待删点；dummy 哨兵让 prev 永不落空，删头也统一处理——"删节点先上 dummy"。**
