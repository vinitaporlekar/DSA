from typing import List
class Solution:
    def dailyTemp(self, temperatures: List[int]) -> int:
        res=[0] * len(temperatures)
        stack =[]

        for i ,t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stacktemp,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res
    
temperatures = (73,74,75,71,69,72,76,73)
sol = Solution()
print(sol.dailyTemp(temperatures))