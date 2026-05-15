# 219. Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# Explanation:
# - Keep a dictionary mapping each number to its most recent index.
# - For each number, check whether it appeared before within k positions.
# - If yes, return True; otherwise update the index.
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for index,num in enumerate(nums):
            if num in dict and abs(index-dict[num])<=k:
                return True
            else:
                dict[num]=index
        return False




        
solution=Solution()
nums = [1,0,1,1]
k=1
print(solution.containsNearbyDuplicate(nums,k))