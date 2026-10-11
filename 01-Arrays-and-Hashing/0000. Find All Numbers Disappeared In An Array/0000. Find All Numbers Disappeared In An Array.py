1class Solution:
2    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
3        dis=[]
4        seen=set(nums)
5        for i in range(1,len(nums)+1):
6            if i not in seen:
7                dis.append(i)
8        return dis
9
10
11        