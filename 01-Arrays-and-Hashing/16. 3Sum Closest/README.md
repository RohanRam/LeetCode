<h2><a href="https://leetcode.com/problems/3sum-closest">16. 3Sum Closest</a></h2>

<p>Given an integer array <code>nums</code> of length <code>n</code> and an integer <code>target</code>, find three integers at <strong>distinct indices</strong> in <code>nums</code> such that the sum is closest to <code>target</code>.</p>

<p>Return <em>the sum of the three integers</em>.</p>

<p>You may assume that each input would have exactly one solution.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-1,2,1,-4], target = 1
<strong>Output:</strong> 2
<strong>Explanation:</strong> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,0], target = 1
<strong>Output:</strong> 0
<strong>Explanation:</strong> The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 500</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ 3Sum-Closest | Explained

## Approach 1: Sorting + Two-Pointer Search
### Intuition
Imagine you are shopping with a gift card worth a specific target amount (say, $100), and you must pick exactly three items from a catalog to get as close to that target sum as possible without needing an exact match. 

If the items are randomly ordered, you would have to check every possible combination of three items, which becomes extremely slow as the catalog grows. However, if you sort the catalog by price from cheapest to most expensive, you can make intelligent decisions:
1. Fix one item first.
2. Pick the cheapest available item (left pointer) and the most expensive available item (right pointer).
3. If their total sum is too large compared to your target, you swap the most expensive item for a cheaper one (decrement right pointer).
4. If their total sum is too small, you swap the cheapest item for a pricier one (increment left pointer).

By sorting the array first, we gain directional control over our search, reducing what would otherwise be an $O(N^3)$ brute-force check into a much more efficient $O(N^2)$ search.

### Algorithm Visualized
```mermaid
flowchart TD
    Start[Start: Sort array 'nums'] --> LoopI[Loop 'i' from 0 to n-3]
    LoopI --> SetPointers[Set left = i + 1, right = n - 1]
    SetPointers --> CheckWhile{left < right?}
    
    CheckWhile -- No --> NextI[End Inner Loop: Next 'i']
    NextI --> CheckOuterDone{i finished?}
    CheckOuterDone -- Yes --> ReturnBest[Return best closest sum 'sumArr']
    CheckOuterDone -- No --> LoopI
    
    CheckWhile -- Yes --> CalcSum[Calculate csum = nums[i] + nums[left] + nums[right]]
    CalcSum --> CheckExact{csum == target?}
    
    CheckExact -- Yes --> ReturnExact[Return csum immediately]
    CheckExact -- No --> MovePointers{csum > target?}
    
    MovePointers -- Yes --> DecRight[right = right - 1]
    MovePointers -- No --> IncLeft[left = left + 1]
    
    DecRight --> CalcDiff[Calculate cdiff = |csum - target|]
    IncLeft --> CalcDiff
    
    CalcDiff --> CheckBest{cdiff < diff?}
    CheckBest -- Yes --> UpdateBest[Update diff = cdiff, sumArr = csum]
    CheckBest -- No --> CheckWhile
    UpdateBest --> CheckWhile
```

### Approach
1. **Initialize Tracking Variables:** 
   Maintain two tracking variables: `diff` to keep track of the smallest absolute difference found so far, and `sumArr` to record the specific 3-element sum that yielded that smallest difference.
2. **Sort the Array:** 
   Sort `nums` in ascending order. This enables the two-pointer technique.
3. **Outer Loop (Fix the first element):**
   Iterate an index `i` from `0` to `n - 3`. Element `nums[i]` acts as the fixed first value of the triplet.
4. **Inner Two-Pointer Loop (Find the remaining two elements):**
   Initialize two pointers: `left = i + 1` (starting just after `i`) and `right = n - 1` (starting at the end of the array).
   While `left < right`:
   - Compute `csum = nums[i] + nums[left] + nums[right]`.
   - If `csum == target`, return `csum` immediately because a difference of `0` cannot be improved upon.
   - If `csum > target`, move `right` leftward (`right -= 1`) to reduce the sum.
   - If `csum < target`, move `left` rightward (`left += 1`) to increase the sum.
   - Calculate the absolute difference `cdiff = abs(csum - target)`.
   - If `cdiff < diff`, update `diff` and store `sumArr = csum`.
5. **Return Best Result:**
   After examining all relevant combinations, return `sumArr`.

### Detailed Code Analysis

Let's dissect the provided Python implementation line-by-line:

- **Lines 3–4:**
  ```python
  sumArr=0
  diff=9999999
  ```
  `sumArr` holds the closest triplet sum found. `diff` is initialized to a large sentinel integer (`9999999`) representing infinity, ensuring that any valid initial triplet difference will be smaller and trigger an update.

- **Lines 6–7:**
  ```python
  nums.sort()
  n=len(nums)
  ```
  `nums.sort()` sorts the input array in-place in $O(N \log N)$ time using Python's Timsort algorithm. `n` captures the total number of elements.

- **Line 9:**
  ```python
  for i in range(0,n-2):
  ```
  This loop iterates through all possible positions for the first element of the triplet. It stops at `n-3` (represented as `n-2` in Python's exclusive `range`), leaving at least two elements (`left` and `right`) to form a valid triplet.

- **Lines 10–11:**
  ```python
  left=i+1
  right=n-1
  ```
  Sets up the two pointers for the remaining sub-array range `[i + 1, n - 1]`.

- **Line 13:**
  ```python
  while left < right :
  ```
  Drives the two-pointer search. Runs as long as the two pointers do not cross.

- **Line 14:**
  ```python
  csum =nums[i] + nums[left] + nums[right] 
  ```
  Calculates the current triplet sum (`csum`).

- **Lines 15–20:**
  ```python
  if csum > target:
      right-=1
  elif csum < target:
      left+=1
  else:
      return csum
  ```
  Adjusts the search range based on `csum`:
  - If `csum > target`, decrement `right` to try smaller values.
  - If `csum < target`, increment `left` to try larger values.
  - If `csum == target`, return `csum` directly as an early exit optimization.

- **Lines 21–25:**
  ```python
  cdiff=abs(csum-target)

  if cdiff < diff :
      diff=cdiff
      sumArr = csum
  ```
  Computes `cdiff` (the distance between `csum` and `target`). If `cdiff` is strictly smaller than our record `diff`, we update `diff` and set `sumArr` to `csum`.

- **Line 28:**
  ```python
  return sumArr
  ```
  Returns the best sum found across all iterations.

### Code
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sumArr=0
        diff=9999999

        nums.sort()
        n=len(nums)

        for i in range(0,n-2):
            left=i+1
            right=n-1

            while left < right :
                csum =nums[i] + nums[left] + nums[right] 
                if csum > target:
                    right-=1
                elif csum < target:
                    left+=1
                else:
                    return csum
                cdiff=abs(csum-target)

                if cdiff < diff :
                    diff=cdiff
                    sumArr = csum

        return sumArr
```

### Complexity
- **Time Complexity:** $\mathcal{O}(N^2)$
  - Sorting the array takes $\mathcal{O}(N \log N)$ time.
  - The outer loop runs $N - 2$ times. Inside, the two pointers `left` and `right` traverse the remaining elements at most $N$ times per outer loop iteration, taking $\mathcal{O}(N)$ time.
  - Overall time complexity: $\mathcal{O}(N \log N + N^2) = \mathcal{O}(N^2)$.
- **Space Complexity:** $\mathcal{O}(1)$ or $\mathcal{O}(N)$
  - Python's built-in `sort()` (Timsort) uses up to $\mathcal{O}(N)$ additional space in the worst case to store temporary runs.
  - Outside of the sorting space, the algorithm only uses a constant amount of extra memory ($\mathcal{O}(1)$) for pointers and scalar variables (`sumArr`, `diff`, `left`, `right`, `csum`, `cdiff`).

---

## 🕵️‍♂️ Follow-up Questions

### 1. How can we optimize this solution further to avoid unnecessary iterations on duplicate numbers?
**Answer:** Similar to the standard 3Sum problem, if the array contains repeated consecutive numbers (e.g., `[1, 1, 1, 2, 3]`), we can skip identical values for `nums[i]`, `nums[left]`, and `nums[right]`. 
For instance, after processing `nums[i]`, if `nums[i] == nums[i - 1]`, we can `continue` directly to the next iteration. Similarly, when moving `left` and `right`, we can skip duplicate elements to save inner-loop cycles.

### 2. Is setting a hardcoded magic number like `diff = 9999999` safe? How should it be handled in production?
**Answer:** Hardcoded sentinel values like `9999999` are risky because problem constraints could theoretically make `abs(csum - target)` larger than `9999999` (e.g., if array values or `target` are around $10^5$, three elements summed could exceed this). In production code, standard practice is to use `float('inf')` or `math.inf` in Python, or initialize `diff` using the absolute difference of the very first triplet (`abs(nums[0] + nums[1] + nums[2] - target)`).