1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        n=len(nums)
4        left=0
5        for right in range(n):
6            if nums[right] != val:
7                nums[left] = nums[right]
8                left+=1       
9            
10
11        return left
12
13                
14              
15
16
17
18        