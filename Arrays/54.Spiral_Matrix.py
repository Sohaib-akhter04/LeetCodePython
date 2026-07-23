# 54. Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        left=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1
        res=[]
        while left <= right and top <= bottom:
            # left -> right
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top+=1

            # top to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1

            # right -> left
            if top <= bottom:
                for j in range(right, left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1

            # Bottom -> Top
            if left <= right:
                for j in range(bottom,top-1,-1):
                    res.append(matrix[j][left])
                left+=1


        return res
                




solution=Solution()
matrix = [[6,9,7]]
print(solution.spiralOrder(matrix))
