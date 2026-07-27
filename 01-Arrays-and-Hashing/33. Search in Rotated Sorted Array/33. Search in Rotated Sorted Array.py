1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4        for i in range(n):
5            if nums[i] == target :
6                return i
7 
8        return -1
9        