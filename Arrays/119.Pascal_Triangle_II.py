#119. Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        prevRow = self.getRow(rowIndex - 1)
        newRow = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            newRow[i] = prevRow[i - 1] + prevRow[i]

        return newRow

        

solution=Solution()
print(solution.getRow(3))