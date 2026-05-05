# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps={}
        for i,num in enumerate(nums):
            complement=target-num
            if complement in num_maps:
                return [num_maps[complement],i]
            num_maps[num]=i
        
    
nums=[2,7,11,15]
target=9
sol=Solution()
print(sol.twoSum(nums,target))
