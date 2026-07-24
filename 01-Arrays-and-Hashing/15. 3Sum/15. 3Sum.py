1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        n=len(nums)
4        out=[]
5        nums.sort()
6        for i in range(n-2):
7            if i>0 and nums[i] == nums[i-1]:
8                continue
9            
10            left = i+1
11            right = n-1
12
13            while left < right:
14                total = nums[i] + nums[left] + nums[right]
15                if total > 0:
16                    right = right-1
17                elif total < 0:
18                    left = left+1
19                else :
20                    out.append([nums[i],nums[left],nums[right]])
21
22                    while left < right and nums[left] == nums[left+1]:
23                        left =left+1
24                    while right > left and nums[right] == nums[right-1]:
25                        right-=1
26                    left += 1
27                    right -= 1
28        
29        return out
30
31
32        