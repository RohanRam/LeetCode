<h2><a href="https://leetcode.com/problems/3sum">15. 3Sum</a></h2>

<p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
<strong>Explanation:</strong> 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,1]
<strong>Output:</strong> []
<strong>Explanation:</strong> The only possible triplet does not sum up to 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,0]
<strong>Output:</strong> [[0,0,0]]
<strong>Explanation:</strong> The only possible triplet sums up to 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


---

# 🛍️ 3Sum | Explained

## Approach 1: Brute Force Search with Linear Deduplication
### Intuition
Imagine you have a bag of numbered balls and you want to find every group of three balls whose numbers add up to zero. The most straightforward strategy—and the one implemented here—is to systematically try every possible combination of three balls. It's like checking every combination on a three-dial lock until you find the combinations that total zero. To prevent adding the exact same combination multiple times (e.g., `[-1, 0, 1]` and `[0, 1, -1]`), each valid group is sorted into a standard order and checked against a master list of already found groups.

### Algorithm Visualized
```mermaid
flowchart TD
    Start([Start: input nums]) --> Init[n = len(nums), out = []]
    Init --> LoopI[Loop i from 0 to n-1]
    LoopI --> LoopJ[Loop j from i+1 to n-1]
    LoopJ --> LoopK[Loop k from j+1 to n-1]
    LoopK --> CheckSum{nums[i] + nums[j] + nums[k] == 0?}
    CheckSum -- Yes --> SortTriplet["curr = sorted([nums[i], nums[j], nums[k]])"]
    SortTriplet --> CheckDup{curr not in out?}
    CheckDup -- Yes --> Append[out.append(curr)]
    CheckDup -- No --> NextK[Next iteration]
    Append --> NextK
    CheckSum -- No --> NextK
    NextK --> LoopK
    LoopK -- End of k --> LoopJ
    LoopJ -- End of j --> LoopI
    LoopI -- End of i --> Return([Return out])
```

### Approach
1. Determine the number of elements $n$ in the input list `nums`.
2. Initialize an empty list `out` to store unique triplet combinations.
3. Use three nested loops to generate all unique triplets based on indices $(i, j, k)$ such that $0 \le i < j < k < n$:
   - The outer loop selects the first element index $i$.
   - The middle loop selects the second element index $j$ starting from $i + 1$.
   - The inner loop selects the third element index $k$ starting from $j + 1$.
4. For each triplet index combination, compute the sum `nums[i] + nums[j] + nums[k]`.
5. If the sum equals `0`:
   - Sort the triplet to canonicalize its order so duplicate combinations appear identical.
   - Perform a membership check `curr not in out`.
   - If `curr` is not in `out`, append it to `out`.
6. Return `out` after checking all combinations.

### Detailed Code Analysis
- **Line 3 (`n=len(nums)`):** Calculates the total number of elements in the list to define loop boundaries.
- **Line 5 (`out=[]`):** Prepares an empty Python list that serves as the accumulator for result triplets.
- **Lines 6–8 (`for i...`, `for j...`, `for k...`):**
  - Line 6 starts the first pointer $i$ from index `0` up to `n-1`.
  - Line 7 starts the second pointer $j$ from `i+1` up to `n-1` to guarantee $j > i$.
  - Line 8 starts the third pointer $k$ from `j+1` up to `n-1` to guarantee $k > j$.
  - This ensures every combination of 3 indices is tested exactly once.
- **Line 9 (`if ((nums[i] + nums[j] + nums[k]) == 0):`):** Evaluates if the sum of the current values equals zero.
- **Line 10 (`curr=sorted([nums[i] , nums[j] , nums[k]])`):** Creates a list of the three elements and sorts it in $O(1)$ time (since length is fixed at 3). Sorting normalizes permutations (e.g., `[-1, 1, 0]` becomes `[-1, 0, 1]`).
- **Line 11 (`if curr not in out:`):** Performs a linear scan over the `out` list to check if `curr` has already been recorded. This prevents duplicate triplets in the output.
- **Line 12 (`out.append(curr)`):** Appends the unique triplet to the results list.
- **Line 13 (`return out`):** Returns the final list of triplets after all index combinations are exhausted.

### Code
```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)

        out=[]
        for i in range (0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if ((nums[i] + nums[j] + nums[k]) == 0):
                        curr=sorted([nums[i] , nums[j] , nums[k]])
                        if curr not in out:
                            out.append(curr)
        return out
```

### Complexity
- **Time:** $O(n^4)$ worst-case. Generating all index triplets takes $\binom{n}{3} = \frac{n(n-1)(n-2)}{6} = O(n^3)$ iterations. Inside the loop, `curr not in out` performs a linear search over `out`. Since `out` can hold up to $O(n^2)$ unique triplets, each check takes up to $O(n^2)$ time in the worst case, yielding an overall time complexity of $O(n^3 \cdot n^2)$ bounded by $O(n^4)$ or $O(n^3)$ depending on duplicate density. This causes a Time Limit Exceeded (TLE) error on LeetCode.
- **Space:** $O(1)$ auxiliary space excluding the memory required to store the output list `out`. If accounting for the result storage, space complexity is $O(k)$ where $k$ is the number of unique triplets found (up to $O(n^2)$).

## 🕵️‍♂️ Follow-up Questions (Optional)

**Q1: How can this solution be optimized to run in $O(n^2)$ time?**
> **Answer:** Sort the array first in $O(n \log n)$ time. Then, iterate through the array with a fixed index `i` and use a Two-Pointer approach (`left` and `right`) for the remaining subarray to find pairs that sum to `-nums[i]`. Duplicates can be skipped efficiently by incrementing/decrementing pointers when consecutive elements are identical, eliminating the need for `if curr not in out`.

**Q2: Why is `curr not in out` inefficient, and how can duplicate checking be optimized?**
> **Answer:** In Python, checking membership in a list (`not in list`) takes linear $O(M)$ time where $M$ is the length of the list. To optimize this without changing the general approach structure, a `set` of tuples could be used for $O(1)$ average lookup time, or sorting the input array initially allows skipping adjacent identical numbers during iteration without dynamic lookups.