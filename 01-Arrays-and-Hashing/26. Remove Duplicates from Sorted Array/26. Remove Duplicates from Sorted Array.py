1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        n=len(nums)
4        
5        if n==0:
6            return 0
7
8        left=0
9
10        for right in range(1,n):
11            if nums[left] != nums[right]:
12                left += 1
13                nums[left] = nums[right]
14        
15        return left+1
16
17