1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums) - 1
5        while l <= r:
6            mid = l + (r - l) // 2
7            if nums[mid] == target:
8                return mid
9
10            if nums[l] <= nums[mid]:
11                if nums[l] <= target < nums[mid]:
12                    r = mid - 1
13                else:
14                    l = mid + 1
15            else:
16                if nums[mid] < target <= nums[r]:
17                    l = mid + 1
18                else:
19                    r = mid - 1
20        return -1
21