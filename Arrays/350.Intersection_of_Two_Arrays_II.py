#350. Intersection of Two Arrays II
#Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        count = Counter(nums1)
        result = []

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result




nums1 = [1,2,2,1] 
nums2 = [2,2]
solution=Solution()
print(solution.intersect(nums1,nums2))
        