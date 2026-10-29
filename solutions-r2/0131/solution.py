"""131. 分割回文串（二刷）——回溯切割 + 双指针判回文（O(n×2^n)/O(n) 标准解）

用户 AC 版（2026-10-29 22:05 提交 757685641，一次通过，59ms/32.9MB）
- start 切割回溯：每层从 start 尝试切到 i（子串 s[start:i+1]），是回文就切，递归 i+1
- 收集条件：start 走到头（切完整个串）→ path 就是一种分割
- isPa 双指针判回文（O(n)）；力扣约束 s 非空，空串守卫是防御性的
"""

from typing import List


def isPa(s: str) -> bool:      # 双指针判回文
    length = len(s)
    p1 = 0
    p2 = length - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        result = []
        length = len(s)

        def fun(path, start=0):
            if start >= length:                    # 切完整个串 → 收集
                result.append(path.copy())
                return path                        # ⚠ 注意：这里没 return 会继续走 for！
            for i in range(start, length):
                if isPa(s[start:i + 1]):           # 子串是回文才切
                    path.append(s[start:i + 1])
                    path = fun(path, i + 1)        # 从切割点后继续
                    path.pop()
            return path

        fun([])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))    # [["a","a","b"],["aa","b"]]
    print(s.partition("a"))      # [["a"]]
    print(s.partition("aba"))    # [["a","b","a"],["aba"]]
    print(s.partition("aaaa"))   # 8 种