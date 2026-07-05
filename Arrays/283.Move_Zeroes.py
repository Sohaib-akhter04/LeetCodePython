# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0

        # Move all non-zero values forward
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Fill the rest with zeros
        for i in range(write, len(nums)):
            nums[i] = 0
                    

        """
        Do not return anything, modify nums in-place instead.
        """
nums=[0,1,0,3,12]
solution=Solution()
solution.moveZeroes(nums)


