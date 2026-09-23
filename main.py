
import time
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:


if __name__ == "__main__":
    s = "()())()"
    # 1. 创建类的实例
    solution = Solution()
    # 2. 调用方法
    start = time()
    result = solution.removeInvalidParentheses(s)
    print((time()-start) * 1000)
    
    # 3. 打印结果
    print(result)