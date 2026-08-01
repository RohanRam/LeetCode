1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        n=len(nums)
4        jumps=0
5        left=0
6        right=0
7
8        while right < n-1:
9
10            far=0
11
12            for i in range(left,right+1):
13                far=max(far,i+nums[i])
14
15            left =right+1
16            right = far
17            jumps+=1
18        return jumps
19
20
21                
22    
23        
24
25            
26        