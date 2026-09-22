1class Solution:
2    def maximum69Number (self, num: int) -> int:
3        s = str(num)
4        r=0
5        for i in range(len(s)):
6            if s[i] == '6':
7                ans = s[:i] + '9' + s[i+1:]
8                r=int(ans)
9                break 
10        
11        if r > num :
12            return r
13        else:
14            return num
15
16        