"""
Given an integer array nums, return true if any value appears
at least twice in the array, and return false if every element is distinct.

There are multiple ways to solve the problem:
1. Brute Force: O(n^2) - Check each element tofind if they are duplicate.
2. Sorting: O(nlogn) - Space Complexity is - O(1) - Once pass through the list and we can find adjacent values are duplicate or not.
3. HashSet - TC: O(n) & SC: O(n) - one pass through the list - if an element is present in the Hashset then return True.
"""

#Hashset Implementation

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Initialize HashSet
        HashSet = set()
        #Loop through the nums list
        for n in nums:
            # check for the number being present in the hashset
            if n in HashSet:
                #if present  return True
                return True
            #else add number to HashSet    
            HashSet.add(n)
        # return False if no dups present    
        return False        
        

