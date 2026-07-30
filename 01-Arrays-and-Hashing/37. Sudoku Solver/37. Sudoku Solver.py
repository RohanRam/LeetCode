1class Solution:
2    def solveSudoku(self, board: List[List[str]]) -> None:
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        # Fill the sets with existing numbers
8        for r in range(9):
9            for c in range(9):
10                if board[r][c] != .:
11                    rows[r].add(board[r][c])
12                    cols[c].add(board[r][c])
13                    box = (r // 3) * 3 + (c // 3)
14                    boxes[box].add(board[r][c])
15
16        def backtrack():
17            for r in range(9):
18                for c in range(9):
19                    if board[r][c] == .:
20                        box = (r // 3) * 3 + (c // 3)
21
22                        for num in 123456789:
23                            if (
24                                num not in rows[r]
25                                and num not in cols[c]
26                                and num not in boxes[box]
27                            ):
28                                board[r][c] = num
29                                rows[r].add(num)
30                                cols[c].add(num)
31                                boxes[box].add(num)
32
33                                if backtrack():
34                                    return True
35
36                                # Undo (Backtrack)
37                                board[r][c] = .
38                                rows[r].remove(num)
39                                cols[c].remove(num)
40                                boxes[box].remove(num)
41
42                        return False
43            return True
44
45        backtrack()