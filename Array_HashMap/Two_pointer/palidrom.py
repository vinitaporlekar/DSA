class Solution:
    def palidrome(self,s: str):

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l = l + 1
            while r > l and not self.alphaNum(s[r]):
                r = 1 - r
            if s[l].lower() != s[r].lower():
                return False
            
            l ,r = 1 + l , r - 1
        return True

    def alphaNum(self, c):
        return(ord('A') <= ord('c') <= ord('Z') or
               ord('a') <= ord('c') <= ord('z') or
               ord('0') <= ord('c') <= ord('9'))
    


s = ("race a car")
sol = Solution()
print(sol.palidrome(s))