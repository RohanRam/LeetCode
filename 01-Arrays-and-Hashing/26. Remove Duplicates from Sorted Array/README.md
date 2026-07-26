<h2><a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array">26. Remove Duplicates from Sorted Array</a></h2>

<p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><strong>in-place</strong></a> such that each unique element appears only <strong>once</strong>. The <strong>relative order</strong> of the elements should be kept the <strong>same</strong>.</p>

<p>Consider the number of <em>unique elements</em> in&nbsp;<code>nums</code> to be <code>k<strong>​​​​​​​</strong></code>​​​​​​​. After removing duplicates, return the number of unique elements&nbsp;<code>k</code>.</p>

<p>The first&nbsp;<code>k</code>&nbsp;elements of&nbsp;<code>nums</code>&nbsp;should contain the unique numbers in <strong>sorted order</strong>. The remaining elements beyond index&nbsp;<code>k - 1</code>&nbsp;can be ignored.</p>

<p><strong>Custom Judge:</strong></p>

<p>The judge will test your solution with the following code:</p>

<pre>int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i &lt; k; i++) {
    assert nums[i] == expectedNums[i];
}
</pre>

<p>If all assertions pass, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 2, nums = [1,2,_]
<strong>Explanation:</strong> Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,0,1,1,1,2,2,3,3,4]
<strong>Output:</strong> 5, nums = [0,1,2,3,4,_,_,_,_,_]
<strong>Explanation:</strong> Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


---

# 🛍️ Remove-Duplicates-from-Sorted-Array | Explained

## Approach 1: Two-Pointer Technique (Read/Write Pointers)

### Intuition
Think of this problem like organizing a row of books on a narrow shelf where identical copies are stacked side by side. You want to consolidate the shelf so that all unique books sit at the front, while duplicate copies are pushed to the end or overwritten.

Since the input array is already sorted, duplicate values are guaranteed to be contiguous (adjacent to one another). We can maintain two pointers:
1. **`left` (Write Pointer):** Marks the boundary of our "unique elements" sub-array. Everything up to index `left` contains unique, sorted elements.
2. **`right` (Read Pointer):** Scans through the rest of the array looking for the next distinct element.

When the `right` pointer encounters an element different from `nums[left]`, we advance `left` by one position and copy the new unique element into `nums[left]`. This overwrites duplicates in-place without needing extra space.

### Algorithm Visualized

```mermaid
graph TD
    Start([Start Loop: right = 1]) --> CheckLoop{right < n?}
    CheckLoop -- No --> ReturnLen[Return left + 1]
    CheckLoop -- Yes --> Compare{nums[left] != nums[right]?}
    
    Compare -- Yes (New Unique Element) --> IncrementLeft[left = left + 1]
    IncrementLeft --> Overwrite[nums[left] = nums[right]]
    Overwrite --> IncrementRight[right = right + 1]
    
    Compare -- No (Duplicate Found) --> IncrementRight
    IncrementRight --> CheckLoop
```

### Approach
1. **Edge Case Guard:** Check if the length of the array `n` is `0`. If so, return `0` immediately as there are no elements to process.
2. **Pointer Initialization:** Initialize `left = 0`. The element at index `0` is inherently the first unique value.
3. **Array Scanning:** Loop `right` from index `1` to `n - 1`.
4. **Duplicate Verification:**
   - If `nums[left] != nums[right]`, we have discovered a new unique value.
   - Advance `left` by `1` (`left += 1`).
   - Copy `nums[right]` into position `nums[left]`.
5. **Return Result:** After `right` completes its traversal, the unique portion of the array occupies indices `0` through `left`. The count of unique elements is therefore `left + 1`.

### Detailed Code Analysis

Let's break down the execution line-by-line against the provided solution:

```python
2    def removeDuplicates(self, nums: List[int]) -> int:
3        n=len(nums)
```
- **Lines 2–3:** We calculate the length of `nums` and store it in variable `n`. Storing `n` avoids redundant function calls to `len()` inside loop bounds.

```python
5        if n==0:
6            return 0
```
- **Lines 5–6:** Guard statement for empty inputs. If the input list `nums` contains no elements (`n == 0`), the function returns `0`.

```python
8        left=0
```
- **Line 8:** Sets the write pointer `left` to index `0`. The first element of a non-empty sorted array is always unique relative to what comes before it.

```python
10        for right in range(1,n):
11            if nums[left] != nums[right]:
12                left += 1
13                nums[left] = nums[right]
```
- **Line 10:** The `for` loop initializes the read pointer `right` at index `1` and iterates sequentially up to `n - 1`.
- **Line 11:** Checks if the value at the current scan index (`nums[right]`) is different from the value at the last written unique index (`nums[left]`).
- **Line 12:** If a new distinct value is found, `left` moves one step to the right to open a spot for the new unique value.
- **Line 13:** Overwrites the element at `nums[left]` with `nums[right]`. This compresses the array in-place, eliminating duplicate slots.

```python
15        return left+1
```
- **Line 15:** Returns `left + 1`. Because arrays are 0-indexed, an index of `left` means there are `left + 1` unique elements positioned at the start of `nums`.

### Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        left = 0

        for right in range(1, n):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1
```

### Complexity

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of elements in the array `nums`. The read pointer `right` traverses the array from index `1` to $N-1$ exactly once. Each comparison and array mutation operation occurs in $\mathcal{O}(1)$ time.
- **Space Complexity:** $\mathcal{O}(1)$ auxiliary space. The algorithm modifies the input array in-place and only allocates a fixed set of scalar pointer variables (`n`, `left`, `right`), requiring constant memory.

---

## 🕵️‍♂️ Follow-up Questions

### 1. What if duplicates are allowed to appear at most twice (e.g., LeetCode 80 - "Remove Duplicates from Sorted Array II")?
**Answer:** Instead of comparing `nums[right]` against `nums[left]`, compare `nums[right]` against `nums[left - 1]`. By looking back two positions instead of one, you allow up to two occurrences of any value while maintaining the same linear time and $\mathcal{O}(1)$ space footprint.

### 2. Can you solve this problem if the array is NOT sorted?
**Answer:** No, not in $\mathcal{O}(N)$ time with $\mathcal{O}(1)$ space. If the array is unsorted, duplicate elements could be spread arbitrarily across the array. You would either need:
- A Hash Set to track seen elements in $\mathcal{O}(N)$ time and $\mathcal{O}(N)$ space.
- Sorting the array first in $\mathcal{O}(N \log N)$ time and $\mathcal{O}(1)$ space before applying this two-pointer approach.