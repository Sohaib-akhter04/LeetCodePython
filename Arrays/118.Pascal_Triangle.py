# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# Explanation:
# - The first row is [1].
# - Each new row starts and ends with 1.
# - Each interior value is the sum of the two values above it from the previous row.
# - Build the triangle row by row, using the previous row to compute the next.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        prevRows=self.generate(numRows-1)
        newRow=[1]*numRows
        # print(newRow)
        for i in range(1,numRows-1):
            newRow[i]=prevRows[-1][i-1]+prevRows[-1][i]
        prevRows.append(newRow)
        return prevRows



solution=Solution()
print(solution.generate(5))