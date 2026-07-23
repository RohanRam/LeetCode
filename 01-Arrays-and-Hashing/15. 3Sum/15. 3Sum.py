1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        n=len(nums)
4
5        out=[]
6        for i in range (0,n):
7            for j in range(i+1,n):
8                for k in range(j+1,n):
9                    if ((nums[i] + nums[j] + nums[k]) == 0):
10                        curr=sorted([nums[i] , nums[j] , nums[k]])
11                        if curr not in out:
12                            out.append(curr)
13        return out
14
15        