#119. Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]*(rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i-1,0,-1):
                row[j]=row[j-1]+row[j]
        return row


        

solution=Solution()
print(solution.getRow(3))