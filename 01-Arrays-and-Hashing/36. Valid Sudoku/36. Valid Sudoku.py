1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        n=9
4        
5        for i in range(0,n):
6            row = set()
7            for j in range(0,n):
8                if board[i][j] == .:
9                    continue
10                if board[i][j] in row:
11                    return False
12
13                row.add(board[i][j])
14                
15        
16        for j in range(0,n):
17            col = set()
18            for i in range(0,n):
19                if board[i][j] == .:
20                    continue
21                if board[i][j] in col:
22                    return False
23
24                col.add(board[i][j])
25
26        for row in range(0, 9, 3):
27            for col in range(0, 9, 3):
28                seen = set()
29                for i in range(row, row + 3):
30                    for j in range(col, col + 3):
31                        if board[i][j] == .:
32                            continue
33                        if board[i][j] in seen:
34                            return False
35                        seen.add(board[i][j])          
36
37            
38           
39        return True      
40                
41            
42
43