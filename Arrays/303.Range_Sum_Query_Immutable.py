# 303. Range Sum Query - Immutable
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] stores the sum of the first i elements.
        # Example: nums = [5, 2, 7] -> prefix = [0, 5, 7, 14]
        # This leading 0 helps us compute any range sum with one subtraction.
        self.prefix = [0]

        # running_sum keeps the cumulative sum while we scan nums.
        running_sum = 0
        for num in nums:
            # Add current value into the cumulative sum.
            running_sum += num

            # Save cumulative sum so later queries are O(1).
            self.prefix.append(running_sum)

    def sumRange(self, left: int, right: int) -> int:
        # Sum from left to right (inclusive):
        # prefix[right + 1] contains sum of nums[0..right]
        # prefix[left] contains sum of nums[0..left-1]
        # Subtract to keep only nums[left..right].
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    # Example input array.
    nums = [-2, 0, 3, -5, 2, -1]

    # Create the object once (preprocessing happens in constructor).
    obj = NumArray(nums)

    # Query examples:
    # nums[0:3] -> [-2, 0, 3] -> 1
    print(obj.sumRange(0, 2))  # 1

    # nums[2:6] -> [3, -5, 2, -1] -> -1
    print(obj.sumRange(2, 5))  # -1

    # nums[0:6] -> entire array -> -3
    print(obj.sumRange(0, 5))  # -3