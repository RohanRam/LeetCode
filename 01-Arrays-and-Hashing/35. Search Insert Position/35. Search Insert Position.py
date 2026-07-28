1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4        left=0
5        right=n-1
6        # [1,3,5,6]2
7        while left <=right:
8            mid = (left+right)//2
9            if target == nums[mid]:
10                return mid
11            elif target < nums[mid] :
12                right=mid-1
13            elif target > nums[mid]:
14                left=mid+1
15        
16        if target > nums[mid]:
17            return mid+1
18        else:
19            return mid
20
21    