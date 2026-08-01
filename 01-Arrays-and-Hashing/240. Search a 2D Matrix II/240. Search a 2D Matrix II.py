1class Solution:
2    def searchMatrix(self, matrix, target):
3        if not matrix or not matrix[0]:
4            return False
5
6        m, n = len(matrix), len(matrix[0])
7        row, col = 0, n - 1
8
9        while row < m and col >= 0:
10            if matrix[row][col] == target:
11                return True
12            elif matrix[row][col] > target:
13                col -= 1
14            else:
15                row += 1
16
17        return False