1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n=len(height)
4        left = 0
5        right = n-1
6        marea = 0
7        while left < right:
8            area = (min(height[left],height[right])) * (right-left)
9            if marea < area :
10                marea = area
11            if height[left] < height[right] :
12                left = left+1
13            else :
14                right = right-1
15
16        return marea
17
18        