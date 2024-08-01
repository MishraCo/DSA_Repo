#LC 39 - Combination Sum I

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=[]

        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(nums) or total > target:
                return
            cur.append(nums[i])    
            dfs(i,cur,total+nums[i]) 
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        print(res)
        return 0      