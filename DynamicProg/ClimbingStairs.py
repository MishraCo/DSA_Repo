class Solution:
    # this was solved using fibonacci series, where we have two options to climb stairs -- one or two
    def climbStairs(self, n: int) -> int:
        #initialize the two variables which will help create the Fibonacci series
        one, two = 1,1
        #looping through all the values uptill n-1 as, we know the nth position is anyways one.
        for _ in range(n-1):
            #one will hold the final solution of the variable, hence returning one
            temp = one
            one = one+two
            two =temp
        return one    


        