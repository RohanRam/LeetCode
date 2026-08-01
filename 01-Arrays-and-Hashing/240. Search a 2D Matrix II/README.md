<h2><a href="https://leetcode.com/problems/search-a-2d-matrix-ii">240. Search a 2D Matrix II</a></h2>

<p>Write an efficient algorithm that searches for a value <code>target</code> in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:</p>

<ul>
	<li>Integers in each row are sorted in ascending from left to right.</li>
	<li>Integers in each column are sorted in ascending from top to bottom.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid2.jpg" style="width: 300px; height: 300px;">
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/24/searchgrid.jpg" style="width: 300px; height: 300px;">
<pre><strong>Input:</strong> matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= n, m &lt;= 300</code></li>
	<li><code>-10<sup>9</sup> &lt;= matrix[i][j] &lt;= 10<sup>9</sup></code></li>
	<li>All the integers in each row are <strong>sorted</strong> in ascending order.</li>
	<li>All the integers in each column are <strong>sorted</strong> in ascending order.</li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>


---

# 🛍️ Search-a-2D-Matrix-II | Explained

## Approach 1: Top-Right Corner Pointer (Staircase Search)

### Intuition
To efficiently search a matrix where both rows and columns are sorted independently in ascending order, think of the matrix as a Binary Search Tree (BST) rotated by 45 degrees. 

If you stand at the **top-right corner** `(0, n - 1)`:
* Moving **left** guarantees you encounter strictly **smaller** values.
* Moving **down** guarantees you encounter strictly **larger** values.

This unique property turns the top-right element into a root node with two clear paths. If the target is smaller than the current element, the entire current column below this position must also be larger than the target, allowing us to safely discard that column by moving left. Conversely, if the target is larger than the current element, the entire current row to the left must be smaller than the target, allowing us to safely discard that row by moving down.

A real-world analogy is standing at an intersection on a mountain grid where walking west always goes downhill and walking south always goes uphill. If you are looking for a specific altitude, you never need to backtrack; your current altitude dictates whether you must head west or south.

### Algorithm Visualized

```mermaid
graph TD
    Start([Start at Top-Right Corner: row = 0, col = n - 1]) --> LoopCheck{row < m AND col >= 0?}
    LoopCheck -- No --> OutOfBounds[Return False]
    LoopCheck -- Yes --> Compare{matrix[row][col] == target?}
    
    Compare -- Yes --> Match[Return True]
    Compare -- No --> CheckGreater{matrix[row][col] > target?}
    
    CheckGreater -- Yes --> MoveLeft[Current value too large<br/>Discard Column: col -= 1]
    CheckGreater -- No --> MoveDown[Current value too small<br/>Discard Row: row += 1]
    
    MoveLeft --> LoopCheck
    MoveDown --> LoopCheck
```

### Approach
1. **Validate Matrix Input**: Check if the matrix is empty or uninitialized to prevent out-of-bounds access.
2. **Initialize Coordinates**: Start at the top-right corner of the matrix (`row = 0`, `col = n - 1`).
3. **Traverse Matrix**: Continue navigating while `row` remains within row bounds (`row < m`) and `col` remains within column bounds (`col >= 0`).
4. **Evaluate Current Cell**:
   * If `matrix[row][col] == target`: Target found, return `True`.
   * If `matrix[row][col] > target`: Decrement `col` by 1 to search for smaller values in the current row.
   * If `matrix[row][col] < target`: Increment `row` by 1 to search for larger values in the current column.
5. **Termination**: If the pointers step out of the matrix boundary, the target does not exist in the matrix. Return `False`.

### Detailed Code Analysis

```python
1class Solution:
2    def searchMatrix(self, matrix, target):
3        if not matrix or not matrix[0]:
4            return False
```
* **Lines 3–4**: Guards against empty input matrices such as `[]` or `[[]]`. If either condition evaluates to `True`, the code immediately short-circuits and returns `False`.

```python
6        m, n = len(matrix), len(matrix[0])
7        row, col = 0, n - 1
```
* **Line 6**: Extracts the dimensions of the grid. `m` represents the total number of rows, and `n` represents the total number of columns.
* **Line 7**: Initializes two pointer variables: `row` set to `0` (top row) and `col` set to `n - 1` (rightmost column). This positions the search at the top-right corner.

```python
9        while row < m and col >= 0:
10            if matrix[row][col] == target:
11                return True
12            elif matrix[row][col] > target:
13                col -= 1
14            else:
15                row += 1
```
* **Line 9**: The loop condition ensures pointers never breach matrix boundaries. We only move downwards (`row` increases toward `m`) and leftwards (`col` decreases toward `0`).
* **Lines 10–11**: Direct equality check. If the cell matches `target`, search terminates successfully with `True`.
* **Lines 12–13**: If the value at `matrix[row][col]` exceeds `target`, all elements below it in the same column are also strictly greater than `target` (since columns are sorted top-to-bottom). Thus, we discard this column by moving left (`col -= 1`).
* **Lines 14–15**: If the value at `matrix[row][col]` is less than `target`, all elements to its left in the same row are also strictly smaller than `target` (since rows are sorted left-to-right). Thus, we discard this row by moving down (`row += 1`).

```python
17        return False
```
* **Line 17**: If the pointers move outside the grid limits without encountering `target`, it confirms `target` does not exist in the matrix. Return `False`.

### Code

```python
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False
```

### Complexity
- **Time Complexity:** $\mathcal{O}(m + n)$
  In each iteration of the `while` loop, we either increment `row` or decrement `col`. In the worst-case scenario (e.g., searching for an element smaller than `matrix[0][0]` or larger than `matrix[m-1][n-1]`), we perform at most $m$ downward moves and $n$ leftward moves before exiting the boundaries. Thus, the maximum number of steps is $m + n$.

- **Space Complexity:** $\mathcal{O}(1)$
  The algorithm executes entirely in-place. It only keeps track of scalar integer pointers (`row`, `col`, `m`, `n`), requiring constant extra space.

---

## 🕵️‍♂️ Follow-up Questions

### 1. Could we start the search from the bottom-left corner instead?
**Answer:** Yes, absolutely. Starting at the bottom-left corner `(m - 1, 0)` provides the exact same decision-making power:
* Moving **up** decreases the current value.
* Moving **right** increases the current value.

However, starting from the top-left `(0, 0)` or bottom-right `(m - 1, n - 1)` corners **does not** work for this algorithm because both available directions from those corners move in the same relative direction (e.g., from top-left, going right OR down both lead to larger values), rendering a deterministic single-path decision impossible.

### 2. How does this compare to running Binary Search on each row?
**Answer:** 
* **Row-by-Row Binary Search:** Running binary search on each of the $m$ rows takes $\mathcal{O}(m \log n)$ time.
* **Top-Right Staircase Search:** Takes $\mathcal{O}(m + n)$ time.

When $m$ and $n$ are roughly equal (e.g., $N \times N$), $\mathcal{O}(N)$ is asymptotically optimal compared to $\mathcal{O}(N \log N)$. However, if $m \ll n$ (e.g., $m = 2, n = 1,000,000$), row-wise binary search $\mathcal{O}(m \log n)$ requires only $\sim 40$ operations, whereas staircase search $\mathcal{O}(m + n)$ takes $\sim 1,000,000$ operations.