"""461. 汉明距离（二刷）——逐位比较（用户 AC 版）

用户二刷（2026-11-04 11:55 提交 758535820，AC 一次通过，0ms/19.1MB）
- 逐位比较法：while x or y 循环，比较最低位 x%2 != y%2 计数，然后双双右移
- 本质：汉明距离 = 两个数二进制中"不同的位的个数" = (x ^ y) 中 1 的个数
- 写法对比：逐位比较（无位运算技巧，O(log n) 位）vs x^y 后 bit_count（更简洁）
"""


# ===== 用户 AC 版（逐位比较） =====
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        while x or y:                      # 直到两个数都归零
            if x % 2 != y % 2:             # 最低位不同 → 该位不同
                count += 1
            x = x >> 1                     # 右移看下一位
            y = y >> 1
        return count


# ===== 参考1：异或 + bit_count（更简洁，338 的直接应用） =====
class SolutionXor:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()         # 不同位 = 1，数 1 的个数


# ===== 参考2：异或 + 逐个数位（不依赖 Python 内置） =====
class SolutionXorManual:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        cnt = 0
        while z:
            cnt += z & 1
            z >>= 1
        return cnt


if __name__ == "__main__":
    s = Solution()
    print(s.hammingDistance(1, 4))      # 2（1=01, 4=100 → 两位不同）
    print(s.hammingDistance(3, 1))      # 1
    print(s.hammingDistance(5, 5))      # 0