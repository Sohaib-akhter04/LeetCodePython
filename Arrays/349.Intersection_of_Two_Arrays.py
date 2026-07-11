#349. Intersection of Two Arrays
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_Dic=set(nums1)
        res=[]
        for  x in nums2:
            if x in nums_Dic:
                res.append(x)
        res=set(res)
        return list(res)



solution = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(solution.intersection(nums1,nums2))