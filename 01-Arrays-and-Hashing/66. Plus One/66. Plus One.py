1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        num=0
4        for i in digits:
5            num= (num*10) + i
6        
7        r=num+1
8        arr= list(map(int,str(r)))
9        return arr
10            
11        
12        
13        
14
15        