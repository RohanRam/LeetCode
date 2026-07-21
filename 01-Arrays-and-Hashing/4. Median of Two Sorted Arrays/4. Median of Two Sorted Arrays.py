1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        nums1.extend(nums2)
4        nums1.sort()
5        n=len(nums1)
6        if n % 2 == 1:
7            median = nums1[n//2]
8        else :
9            median = (( nums1[n//2-1] + nums1[n//2] )/2)
10
11        return median
12
13
14        