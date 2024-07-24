"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #list returning the triplets
        res=[]
        #sorting the array for easier traversal O(nlogn) 
        nums.sort()
        #first loop to select the value a in the three component sum
        for i,n in enumerate(nums):
            # if the i is not the first element and is the same as the previous value we just found triplet for, move ahaead, to avoid duplicates
            if i > 0 and nums[i]==nums[i-1]:
                continue
            #introduce two pointers to find b & c which as a whole lead to 0 (zero).
            l,r=i+1,len(nums)-1
            while l<r:
                threesum = n+nums[l]+nums[r]
                #if sum is greater than zero, move to left of the sub raay to find small numbers
                if threesum>0:
                    r-=1
                #if sum is less than zero, move to right of the sub raay to find larger numbers    
                elif threesum <0:
                    l+=1
                # if found append to res and cjeck for other combos    
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    # if l points to same number as before, move further right
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        # finally return the list of solutions                
        return res