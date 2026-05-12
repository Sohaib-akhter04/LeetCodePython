# 217. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for index,num in enumerate(nums):
            if num in dict:
                return True
            else:
                dict[num]=1
        return False
        
solution=Solution()
nums = [1,2,3]
print(solution.containsDuplicate(nums))