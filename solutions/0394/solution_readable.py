# -*- coding: utf-8 -*-
"""
第 394 题 字符串解码 · 标准双栈版（与用户单栈版结果一致，1 万组对拍 0 差异）

设计：栈存 (重复次数, 进入本层之前的字符串) 元组 + 一个 cur 变量。
    '['  → 压栈当前进度，重置 cur（下钻一层）
    ']'  → 弹栈合并：cur = 前缀 + cur * 次数（返回上一层）
递归版 = 本版的隐式栈版本（调用栈即状态栈）。
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []          # (重复次数, 前缀)
        cur = ""
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)          # 多位数字累加
            elif c == '[':
                stack.append((num, cur))         # 下钻：保存进度
                num, cur = 0, ""
            elif c == ']':
                last_num, prefix = stack.pop()   # 返回上层：合并
                cur = prefix + cur * last_num
            else:
                cur += c                          # 普通字母
        return cur