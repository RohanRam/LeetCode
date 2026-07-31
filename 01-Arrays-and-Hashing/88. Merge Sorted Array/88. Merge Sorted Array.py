1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        
4        Do not return anything, modify nums1 in-place instead.
5        
6        nums1[:]=nums1[:m]
7        nums1.extend(nums2)
8        nums1.sort()
9        # zc=0
10        # for i in range (m+n):
11        #     if nums1[i] == 0:
12        #         zc+=1
13        # nums1[:]=nums1[zc:]
14        
15
16
17
18
19            
20
21