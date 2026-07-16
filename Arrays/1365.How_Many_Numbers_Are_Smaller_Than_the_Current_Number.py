# 1365. How Many Numbers Are Smaller Than the Current Number
# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
from typing import List
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         n=len(nums)
#         numCount=[0]*n
#         for i in range(n):
#             for j in range(n):
#                 if i!=j and nums[i]>nums[j]:
#                     numCount[i]+=1
#         return numCount
    # Alternate solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        result=[]
        n=len(nums)
        for num in nums:
            count[num]+=1
        for i in range(1,101):
            count[i]+=count[i-1]
        for num in nums:
            if num==0:
                result.append(0)
            else:
                result.append(count[num-1])
        return result

nums = [8,1,2,2,3]
solution=Solution()
print(solution.smallerNumbersThanCurrent(nums))