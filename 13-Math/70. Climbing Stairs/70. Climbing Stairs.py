1class Solution:
2    def climbStairs(self, n: int) -> int:
3
4        dp = [0] * (n + 2)
5
6        dp[1]=1
7        dp[2]=2
8
9        if n == 1:
10            return 1
11        elif n == 2:
12            return 2
13        else:
14            for i in range(3,n+1):
15                dp[i]=dp[i-1]+dp[i-2]
16        
17            return dp[n]      
18