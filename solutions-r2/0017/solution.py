"""17. 电话号码的字母组合（二刷）——回溯枚举（O(4^n × n)/O(n) 标准解）

用户 AC 版（2026-10-29 15:41 提交 757607534，守卫版一次通过，0ms/19.1MB）
- 回溯：逐位枚举每个数字对应的字母，path 收集当前组合，到底加入 result
-   ⚡ 空串守卫 if not digits: return []（力扣约定，不加会返回 [""]）
- 注意：嵌套函教 path=[] 可变默认参数——本次 append/pop 严格配平所以没炸，
-     但坏习惯，建议 def fun(i, path=None) + 体内初始化（见 208 教训）
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        hash_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        length = len(digits)

        def fun(i, path=[]):          # ⚠ 可变默认参数（本次配平无恙，规范写法见下）
            if i == length:
                result.append("".join(path))
                return path
            for c in hash_map[digits[i]]:
                path.append(c)
                path = fun(i + 1, path)
                path.pop()
            return path

        fun(0)
        return result


# ===== 规范写法参考（避免可变默认参数） =====
class SolutionClean:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        m = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def dfs(i, path):
            if i == len(digits):
                res.append("".join(path))
                return
            for c in m[digits[i]]:
                path.append(c)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))   # ['ad','ae','af','bd','be','bf','cd','ce','cf']
    print(s.letterCombinations("2"))    # ['a','b','c']
    print(s.letterCombinations(""))     # []
    print(s.letterCombinations("7"))    # ['p','q','r','s']