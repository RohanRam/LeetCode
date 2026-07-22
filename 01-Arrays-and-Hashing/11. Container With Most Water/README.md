<h2><a href="https://leetcode.com/problems/container-with-most-water">11. Container With Most Water</a></h2>

<p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;">
<pre><strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Container-With-Most-Water | Explained

## Approach 1: Two Pointers (Greedy Strategy)
### Intuition
Imagine holding two vertical board supports at opposite ends of a pool. The amount of water held between any two boards is constrained by two factors: the distance between them (width) and the height of the shorter board (height bottleneck).

To find the maximum possible volume, we start by placing our pointers at the maximum possible width (the extreme ends of the array). From this state, to potentially increase or maintain the area as the width shrinks, we must attempt to increase the height bottleneck. Moving the pointer at the taller board will only decrease the width while keeping the height bottleneck same or smaller, making an increase in area mathematically impossible. Therefore, the only logical choice is to greedily move the pointer pointing to the shorter board inward in hopes of finding a taller boundary.

### Algorithm Visualized
```mermaid
flowchart TD
    Start([Start]) --> Init[Initialize left = 0, right = n - 1, marea = 0]
    Init --> Condition{left < right?}
    Condition -- Yes --> CalcArea["Calculate area = min(height[left], height[right]) * (right - left)"]
    CalcArea --> CheckMax{area > marea?}
    CheckMax -- Yes --> UpdateMax[marea = area]
    CheckMax -- No --> CheckHeight
    UpdateMax --> CheckHeight{height[left] < height[right]?}
    CheckHeight -- Yes --> MoveLeft[left = left + 1]
    CheckHeight -- No --> MoveRight[right = right - 1]
    MoveLeft --> Condition
    MoveRight --> Condition
    Condition -- No --> Return([Return marea])
```

### Approach
1. **Initialize Pointers:** Set `left` pointer at index `0` and `right` pointer at index `n - 1`.
2. **Track Maximum Area:** Maintain a running variable `marea` initialized to `0`.
3. **Iterate with Two Pointers:** Loop while `left < right`:
   - Compute current container width: `right - left`.
   - Compute current container effective height: `min(height[left], height[right])`.
   - Compute current area: `width * height`.
   - Update `marea` if current `area` is greater than `marea`.
   - **Greedy Move:** Compare `height[left]` and `height[right]`. Increment `left` if `height[left]` is smaller; otherwise, decrement `right`.
4. **Return Result:** Once pointers meet, return `marea`.

### Detailed Code Analysis
- **Line 3 (`n=len(height)`):** Stores the total length of the array to compute initial boundaries.
- **Lines 4–6 (`left = 0`, `right = n-1`, `marea = 0`):** Sets up the extreme boundaries to maximize initial width and initializes the variable `marea` to store the maximum container area found.
- **Line 7 (`while left < right:`):** Loop invariant enforcing that a valid container requires at least two distinct lines.
- **Line 8 (`area = (min(height[left],height[right])) * (right-left)`):** Calculates the water area formed between `height[left]` and `height[right]`. The bottleneck height is extracted via `min()`.
- **Lines 9–10 (`if marea < area : marea = area`):** Updates the running maximum whenever a strictly larger area is encountered.
- **Lines 11–14 (`if height[left] < height[right] : left = left+1 else : right = right-1`):** The core greedy heuristic. Skips lines bounded by the shorter line, as any inner line paired with the current shorter line would produce a strictly smaller area (smaller width, same or smaller height).
- **Line 16 (`return marea`):** Returns the overall maximum area encountered during traversal.

### Code
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        marea = 0
        while left < right:
            area = (min(height[left], height[right])) * (right - left)
            if marea < area:
                marea = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return marea
```

### Complexity
- **Time Complexity:** $\mathcal{O}(n)$ — In each step of the loop, either `left` is incremented or `right` is decremented. Thus, every element in `height` is examined at most once, resulting in linear execution time.
- **Space Complexity:** $\mathcal{O}(1)$ — The algorithm only maintains scalar tracking variables (`n`, `left`, `right`, `marea`, `area`), using constant auxiliary memory.

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **When `height[left] == height[right]`, does it matter which pointer is moved?**
   - **Answer:** No. When both heights are equal, moving either pointer (or both) is correct. Because both boundaries share the same height bottleneck, keeping either wall while narrowing the width can never produce a larger area with any remaining interior wall unless both pointers are moved to find a strictly taller pair of lines.

2. **How does this problem differ fundamentally from "Trapping Rain Water"?**
   - **Answer:** "Container With Most Water" asks for a single container formed by choosing *any two lines* in the array (ignoring intermediate lines inside). "Trapping Rain Water" computes the aggregate water trapped across *all* elevation relief bars based on local surrounding maximum heights. Two pointers work for both, but the governing formulas and conditions reflect global pair selection vs. local elevation bounds.