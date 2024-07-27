"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        #solving it using dp; formula for counting 1's for each integer(n) -> 1+dp[n-(2^i)] 
        dp=[0] * (n+1)
        #(2^i is nothing but the offset)
        offset=1
        for i in range(1,n+1):
            #when n becomes equal to offset*2 , then time to update offset
            if offset*2==i:
                offset = i
            #storing the values in dp to utilize for further loops    
            dp[i] = 1+dp[i-offset]
        return dp        
