#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Explanation:
# - Append nums2 elements to the end of nums1.
# - Sort the merged array using a merge sort helper.
# - Copy the sorted results back into nums1.
# - This uses extra space from merge sort but preserves the required output array.
from typing import List
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m + i] = nums2[i]

        sorted_nums = self.merge_sort(nums1)

        for i in range(len(nums1)):
            nums1[i] = sorted_nums[i]

    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge2(left, right)

    def merge2(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result



    
    
solution=Solution()
nums1=[1,2,3,0,0,0]
nums2 = [2,5,6]
solution.merge(nums1,3,nums2,3)