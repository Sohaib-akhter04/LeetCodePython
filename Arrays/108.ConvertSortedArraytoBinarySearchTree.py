# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# Explanation:
# - Choose the middle element as the root to maintain balance.
# - Recursively build the left subtree from elements before mid.
# - Recursively build the right subtree from elements after mid.
# - This produces a BST where depths of subtrees differ by at most one.
from typing import Optional, List
from xml.dom.minidom import Node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def Build(left,right):
            if left>right:
                return None
            
            mid=(left+right)//2

            root=TreeNode(nums[mid])
            root.left=Build(left,mid-1)
            root.right=Build(mid+1,right)

            return root
        
        return Build(0,len(nums)-1)


            


        

solution=Solution()
nums=[1,2,3,4,5]
root=solution.sortedArrayToBST(nums)
