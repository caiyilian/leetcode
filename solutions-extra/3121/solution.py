"""3121. 统计特殊字母的数量 II（Count the Number of Special Characters II）· 非 HOT100 独立归档

用户 AC 版（2026-11-10 11:47 提交 759428861，303ms/20.6MB；WA×3 → AC×2 演进）
- 状态机思路：对每个字母维护「小写先于大写且不违反规则」的状态
- meet_small：见过该小写（大写还没出现）
- result：已确认特殊（小写全出现在首个大写之前）
- error：已作废（大写后还有小写 / 先大写后小写）——命中直接跳过
- 时间 O(n)、空间 O(1)（set 上限 26），达理论下界
"""


# ===== 用户 AC 版（三集合状态机） =====
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        meet_small = set()   # 遇到过的小写字母（尚未见其大写）
        result = set()       # 已确认特殊的字母
        error = set()        # 已作废的字母（大写后还有小写，或先大写后小写）
        small_range = (ord("a"), ord("z"))

        for c in word:
            c_lower = c.lower()
            if c_lower in error:          # 已作废，跳过
                continue

            if small_range[0] <= ord(c) <= small_range[1]:
                # 当前是小写字母
                meet_small.add(c)
                if c in result:
                    # 该字母大写已出现过、现在又出现小写 → 违反"小写全在大写前" → 作废
                    result.remove(c)
                    error.add(c)
            else:
                # 当前是大写字母
                if c_lower in result:     # 已确认特殊，不必重复处理
                    continue
                if c_lower in meet_small: # 先见过小写 → 首个大写出现，确认特殊
                    result.add(c_lower)
                else:
                    # 还没见过小写就出现大写 → 之后的小写必然在其后 → 作废
                    error.add(c_lower)

        return len(result)


# ===== 官方解法参照：位置比较法（首尾位置） =====
class SolutionPos:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}   # 每个字母第一次大写出现的位置
        last_lower = {}    # 每个字母最后一次小写出现的位置
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                low = ch.lower()
                if low not in first_upper:
                    first_upper[low] = i
        ans = 0
        for c in set(last_lower) & set(first_upper):
            if first_upper[c] > last_lower[c]:   # 最后的小写在首个大写之前
                ans += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSpecialChars("aaAbcBC"))    # 3
    print(s.numberOfSpecialChars("abc"))        # 0
    print(s.numberOfSpecialChars("AbBCab"))     # 0
    print(s.numberOfSpecialChars("aabAbcBC"))   # 3