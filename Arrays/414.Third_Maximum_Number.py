#414. Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new_num=list(set(nums))
        
        n=len(new_num)
        for i in range(n):
            for j in range(n-i-1):
                if new_num[j]<new_num[j+1]:
                    new_num[j],new_num[j+1]=new_num[j+1],new_num[j]
        print(new_num)


        if len(new_num)>2:
            return new_num[2]
        else:
            return new_num[0]
        
        
                    




nums=[2,2,3,1]
solution=Solution()
print(solution.thirdMax(nums))
