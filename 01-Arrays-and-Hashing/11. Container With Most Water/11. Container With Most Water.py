1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n=len(height)
4        marea=0
5        for i in range(0,n):
6            for j in range(i+1,n):
7                area = (min(height[i],height[j])) * (j-i)
8                if area > marea :
9                    marea = area
10                
11        return marea
12                
13        