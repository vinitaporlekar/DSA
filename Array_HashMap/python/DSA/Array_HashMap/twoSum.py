from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prevMap ={}

        for i ,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return (prevMap[diff] , i)
            prevMap[n] =i
        return
    
nums = [1,2,3,4]
target = 3
sol = Solution()
print(sol.twoSum(nums,target))
