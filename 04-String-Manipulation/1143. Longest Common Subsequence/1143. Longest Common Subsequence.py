1class Solution:
2    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
3        n = len(text1)
4        m = len(text2)
5
6
7        dp= [[0] * (m+1) for _ in range(n+1)]
8
9        for i in range(1,n+1):
10            for j in range(1,m+1):
11                if text1[i-1] == text2[j-1]:
12                    dp[i][j] = dp[i-1][j-1] + 1
13                else:
14                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
15            
16        return dp[n][m]
17        