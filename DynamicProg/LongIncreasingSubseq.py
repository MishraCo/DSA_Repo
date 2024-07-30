"""
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                # j comes after i , for if i<j, we can safely add 1 to what number res[j] holds
                if nums[i]<nums[j]:
                    res[i]=max(res[i],1+res[j])
        return max(res)            