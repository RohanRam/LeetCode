<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array">33. Search in Rotated Sorted Array</a></h2>

<p>There is an integer array <code>nums</code> sorted in ascending order (with <strong>distinct</strong> values).</p>

<p>Prior to being passed to your function, <code>nums</code> is <strong>possibly left rotated</strong> at an unknown index <code>k</code> (<code>1 &lt;= k &lt; nums.length</code>) such that the resulting array is <code>[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]</code> (<strong>0-indexed</strong>). For example, <code>[0,1,2,4,5,6,7]</code> might be left rotated by&nbsp;<code>3</code>&nbsp;indices and become <code>[4,5,6,7,0,1,2]</code>.</p>

<p>Given the array <code>nums</code> <strong>after</strong> the possible rotation and an integer <code>target</code>, return <em>the index of </em><code>target</code><em> if it is in </em><code>nums</code><em>, or </em><code>-1</code><em> if it is not in </em><code>nums</code>.</p>

<p>You must write an algorithm with <code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li>All values of <code>nums</code> are <strong>unique</strong>.</li>
	<li><code>nums</code> is an ascending array that is possibly rotated.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Search-in-Rotated-Sorted-Array | Explained

## Approach 1: Linear Search (Brute Force)
### Intuition
Imagine looking for a specific book on a single bookshelf where the books were originally in alphabetical order, but someone picked up a section from the end and put it at the beginning. If you choose to ignore the partial ordering and simply check every single book one by one from left to right, you are performing a linear search. This approach works unconditionally because checking every element guarantees you will either find the target or prove it is not present in the array.

### Algorithm Visualized
```mermaid
graph TD
    A[Start Search] --> B[Initialize length n = len nums]
    B --> C[Loop i from 0 to n-1]
    C --> D{Is nums[i] == target?}
    D -- Yes --> E[Return Index i]
    D -- No --> F[Continue Loop]
    F --> C
    C -- Exhausted Array --> G[Return -1]
```

### Approach
1. Determine the length of the input array `nums` and store it in `n`.
2. Iterate through each index `i` from `0` to `n - 1`.
3. Compare the element at the current index `nums[i]` with the `target`.
4. If a match is found, immediately return the current index `i`.
5. If the loop completes without finding the `target`, return `-1` to indicate that the target does not exist in the array.

### Detailed Code Analysis
- **Line 3 (`n=len(nums)`):** Calculates the total number of elements in the array `nums` and assigns it to variable `n`.
- **Line 4 (`for i in range(n):`):** Establishes a `for` loop that iterates sequentially through all valid indices from `0` up to `n - 1`.
- **Line 5 (`if nums[i] == target :`):** Evaluates whether the value at index `i` matches the specified `target`.
- **Line 6 (`return i`):** Short-circuits the function execution and returns the index `i` as soon as the target element is encountered.
- **Line 8 (`return -1`):** Executes only if the loop finishes without triggering the return statement inside the conditional check, signalling that the target is absent from `nums`.

### Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i] == target :
                return i
 
        return -1
```

### Complexity
- **Time:** $\mathcal{O}(N)$, where $N$ is the number of elements in `nums`. In the worst-case scenario ( target is at the last position or not present at all), every element in the array must be inspected once.
- **Space:** $\mathcal{O}(1)$ auxiliary space, as the algorithm only uses a single integer variable `n` and loop counter `i`, requiring constant additional memory regardless of input size.

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **Can we improve the time complexity to $\mathcal{O}(\log N)$?**
   - **Answer:** Yes. Because the original array was sorted prior to rotation, one half of the array divided by the midpoint will always remain strictly sorted. By modified Binary Search, we can identify which half is sorted, check if the `target` falls within that sorted range, and discard the other half in each step, reducing time complexity to $\mathcal{O}(\log N)$.

2. **How does this solution handle duplicate values if the problem constraints are relaxed?**
   - **Answer:** Linear search handles duplicates automatically without modification because it checks every index sequentially. However, for a binary search approach, duplicates make it impossible to determine which half is sorted when `nums[left] == nums[mid] == nums[right]`, forcing a worst-case degradation to $\mathcal{O}(N)$.