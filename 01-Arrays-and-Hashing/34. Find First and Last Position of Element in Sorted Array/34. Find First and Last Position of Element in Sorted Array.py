1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        n=len(nums)
4        t=[]
5        for i,num in enumerate(nums):
6            if num == target:
7                t.append(i)
8        if target in nums:
9            return [t[0],t[-1]]
10        else:
11            return [-1,-1]
12
13
14            
15            
16            
17
18