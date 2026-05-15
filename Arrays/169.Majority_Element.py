#169. Given an array nums of size n, return the majority element.The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Explanation:
# - Count how many times each number appears using a dictionary.
# - Since a majority element is guaranteed, return the element with count greater than n/2.
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        max=0
        maxocc=0
        for index,num in enumerate(nums):
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        for key,value in dict.items():
            if value>len(nums)//2 and value>max:
                max=value
                maxocc=key
        return maxocc
                


solution=Solution()
nums = [2,2,1,1,1,2,2]
print(solution.majorityElement(nums))