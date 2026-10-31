"""155. 最小栈（二刷）——双栈：辅助栈存最小值索引（O(1) 全操作 / O(n) 空间 最优解）

用户 AC 版（2026-10-31 16:38 提交 757914223，一次通过，147ms/31.7MB）
- ⚡ 索引版（比标准值版更省）：辅助栈存"最小值在 stack 中的索引"而非值
- push：只在新值 < 当前最小值时 push 索引（重复最小值不撑大辅助栈）
- pop：被弹出的是当前最小值的索引才 pop 辅助栈（自动"恢复"上一个最小值）
- getMin：stack[min_stack[-1]]（O(1) 不遍历）
"""

from typing import List


# ===== 用户 AC 版（索引辅助栈） =====
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        # 只存遇到过的最小值在 stack 中的索引

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(len(self.stack) - 1)
        else:
            if value < self.stack[self.min_stack[-1]]:
                self.min_stack.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()
        pop_index = len(self.stack)          # 弹出后 stack 的新长度 = 被弹出元素的原下标
        if self.min_stack[-1] == pop_index:  # 弹掉的恰好是当前最小值的索引 → 辅助栈同步弹
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_stack[-1]]


# ===== 标准"值辅助栈"版参考（更常见，面试也认） =====
class MinStackStd:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, v: int) -> None:
        self.stack.append(v)
        if not self.min_stack or v <= self.min_stack[-1]:   # 注意 <=：重复最小值也存
            self.min_stack.append(v)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:          # 弹出的是当前最小值才同步弹
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())    # -3
    s.pop()
    print(s.top())       # 0
    print(s.getMin())    # -2