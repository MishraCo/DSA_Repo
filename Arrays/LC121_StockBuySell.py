"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two Pointers Problem
        l,r=0,1
        #Maximum Profir that can be acheived
        MaxP=0
        #condition for loop to run to avoid out of bounds situation
        while r<len(prices):
            # if l is less than r , then naturally it is profitable and hence the profit will be calculated to see if it is more than the current profit and the value will be replaced with this buying condition, as it is favorable to the desired outcome.
            if prices[l]<prices[r]:
                diff = prices[r]-prices[l]
                MaxP = max(MaxP,diff)

            else:
                # If r<l then we desire the lowest buying point, hence l should take th place of r
                l=r
            # compare l with the rest of the values to only select the r we need    
            r+=1        
        return MaxP

        