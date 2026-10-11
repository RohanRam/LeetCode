1class Solution:
2    def buildArray(self, target: list[int], n: int) -> list[str]:
3        op=[]
4        j=0
5
6        for i in range(1,n+1):
7            op.append(Push)
8
9            if i == target[j]:
10                j=j+1
11                if j == len(target):
12                    break            
13                        
14            else:
15                op.append(Pop)
16                
17        
18        return op
19            
20
21        