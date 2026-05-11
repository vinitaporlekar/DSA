from typing import List

class Solution:
    def ContainsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    
sol = Solution()
print(sol.ContainsDuplicate([1,2,3,4]))
