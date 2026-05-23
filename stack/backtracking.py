class Solution:
    def parenthsis(self, n : int) -> List[str]:
        res = []
        stack =[]

        def backtracking(openN, closedN):
            if closedN == openN == n:
                res.append("".join(stack))

                return
            
            if openN < n:
                stack.append("(")
                backtracking(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtracking(openN, closedN +1)
                stack.pop()

        backtracking(0,0)
        return res
    
    
n = (3)
sol = Solution()
print(sol.parenthsis(n))
