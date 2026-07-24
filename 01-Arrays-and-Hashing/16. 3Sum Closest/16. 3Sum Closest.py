1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        sumArr=0
4        diff=9999999
5
6        nums.sort()
7        n=len(nums)
8
9        for i in range(0,n-2):
10            left=i+1
11            right=n-1
12
13            while left < right :
14                csum =nums[i] + nums[left] + nums[right] 
15                if csum > target:
16                    right-=1
17                elif csum < target:
18                    left+=1
19                else:
20                    return csum
21                cdiff=abs(csum-target)
22
23                if cdiff < diff :
24                    diff=cdiff
25                    sumArr = csum
26                    
27
28        return sumArr
29
30                
31                
32                
33
34
35
36
37        