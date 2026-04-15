# Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string 
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength=200
        for i,nums in enumerate(strs):
            if len(nums)<minLength:
                minLength=len(nums)
                smallest=nums
        print(minLength,smallest)
        for i in range(minLength):
            for words in strs:
                if words[i]!= smallest[i]:
                    return smallest[:i]
        return smallest[:minLength]

strs=["flower","flow","flight"]        
sol=Solution()
print(sol.longestCommonPrefix(strs))