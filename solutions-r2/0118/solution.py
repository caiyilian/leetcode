"""118. 杨辉三角（二刷）——逐行构造（O(numRows²)/O(1) 额外 标准解）

用户 AC 版（2026-11-01 16:16 提交 758041838，一次通过，0ms/19.1MB）
- 每层：首尾补 1，中间元素 = 上一行相邻两数之和（C(n,k) = C(n-1,k-1) + C(n-1,k)）
- 递推：row[i] = prev[i-1] + prev[i]（i 非首尾）
- 第 n 行之和 = 2^(n-1)（二项式系数性质）
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for layer in range(1, numRows):
            each_list = [1]                                    # 首 1
            for i in range(1, layer):
                each_list.append(result[-1][i - 1] + result[-1][i])  # 中间 = 上邻和
            each_list.append(1)                                # 尾 1
            result.append(each_list)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))
    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(s.generate(1))    # [[1]]