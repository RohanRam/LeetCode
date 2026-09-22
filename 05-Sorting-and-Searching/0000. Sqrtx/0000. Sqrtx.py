1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x < 2:
4            return x
5
6        left = 1
7        right = x / 2
8
9        while left <= right:
10            mid =  left +( right - left ) // 2
11
12            if mid * mid == x:
13                return int(mid) 
14            elif mid * mid < x:
15                left = mid + 1
16            else :
17                right = mid - 1
18        
19        right = int(right)
20        return right
21
22
23        