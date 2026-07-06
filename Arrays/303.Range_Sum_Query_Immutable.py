# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] stores sum of first i elements (0..i-1)
        self.prefix = [0]
        running_sum = 0
        for num in nums:
            running_sum += num
            self.prefix.append(running_sum)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right) 

if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)

    print(obj.sumRange(0, 2))  # 1
    print(obj.sumRange(2, 5))  # -1
    print(obj.sumRange(0, 5))  # -3