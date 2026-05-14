from typing import List
class Solution:
    def containerWater(self, height: List[int])-> int:
        res =0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r -1) * min(height[l], height[r])
            res = max(res,area)

            if height[l]< height[r]:
                l = l+1
            else:
                 r= r-1
        return res
    
height=[1,8,6,2,5,4,8,3,7]
    
sol = Solution()
print(sol.containerWater(height))
            