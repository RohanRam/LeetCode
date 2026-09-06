1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        r =[]
4        r = s.split( )
5        if len(r[-1]) == 0:
6            for i in range(len(r)):
7                f = r[-1 - i]
8                if len(f) != 0:
9                    return len(f)
10
11        else:
12            return len(r[-1])