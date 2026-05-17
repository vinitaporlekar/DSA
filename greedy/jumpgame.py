from typing import List
class Solution:
    def  jumpGame(self, nums: List[int])-> int:
        goal =0

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= goal:
                goal =i
        return True if goal == 0 else False
        

sol = Solution()
print(sol.jumpGame(nums = [2,3,1,1,4]))
