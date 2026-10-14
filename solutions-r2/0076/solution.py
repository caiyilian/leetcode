"""76. 最小覆盖子串（二刷）——滑动窗口（双解法）

解法一：用户 AC 版（2026-10-14 14:49 提交 754751770）
  思路：右扩到满足 → 左缩到刚好不满足 → 记录。每次用 equ() 全扫字符集判断。
解法二：标准 missing 计数版（推荐）——维护"还缺几个字符"，O(1) 判断 → 真 O(n)
"""

from collections import defaultdict
from typing import List


# ========== 解法一：用户 AC 版（equ 全扫判断）==========
def equ(count_dict, now_dict):
    eq = True
    for key, value in count_dict.items():
        if now_dict[key] < value:
            eq = False
            break
    return eq


class SolutionUser:
    def minWindow(self, s: str, t: str) -> str:
        count_dict = {}
        for c in t:
            count_dict[c] = count_dict.get(c, 0) + 1
        now_dict = defaultdict(int)
        left = 0
        result = ""
        min_length = float('inf')
        for right in range(len(s)):
            now_dict[s[right]] += 1
            if equ(count_dict, now_dict):
                while True:
                    now_dict[s[left]] -= 1
                    left += 1
                    if equ(count_dict, now_dict) is False:
                        now_len = right - left + 2
                        if now_len < min_length:
                            result = s[left - 1: right + 1]
                            min_length = now_len
                        break
        return result


# ========== 解法二：标准 missing 计数版（推荐，O(n)）==========
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        missing = len(t)                # ★ 还缺多少个字符（含重复）
        left = 0
        result = ""
        min_len = float('inf')
        for right, c in enumerate(s):
            if need[c] > 0:             # 这个字符正是 t 需要的 → 缺口减一
                missing -= 1
            need[c] -= 1                # 窗口计数（负数 = 超出需要，不影响缺口）
            while missing == 0:         # ★ 缺口清零 = 完全覆盖 → 尝试缩左
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left: right + 1]
                if need[s[left]] == 0:  # left 退出窗口：若它正好卡在缺口边界，缺口加回
                    missing += 1
                need[s[left]] += 1
                left += 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))  # BANC
    print(s.minWindow("a", "aa"))               # ""
    print(s.minWindow("a", "a"))                # "a"