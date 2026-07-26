<h2><a href="https://leetcode.com/problems/remove-element">27. Remove Element</a></h2>

<p>Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a>. The order of the elements may be changed. Then return <em>the number of elements in </em><code>nums</code><em> which are not equal to </em><code>val</code>.</p>

<p>Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:</p>

<ul>
	<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
	<li>Return <code>k</code>.</li>
</ul>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i &lt; actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,2,3], val = 3
<strong>Output:</strong> 2, nums = [2,2,_,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,2,2,3,0,4,2], val = 2
<strong>Output:</strong> 5, nums = [0,1,4,0,3,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 100</code></li>
</ul>


---

# 🛍️ Remove-Element | Explained

## Approach 1: Two Pointers (Fast & Slow Pointers)

### Intuition
Imagine you are a teacher organizing a line of students, where some students are wearing red shirts (`val`) and need to be removed from the line, while everyone else remains. Instead of creating a second line from scratch, you walk down the line with a write-marker (`left` pointer) and a reading eye (`right` pointer). 

Every time your reading eye sees a student *not* wearing a red shirt, you move that student up to the position marked by your write-marker and increment the marker. If you encounter a red shirt, you simply ignore it and move your reading eye to the next person. By the end of the line, all non-red-shirt students have been consolidated at the front of the line, and your write-marker indicates the exact number of valid students.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start Loop: right from 0 to n-1]) --> CheckVal{nums[right] != val?}
    CheckVal -- Yes --> Overwrite[Copy: nums[left] = nums[right]]
    Overwrite --> IncrementLeft[Increment: left += 1]
    IncrementLeft --> NextIter[Next Iteration]
    CheckVal -- No --> NextIter
    NextIter --> IsDone{right == n - 1?}
    IsDone -- No --> Start
    IsDone -- Yes --> End([Return left])
```

### Approach
1. Initialize a pointer `left = 0` to serve as the write index for elements that do not equal `val`.
2. Iterate through the array using a `right` pointer (serving as the read index) from index `0` to `n - 1`.
3. At each index `right`, check if `nums[right]` is equal to target `val`:
   - If `nums[right] != val`, overwrite `nums[left]` with `nums[right]` and increment `left` by `1`.
   - If `nums[right] == val`, skip it and do not increment `left`.
4. Once the loop finishes, the first `left` elements of `nums` contain all valid elements in their updated order.
5. Return `left`, which represents the length of the modified array.

### Detailed Code Analysis

- **Lines 3–4: `n = len(nums)` & `left = 0`**
  - We calculate `n`, the length of the input list `nums`, to set upper bounds for iteration.
  - `left` is initialized to `0`. It acts as the "write pointer" indicating where the next valid element (an element not equal to `val`) should be placed.

- **Line 5: `for right in range(n):`**
  - We loop through every index of the list using `right` as our "read pointer".

- **Lines 6–8: `if nums[right] != val:` block**
  - We evaluate whether the current element `nums[right]` should be kept.
  - If `nums[right] != val`, we assign `nums[left] = nums[right]`. This overwrites any undesirable target values at index `left` with a valid value from index `right`.
  - We then execute `left += 1` to advance the write pointer to the next available slot.
  - If `nums[right] == val`, the `if` block is skipped entirely. `left` remains at its current position while `right` continues forward, effectively skipping the unwanted element.

- **Line 11: `return left`**
  - After examining all elements, `left` holds the total count of elements that were not equal to `val`.
  - LeetCode's judge reads the array up to index `left - 1` to verify correctness.

### Code

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        left = 0
        for right in range(n):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1       

        return left
```

### Complexity

- **Time:** $\mathcal{O}(n)$, where $n$ is the length of `nums`. We traverse the list exactly once with the `right` pointer.
- **Space:** $\mathcal{O}(1)$ auxiliary space. The modification is done entirely in-place without allocating additional memory structures.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

**1. What if elements to remove are rare? Is there an optimized two-pointer variation?**
*Answer:* Yes. If the target `val` appears rarely, the current fast-slow pointer approach performs unnecessary copy operations (e.g., copying elements to themselves when `left == right`). Instead, we can use two pointers starting from opposite ends (`left = 0` and `right = len(nums) - 1`). When `nums[left] == val`, we swap/overwrite `nums[left]` with the last element `nums[right]` and decrement `right`. This avoids redundant writes when few elements match `val`.

**2. Does the order of elements matter in this problem?**
*Answer:* According to the problem constraints on LeetCode, the order of elements can be changed. This flexibility allows both the fast-slow pointer approach and the opposite-ends pointer approach to be valid $\mathcal{O}(n)$ in-place solutions.