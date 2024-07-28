"""LC 322: You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin."""

#Dynamic Programming - Bottom up Approach
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize dp for the length of amount+1 and each value of this list to a max number
        dp=[amount+1]*(amount+1)
        #base case -- 0 coins required for getting zero values
        dp[0] =0
        # looping through each amount
        for a in range(1,amount+1):
            #checking the no. of denomination required to reach the goal
            for c in coins:
                #only when there is a probable solution
                if a-c >=0:
                    #main regression formula for the whole problem - 1+dp[amount-coin_denomination]
                    dp[a] = min(dp[a],1+dp[a-c])
        # return this amount only if the amount is less than  the max initiated value, else -1 (no solutions)          
        return dp[amount] if dp[amount]<amount+1 else -1            

        