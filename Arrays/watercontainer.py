#brute force solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        for n in range(len(height)):
            for k in range(n+1,len(height)):
                area = (k-n) * min(height[n],height[k])
                res=max(res,area)
        return res        

#linear time comlexity solution 
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l,r= 0, (len(height)-1)
        while l < r:
            area = (r - l) * min(height[l],height[r])
            res=max(res,area)
            #whichever height is smaller, shit that pointer to next
            if height[l] < height[r]:
                l+=1
            elif height[r]< height[l]:
                r-=1
            #both are equal height, update anyone    
            else:
                r-=1
        return res        

        