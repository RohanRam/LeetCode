1# class Solution:
2#     def isPalindrome(self, x: int) -> bool:
3#         s = str(x)
4#         r=s[::-1]
5#         if s == r:
6#             return True
7#         else :
8#             return False
9        
10
11class Solution:
12    def isPalindrome(self, x: int) -> bool:
13        if x < 0 or (x % 10 == 0 and x != 0):
14            return False
15        og=x
16        r=0
17        while x > 0 :
18            digit = x % 10 
19            r = r * 10 + digit
20            x = x // 10  
21
22        if r == og :
23            return True
24        else:
25            return False  