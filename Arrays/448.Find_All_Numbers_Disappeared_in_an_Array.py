#448. Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index=abs(num)-1
            nums[index]=-abs(nums[index])
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res

solution=Solution()
nums = [4,3,2,7,8,2,3,1]
solution.findDisappearedNumbers(nums)