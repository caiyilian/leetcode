"""763. 划分字母区间（二刷）——贪心区间扩展（O(n)/O(1) 标准解）

用户 AC 版（2026-11-01 15:25 提交 758031541，一次通过，4ms/19.2MB）
- ① 第一遍扫描：end_dict[字母] = 该字母最后一次出现的位置
- ② 第二遍扫描：维护当前段的右边界 end = max(end, end_dict[s[i]])
   当 i == end：说明当前段内所有字母已经覆盖完最后出现位置 → 这一段可以切割
- 核心：段内任意字母的最后出现位置决定段的右边界，贪心取 max 即"最晚的收尾点"
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # ① 记录每个字母最后出现的位置
        end_dict = {}
        for i in range(len(s)):
            end_dict[s[i]] = i

        # ② 贪心扩展右边界，i 撞到 end 就切一段
        end = 0
        start = 0
        results = []
        for i in range(len(s)):
            end = max(end, end_dict[s[i]])   # 当前段右边界 = 段内字母最晚出现处
            if i == end:                     # 扫描到右边界 → 段内字母不会出现在后面
                results.append(end - start + 1)
                start = end + 1
        return results


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))   # [9, 7, 8]
    print(s.partitionLabels("eccbbbbdec"))                 # [10]