class Solution:
    def reverseBits(self, n: int) -> int:
        #result is zero
        res=0
        #traversing through the 32 bits
        for _ in range(32):
            # appnending results bit by 0 to the right end and ORing it with the right most bit from n
            res = (res<<1) | (n&1)
            #shifting to the last but one bit of n now
            n>>=1
        return res    