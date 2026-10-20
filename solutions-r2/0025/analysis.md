# 25. K 个一组翻转链表 · 解析（二刷）

## 一、核心思路：按组"分离 → 反转 → 拼接"

困难题，但 = 已做过的组件拼装：**206 反转链表（反转单组）+ dummy（统一头处理）+ 循环推进（逐组处理）**。

```
dummy → [1 → 2 → 3] → 4 → 5      k=3
        ↑prev  组[p1..p_last]   ↑p_next
反转组内：
dummy → [3 → 2 → 1] → 4 → 5
prev.next = 3（新头），1.next = 4，prev 前进到 1
再处理下一组…
```

## 二、三个"接缝"必须全部维护（本次踩坑核心）

反转一组后，链上有三个地方要重接，漏一个就掉链：

| 接缝 | 做什么 | 漏掉的后果 |
|------|--------|-----------|
| **前驱 → 新头** | `prev.next = 反转后新头` | ★ 整组悬空丢失（本次的坑） |
| **新尾 → 后继** | `新尾.next = p_next` | 后面的链丢失 |
| **前驱指针推进** | `prev = 新尾` | 下一轮起点错乱 |

**连接守恒原则**：链表操作中，每改动一个节点的 next，都要问一句"现在还有谁指着我？"——特别是**前驱**，它是最容易忘记维护的指针。

## 三、代码骨架（用户 AC 版）

```python
while prev.next:
    p1 = prev.next                # 组头
    p_last = p1
    for _ in range(k - 1):        # 找组尾；不足 k 个 → break
        p_last = p_last.next
        if p_last is None:
            break
    else:                          # for-else：没 break 说明凑够一组
        p_next = p_last.next       # 记住下一组起点
        p_last.next = None         # 断链（便于反转）
        p1, p_last = reverse_node(p1)   # 反转组内，返回 (新头, 新尾)
        prev.next = p1             # ★ 接缝1：前驱接新头
        p_last.next = p_next       # 接缝2：新尾接后继
        prev = p_last              # 接缝3：前驱前进
        continue
    break                          # 剩余不足 k 个 → 保持原样
return dummy.next
```

**细节**：
- `for...else`：Python 特有——for 循环没被 break 打断才执行 else 块，用来表达"凑够 k 个才反转"非常贴切（用户自创写法）；
- `p_last.next = None` 其实可省（reverse_node 用 next_node 先存后继再改，天然断链），但显式断链思路更直白；
- 不足 k 个的尾组：`for` 里 break → else 不执行 → 外层 `break` → 保持原样返回。

## 四、复杂度

- 时间：O(n)——每节点反转一次
- 空间：O(1)——迭代 + 局部反转（递归版会 O(n/k) 栈深，本题进阶要求 O(1)，用迭代）

## 五、一刷 vs 二刷

- 一刷（9-14）：`p_prev.next, p_now_last = self.reverse_list(p_prev.next)` 一步双更新（新头+新尾），按提示独立完成；
- 二刷（10-20）：拆成 `p1, p_last = reverse_node(p1)` + **`prev.next = p1`**，先漏后补——**连接守恒原则通过一次 WA 彻底理解**。

## 六、关联题目

| 套路 | 相关题 |
|------|--------|
| 反转子链（206） | 24 两两交换（k=2 特例）、92 反转链表 II（区间反转） |
| dummy 头处理 | 19 / 21 / 23 / 24（头会变的链表全家桶） |
| for-else / 先判断后动手 | 24（while True + break 元知识）、142（步数可以是 0） |

**25 = 206（反转）+ 24（分组）+ dummy**，困难题是简单题的组合。

## 七、一句话记住

> **K 个一组翻转 = 每轮找 [p1..p_last] → 断链反转 → 三个接缝全部重接（prev→新头、新尾→后继、prev 前进）；漏 `prev.next = 新头` 整组悬空——"每改一个 next，先问谁还指着我"。**
