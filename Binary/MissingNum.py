class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(len(nums)):
            # cane be done by summing bothe the arrays and subtracting to find the difference, that's the missing number
            #res+= i-nums[i]
            #xoring method -- 5^5^3=3 --- same values negate each other, odd one reamins
            res^=i^nums[i]
        return res    
        