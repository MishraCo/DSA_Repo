"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        MaxSub = nums[0]
        CurSum = 0
        for n in nums:
            if CurSum <0:
                CurSum = 0
            CurSum+=n
            MaxSub=max(MaxSub,CurSum)
        return MaxSub    