# Created by Chono-Hina at 2026/09/17 16:38
# leetgo: 1.4.18
# https://leetcode.cn/problems/min-stack/

from typing import *
from leetgo_py import *

# @lc code=begin

class MinStack:

    def __init__(self):
        self.stack = []
        self.time_min_val = [float('inf')]     # 辅助栈：第 i 层 = 主栈前 i 层的最小值；inf 哨兵免判空

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.time_min_val.append(min(value, self.time_min_val[-1]))   # 新最小 = min(旧最小, value)

    def pop(self) -> None:
        self.stack.pop()
        self.time_min_val.pop()                # 同步弹出（回到上一时刻的最小值）

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.time_min_val[-1]           # O(1) 直接看辅助栈顶

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
