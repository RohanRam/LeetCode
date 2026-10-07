1# class Solution:
2#     def maxSubArray(self, nums: list[int]) -> int:
3#         n=len(nums)
4#         result = []
5#         for i in range(n):
6#             for j in range(i,n):
7#                 result.append(nums[i:j+1])
8        
9#         temp = float('-inf')
10#         for res in result :
11#             t = sum(res)
12#             if t > temp :
13#                 temp = t
14#         return temp
15
16class Solution:
17    def maxSubArray(self, nums: list[int]) -> int:
18        cur_sum = 0
19        max_sum = nums[0]
20        for num in nums:
21            cur_sum = cur_sum + num
22            if cur_sum > max_sum :
23                max_sum = cur_sum
24            if cur_sum < 0 :
25                cur_sum = 0
26        return max_sum
27            
28#DP_topic