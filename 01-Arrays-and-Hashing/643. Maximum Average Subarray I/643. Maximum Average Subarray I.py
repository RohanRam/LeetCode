1class Solution:
2    def findMaxAverage(self, nums: list[int], k: int) -> float:
3        win_sum = sum(nums[:k])
4        max_sum = win_sum
5
6        for i in range(k,len(nums)):
7            # win_sum = win_sum + nums[i]
8            # win_sum = win_sum - nums[i-k]
9
10            # max_sum = max(win_sum,max_sum)
11
12            win_sum += nums[i] - nums[i-k]
13            if  win_sum > max_sum:
14                max_sum=win_sum
15
16                
17        return max_sum / k
18
19        
20        
21
22        