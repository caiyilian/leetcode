# Created by Chono-Hina at 2026/09/17 16:38
# leetgo: 1.4.18
# https://leetcode.cn/problems/min-stack/

from typing import *
from leetgo_py import *

# @lc code=begin

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

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MinStack()

    for i in range(1, len(ops)):
        match ops[i]:
            case "push":
                method_params = split_array(params[i])
                value: int = deserialize("int", method_params[0])
                obj.push(value)
                output.append("null")
            case "pop":
                obj.pop()
                output.append("null")
            case "top":
                ans = serialize(obj.top())
                output.append(ans)
            case "getMin":
                ans = serialize(obj.getMin())
                output.append(ans)

    print("\noutput:", join_array(output))
