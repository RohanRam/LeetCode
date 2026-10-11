1class Solution:
2    def findErrorNums(self, nums: list[int]) -> list[int]:
3        nums.sort()
4        seen = {}
5        dup=0
6        missing=0
7        for i,num in enumerate(nums):
8            if num in seen:
9                dup=num
10            else:
11                seen[num]=i
12        
13        for i in range(len(nums)+1):
14            if i not in seen:
15                missing = i
16        
17        return [dup,missing]
18
19         
20
21            
22
23        
24            
25            
26        
27
28        