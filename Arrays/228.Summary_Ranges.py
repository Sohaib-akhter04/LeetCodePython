# 228. You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
# Explanation:
# - Track the start and end of the current consecutive range.
# - Extend the range while each next number is exactly one greater than the previous.
# - When a break occurs, append the completed range string to the result.
# - After the loop, append the final range before returning.
from typing import List 
'''You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        
        ranges=[]
        start=nums[0]
        end=nums[0]


        for i in range(1,len(nums)):
            if nums[i]==end+1: #7==6+1
                end=nums[i]  #7 idher ayega tou loop khtm hojayega 
            else:
                if start==end:
                    ranges.append(str(end))
                else:
                    ranges.append(str(start)+"->"+str(end))
                start=nums[i] # 7
                end=nums[i] # 7
        if start==end:
            ranges.append(str(end)) # 7==7
        else:# else me start iska different hoga tou wo tou piche saved hai or wo else me ayega hi jab or change hoga jb wo plus nhi horha
            ranges.append(str(start)+"->"+str(end))
        return ranges
        


solution=Solution()
nums=[0,1,2,4,5,7]
print(solution.summaryRanges(nums))