import math
from typing import List

class Solution:
    def kokoBanana(self, piles : List[int], h : int) -> int:
        l , r= 1, max(piles)
        res = r

        while l <= r:
            hours = 0

            for p in piles:
                k = (l + r)//2
                hours = hours + math.ceil(p / k)

            if hours<= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k +1
        return res
    
piles = (3,6,7,11)
h = 8
sol = Solution()
print(sol.kokoBanana(piles, h))