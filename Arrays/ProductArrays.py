"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Using the prefix and postfix values, multiplying them together we can find the value for each position without having to multiply with the product itself.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        Prefix = 1
        # calculating prefix and storing in the array/list
        for i in range(len(nums)):
            res[i] = Prefix
            Prefix*=nums[i]
        Postfix=1    
        #calculating pstfix and storing in the array/list
        for j in range(len(nums)-1, -1,-1):
            res[j]*=Postfix
            Postfix*=nums[j]
        return res    