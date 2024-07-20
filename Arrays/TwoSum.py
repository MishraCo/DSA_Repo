"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initialize Dictionary [vlaue:index pair]
        res={}  
        # Iterate through the dictionary with index and value  
        for i,n in enumerate(nums):
            # check the difference value to find if it exists in the hashmap yet 
            diff = target - n
            if diff in res:
                return [res[diff],i]
            # If Diff value not found in hashmap then add the new value index pair to res    
            res[n] = i    
        return None
# Time Complexity: O(n) -- Space complexity: O(n)