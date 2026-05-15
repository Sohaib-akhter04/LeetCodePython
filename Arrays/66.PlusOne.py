# 66. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Explanation:
# - Add one to the number represented by the digits array.
# - Traverse digits from right to left.
# - If a digit is less than 9, increment it and return.
# - If a digit is 9, set it to 0 and continue carrying.
# - If all digits become 0, prepend 1.

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+digits


solution=Solution()
nums=[2,9,9]
print(solution.plusOne(nums))
