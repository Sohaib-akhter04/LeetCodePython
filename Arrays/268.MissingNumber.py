#268. Missing Number
#Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
from typing import List 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum=n*(n+1)/2
        act_sum=sum(nums)
        self.missingNumber=exp_sum-act_sum
        return int(self.missingNumber)

nums=[0,1]
solution=Solution()
print(solution.missingNumber(nums))