1class Solution:
2    def nextPermutation(self, nums: List[int]) -> None:
3        
4        Do not return anything, modify nums in-place instead.
5        
6        # [1, 3, 7, 4, 2, 1]
7        n=len(nums)
8        
9        i=n-2
10
11        while i>=0 and nums[i] >= nums[i+1] :
12            i-=1
13        
14        if i >= 0: 
15            j=n-1
16            while nums[j] <= nums[i]:
17                j-=1
18            temp=nums[i]
19            nums[i]=nums[j]
20            nums[j]=temp
21        
22        left = i+1
23        right=n-1
24
25        while left < right :
26            nums[left],nums[right] = nums[right],nums[left]
27
28            left+=1
29            right-=1
30        
31
32        
33            
34
35
36
37
38            
39
40        