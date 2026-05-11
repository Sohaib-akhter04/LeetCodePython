# 136.Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict={}
        for index,num in enumerate(nums):
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for key, value in dict.items():
            if value == 1:
                return key
        
                


solution=Solution()
nums = [2,2,1]
print(solution.singleNumber(nums))
