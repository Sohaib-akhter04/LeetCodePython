# 27. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Explanation:
# - Use a write pointer to keep track of the next position for a value that is not val.
# - Copy each non-val element forward and increment the pointer.
# - Return the final pointer as the count of remaining values.
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index



solution=Solution()
print(solution.removeElement([3,2,2,3], 3)) # Output: 2