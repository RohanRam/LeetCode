<h2><a href="https://leetcode.com/problems/next-permutation">31. Next Permutation</a></h2>

<p>A <strong>permutation</strong> of an array of integers is an arrangement of its members into a sequence or linear order.</p>

<ul>
	<li>For example, for <code>arr = [1,2,3]</code>, the following are all the permutations of <code>arr</code>: <code>[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]</code>.</li>
</ul>

<p>The <strong>next permutation</strong> of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the <strong>next permutation</strong> of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).</p>

<ul>
	<li>For example, the next permutation of <code>arr = [1,2,3]</code> is <code>[1,3,2]</code>.</li>
	<li>Similarly, the next permutation of <code>arr = [2,3,1]</code> is <code>[3,1,2]</code>.</li>
	<li>While the next permutation of <code>arr = [3,2,1]</code> is <code>[1,2,3]</code> because <code>[3,2,1]</code> does not have a lexicographical larger rearrangement.</li>
</ul>

<p>Given an array of integers <code>nums</code>, <em>find the next permutation of</em> <code>nums</code>.</p>

<p>The replacement must be <strong><a href="http://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in place</a></strong> and use only constant extra memory.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,3]
<strong>Output:</strong> [1,3,2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,1]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,5]
<strong>Output:</strong> [1,5,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


---

# 🛍️ Next-Permutation | Explained

## Approach 1: Single-Pass Swap and In-Place Reversal (Optimal)

### Intuition
To find the next lexicographically greater permutation, think of the array as a multi-digit number. We want to create the smallest number that is strictly larger than the current number. 

Imagine adjusting an odometer or a combination lock:
1. **Find where the sequence breaks its ascending order from right to left.** If a sequence is strictly decreasing from right to left (e.g., `[7, 4, 2, 1]`), no larger permutation can be formed using just those digits because it is already at its maximum possible arrangement.
2. **Find the pivot:** Moving from right to left, the first number that breaks this decreasing pattern (i.e., `nums[i] < nums[i+1]`) is our "pivot". Increasing this digit will give us the next larger overall permutation.
3. **Swap with the next larger candidate:** To make the increase as small as possible, we swap this pivot with the smallest number to its right that is still strictly greater than the pivot.
4. **Minimize the tail:** Once the swap is complete, the suffix to the right of our pivot position is still sorted in descending order. To make this new permutation as small as possible, we must turn this suffix into ascending order. Reversing a descending subarray turns it into ascending order in $O(N)$ time.

---

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: Array nums]) --> Step1[1. Scan right-to-left for Pivot 'i':<br/>Find first element where nums[i] < nums[i+1]]
    Step1 --> CheckPivot{Is i >= 0?}
    
    CheckPivot -- Yes --> Step2[2. Scan right-to-left for 'j':<br/>Find first element where nums[j] > nums[i]]
    Step2 --> Step3[3. Swap nums[i] and nums[j]]
    Step3 --> Step4[4. Reverse suffix from index i+1 to end]
    
    CheckPivot -- No <br/>(Entire array is descending) --> Step4
    Step4 --> End([End: In-place Next Permutation])
```

---

### Approach

1. **Find the Pivot ($i$):**
   - Start from the second to last element (`i = n - 2`) and move leftwards.
   - Stop at the first index `i` where `nums[i] < nums[i+1]`.
   
2. **Find the Swap Partner ($j$):**
   - If a valid pivot $i$ is found (`i >= 0`), search from the rightmost element (`j = n - 1`) moving left.
   - Stop at the first element `nums[j]` that is strictly greater than `nums[i]`.
   - Swap `nums[i]` and `nums[j]`.

3. **Reverse the Suffix:**
   - Reverse all elements from index `i + 1` up to `n - 1`. 
   - If no pivot was found (`i < 0`), the entire array was in descending order (maximum permutation). Reversing it from `i + 1` (index 0) converts it into the smallest permutation (fully sorted ascending order).

---

### Detailed Code Analysis

Let's break down the execution step-by-step using your exact code implementation:

#### 1. Setup Pointer and Search for the Pivot
```python
n = len(nums)
i = n - 2

while i >= 0 and nums[i] >= nums[i+1]:
    i -= 1
```
* **Lines 7–9:** We store the array length in `n` and initialize index `i` at `n - 2` because we compare `nums[i]` with `nums[i+1]`.
* **Lines 11–12:** The `while` loop iterates leftwards as long as the array continues to increase or stay equal when looking from right to left (`nums[i] >= nums[i+1]`). When this loop breaks, `i` points to the pivot element that breaks the descending suffix.

#### 2. Locating Swap Target and Performing Swap
```python
if i >= 0: 
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
```
* **Line 14:** We check `if i >= 0`. If `i == -1`, it means the entire sequence was descending (e.g., `[3, 2, 1]`), so we skip finding a swap element $j$ and jump directly to reversing the array.
* **Lines 15–17:** We set `j = n - 1` and decrement `j` until we find the rightmost element strictly greater than `nums[i]`.
* **Lines 18–20:** We perform a classic manual swap using a `temp` variable to exchange `nums[i]` and `nums[j]`.

#### 3. Reversing the Suffix
```python
left = i + 1
right = n - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```
* **Lines 22–23:** We initialize two pointers: `left` at `i + 1` (start of the suffix) and `right` at `n - 1` (end of the array).
* **Lines 25–29:** Using a standard two-pointer reverse pattern, we swap elements at `left` and `right`, incrementing `left` and decrementing `right` until they meet. This converts the descending suffix into ascending order in-place.

---

### Code

```python
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2: If pivot exists, find the element just larger than nums[i] and swap
        if i >= 0: 
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        
        # Step 3: Reverse the suffix starting from index i + 1
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

---

### Complexity

- **Time Complexity:** $\mathcal{O}(N)$
  - Scanning for the pivot $i$ takes at most $N$ operations.
  - Scanning for $j$ takes at most $N$ operations.
  - Reversing the suffix takes at most $N/2$ swaps.
  - Overall total time spent is bounded by $\mathcal{O}(N)$, where $N$ is the length of `nums`.

- **Space Complexity:** $\mathcal{O}(1)$
  - Modifies the array strictly in-place.
  - Only uses auxiliary pointer variables (`n`, `i`, `j`, `left`, `right`, `temp`).

---

## 🕵️‍♂️ Follow-up Questions

### 1. How would you modify this solution if duplicates are present in `nums`?
**Answer:** The current code **already handles duplicate elements correctly**.
- The pivot search condition `nums[i] >= nums[i+1]` correctly skips non-increasing sequences containing duplicate values (e.g., `[1, 5, 5, 1]`).
- The search for `j` using `nums[j] <= nums[i]` ensures we skip elements equal to `nums[i]` and only swap with an element that strictly increases the value at index `i`.

### 2. Can we implement "Previous Permutation" using the same logic pattern?
**Answer:** Yes, by reversing the comparison conditions:
1. Scan right-to-left for the first **increasing** element from the right (`nums[i] > nums[i+1]`).
2. Scan right-to-left for the first element strictly **smaller** than `nums[i]` (`nums[j] < nums[i]`).
3. Swap `nums[i]` and `nums[j]`.
4. Reverse the suffix from `i + 1` to `n - 1`.