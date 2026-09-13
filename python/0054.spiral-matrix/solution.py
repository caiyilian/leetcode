# Created by Chono-Hina at 2026/09/13 11:28
# leetgo: 1.4.18
# https://leetcode.cn/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        use_dir_index = 0
        result = [matrix[0][0]]
        
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        count = 1
        dir_max = [n, m, 0, 0] # 'right', 'down', 'left', 'up'的边界
        length = m*n
        while True:
            if use_dir_index==0:
                
                if j < dir_max[0]-1:
                    j += 1
                    result.append(matrix[i][j])
                    count += 1
                else:
                    dir_max[use_dir_index-1] += 1
                    use_dir_index = (use_dir_index + 1) % 4
                    # break
            elif use_dir_index==1:
                if i < dir_max[1] - 1:
                    i += 1
                    result.append(matrix[i][j])
                    count += 1
                else:
                    dir_max[use_dir_index-1] -= 1
                    use_dir_index = (use_dir_index + 1) % 4
                    # break
            elif use_dir_index==2:
                if j > dir_max[2]:
                    j -= 1
                    result.append(matrix[i][j])
                    count += 1
                else:
                    dir_max[use_dir_index-1] -= 1
                    use_dir_index = (use_dir_index + 1) % 4
            else:
                if i > dir_max[3]:
                    i -= 1
                    result.append(matrix[i][j])
                    count += 1
                else:
                    dir_max[use_dir_index-1] += 1
                    use_dir_index = (use_dir_index + 1) % 4
            if count == length:
                break
        return result
        

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
