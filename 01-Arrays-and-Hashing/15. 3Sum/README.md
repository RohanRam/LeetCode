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

## Approach 1: Sorting + Two-Pointer Convergence
### Intuition
Imagine you are at a gym rack with dumbbells of various positive and negative calibrated weights, and you need to find three weights that perfectly balance out to zero net weight. If the weights are scattered randomly, you would have to test every possible group of three—an inefficient $O(N^3)$ exhaustive search. 

However, if you first arrange the dumbbells in strict order from lightest (most negative) to heaviest (most positive), the problem becomes much simpler:
1. You fix one weight as your anchor (`nums[i]`).
2. To find the remaining two weights that cancel out `nums[i]`, you place one hand at the lightest available weight (`left`) and your other hand at the heaviest available weight (`right`).
3. If the combined sum is too heavy (greater than zero), you move your right hand to a lighter weight. If it is too light (less than zero), you move your left hand to a heavier weight.
4. Because the array is sorted, identical values cluster together, allowing you to easily skip duplicate values and avoid reporting redundant triplets.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: Input Array 'nums']) --> Sort[Sort 'nums' in non-decreasing order]
    Sort --> OuterLoop[Loop 'i' from 0 to n-3]
    
    OuterLoop --> CheckDupI{i > 0 AND<br>nums[i] == nums[i-1]?}
    CheckDupI -- Yes --> NextI[Continue to next 'i']
    NextI --> OuterLoop
    
    CheckDupI -- No --> InitPointers[Set left = i + 1<br>Set right = n - 1]
    
    InitPointers --> PointerLoop{left < right?}
    PointerLoop -- No --> NextI
    
    PointerLoop -- Yes --> CalcSum[total = nums[i] + nums[left] + nums[right]]
    
    CalcSum --> CheckSum{Compare 'total' to 0}
    
    CheckSum -- total > 0 --> DecRight[right = right - 1]
    DecRight --> PointerLoop
    
    CheckSum -- total < 0 --> IncLeft[left = left + 1]
    IncLeft --> PointerLoop
    
    CheckSum -- total == 0 --> AddResult[Append triplet to 'out']
    AddResult --> SkipLeftDup[While left < right AND<br>nums[left] == nums[left+1]:<br>left++]
    SkipLeftDup --> SkipRightDup[While right > left AND<br>nums[right] == nums[right-1]:<br>right--]
    SkipRightDup --> MoveBoth[left++, right--]
    MoveBoth --> PointerLoop
```

### Approach
1. **Sort the Input**: Sort `nums` in non-decreasing order. Sorting takes $O(N \log N)$ time and enables the directional two-pointer technique.
2. **Anchor Outer Loop**: Iterate index `i` from `0` to `n - 3`. This index fixes the first element `nums[i]` of potential triplets.
3. **Primary Duplicate Elimination**: Skip iteration if `i > 0` and `nums[i] == nums[i-1]`, as processing the same anchor value produces duplicate triplets.
4. **Two-Pointer Setup**: Set `left = i + 1` and `right = n - 1`.
5. **Sum Evaluation & Pointer Shrinking**:
   - Calculate `total = nums[i] + nums[left] + nums[right]`.
   - If `total > 0`, the sum is too large. Decrement `right` to reduce the sum.
   - If `total < 0`, the sum is too small. Increment `left` to increase the sum.
   - If `total == 0`, record `[nums[i], nums[left], nums[right]]` into the output array.
6. **Secondary Duplicate Elimination**: Once a valid triplet is found, skip duplicate values for both `left` and `right` using `while` loops, then increment `left` and decrement `right` once more to find new distinct combinations.

### Detailed Code Analysis

* **Lines 3–5 (`n=len(nums)`, `out=[]`, `nums.sort()`):**
  We cache the length of the list, initialize the dynamic array `out` to store matching triplets, and sort `nums` in-place using Python's Timsort algorithm.

* **Line 6 (`for i in range(n-2):`):**
  The outer loop runs up to `n - 3` (written as `range(n-2)`). We stop here because a valid triplet requires at least two remaining elements to the right of `i` (`left` and `right`).

* **Lines 7–8 (`if i>0 and nums[i] == nums[i-1]: continue`):**
  Handles primary duplicate prevention. Checking `i > 0` prevents out-of-bounds access on index `-1`. If the current anchor `nums[i]` matches the preceding anchor `nums[i-1]`, we skip it immediately.

* **Lines 10–11 (`left = i+1`, `right = n-1`):**
  Initializes two pointers defining a shrinking search space between `i + 1` and the last element of the list.

* **Line 13 (`while left < right:`):**
  Executes the two-pointer sweep until the bounds cross or meet.

* **Lines 14–18 (`total = ...`, `if total > 0: ... elif total < 0: ...`):**
  Computes the sum of the selected triplet. Because the array is sorted, shifting `right` leftward strictly non-increases `total`, while shifting `left` rightward strictly non-decreases `total`.

* **Lines 19–20 (`out.append(...)`):**
  Executes when `total == 0`. The triplet forms a valid result and is saved to the output list.

* **Lines 22–27 (`while left < right and nums[left] == nums[left+1]: ...`):**
  Eliminates duplicate triplets for the current anchor `nums[i]`:
  - Lines 22–23 advance `left` forward as long as `nums[left]` equals its right neighbor `nums[left+1]`.
  - Lines 24–25 move `right` backward as long as `nums[right]` equals its left neighbor `nums[right-1]`.
  - Lines 26–27 perform the final single step (`left += 1`, `right -= 1`) to position both pointers at completely new candidate values.

### Code

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        out=[]
        nums.sort()
        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right = right-1
                elif total < 0:
                    left = left+1
                else :
                    out.append([nums[i],nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left =left+1
                    while right > left and nums[right] == nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1
        
        return out
```

### Complexity
- **Time Complexity:** $\mathcal{O}(N^2)$
  - Sorting the array costs $\mathcal{O}(N \log N)$ time.
  - The outer loop runs $\mathcal{O}(N)$ times. For each iteration, the inner `while` loop moves `left` and `right` toward each other, traversing the remaining elements at most once ($\mathcal{O}(N)$ operations per outer step).
  - Overall time complexity: $\mathcal{O}(N \log N) + \mathcal{O}(N^2) = \mathcal{O}(N^2)$.

- **Space Complexity:** $\mathcal{O}(N)$
  - Python's `sort()` uses Timsort, which requires up to $\mathcal{O}(N)$ auxiliary memory space in the worst case.
  - Excluding the memory allocated for the returned answer (`out`), the auxiliary space complexity is $\mathcal{O}(N)$ due to sorting.

---

## 🕵️‍♂️ Follow-up Questions

### 1. How can we optimize this solution with early termination conditions?
Since the array is sorted, we can prune search branches early:
* **Positive Anchor Break:** If `nums[i] > 0`, break the loop immediately. Because the array is sorted, all subsequent numbers will also be strictly positive ($> 0$), making it impossible for three positive numbers to sum to $0$.
* **Minimum Sum Check:** If `nums[i] + nums[i+1] + nums[i+2] > 0`, break the loop. The smallest possible sum starting from `nums[i]` exceeds zero, so no further valid triplets exist.
* **Maximum Sum Check:** If `nums[i] + nums[n-2] + nums[n-1] < 0`, skip this iteration using `continue`. The largest possible sum incorporating `nums[i]` is still less than zero, meaning `nums[i]` is too small to participate in any zero-sum triplet.

### 2. Can 3Sum be solved without modifying the original input array?
Yes. If mutating the input array is prohibited (e.g., in a read-only concurrent system):
1. Create a sorted copy of the array using `sorted(nums)`, requiring $\mathcal{O}(N)$ additional space, and execute the two-pointer approach on the copy.
2. Alternatively, use a Hash Set pattern similar to 2Sum: for each fixed anchor `nums[i]`, iterate over `nums[j]` ($j > i$) and check if candidate `-(nums[i] + nums[j])` exists in a dynamically populated hash set. This avoids sorting the array directly, though handling duplicate triplets cleanly becomes trickier and typically requires sorting each individual triplet before inserting into a global result set.