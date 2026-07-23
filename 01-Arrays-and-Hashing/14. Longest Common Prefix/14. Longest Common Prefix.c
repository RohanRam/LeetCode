1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        common = 
4        strs.sort()
5        n=len(strs)
6        s1 = strs[0]
7        s2 = strs[-1]
8        x=min(len(s1),len(s2))
9        for i in range(0,x):
10            if s1[i] == s2[i]:
11                common = common + s1[i]
12            else :
13                break
14        return common       
15        