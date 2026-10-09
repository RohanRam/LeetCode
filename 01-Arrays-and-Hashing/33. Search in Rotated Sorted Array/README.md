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

## Approach 1: Modified One-Pass Binary Search
### Intuition
Imagine you have a two-volume encyclopedia where the volumes were placed on a bookshelf out of order: Volume 2 is on the left, and Volume 1 is on the right (e.g., `[4, 5, 6, 7, 0, 1, 2]`). If you split this collection at any arbitrary book, at least one of the two halves will always be in perfect, unbroken alphabetical order. 

Because one half is guaranteed to be sorted, you can inspect its starting and ending titles to determine definitively if your target word falls within that section. 
- If the target falls within that sorted segment's boundary, you can safely discard the other half and restrict your search there.
- If it doesn't, the target *must* reside in the other half (which contains the inflection point/rotation pivot). 

This allows us to maintain the logarithmic halving property of standard binary search, even without the entire array being uniformly sorted.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: l = 0, r = len - 1]) --> CheckLoop{l <= r?}
    CheckLoop -- No --> NotFound([Return -1])
    CheckLoop -- Yes --> CalcMid[Calculate mid = l + r - l // 2]
    
    CalcMid --> CheckTarget{nums[mid] == target?}
    CheckTarget -- Yes --> Found([Return mid])
    CheckTarget -- No --> CheckSortedHalf{nums[l] <= nums[mid]?}
    
    %% Left half sorted branch
    CheckSortedHalf -- Yes: Left Half Sorted --> InLeftRange{nums[l] <= target < nums[mid]?}
    InLeftRange -- Yes --> MoveR1[r = mid - 1]
    InLeftRange -- No --> MoveL1[l = mid + 1]
    
    %% Right half sorted branch
    CheckSortedHalf -- No: Right Half Sorted --> InRightRange{nums[mid] < target <= nums[r]?}
    InRightRange -- Yes --> MoveL2[l = mid + 1]
    InRightRange -- No --> MoveR2[r = mid - 1]
    
    MoveR1 --> CheckLoop
    MoveL1 --> CheckLoop
    MoveL2 --> CheckLoop
    MoveR2 --> CheckLoop
```

### Approach
1. **Initialize Pointers:** Set two pointers, `l = 0` and `r = len(nums) - 1`.
2. **Loop Invariant:** While `l <= r`, calculate the midpoint `mid = l + (r - l) // 2`.
3. **Target Match:** Check if `nums[mid] == target`. If so, return `mid` immediately.
4. **Identify the Sorted Half:**
   - **Case A: Left half is sorted (`nums[l] <= nums[mid]`)**
     - Check if `target` falls strictly within the sorted left half: `nums[l] <= target < nums[mid]`.
     - If it does, eliminate the right half by setting `r = mid - 1`.
     - Otherwise, the target must be in the right half, so set `l = mid + 1`.
   - **Case B: Right half is sorted (`nums[l] > nums[mid]`)**
     - Check if `target` falls strictly within the sorted right half: `nums[mid] < target <= nums[r]`.
     - If it does, eliminate the left half by setting `l = mid + 1`.
     - Otherwise, the target must be in the left half, so set `r = mid - 1`.
5. **Element Absent:** If `l > r` without finding the target, return `-1`.

### Detailed Code Analysis

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
```
- **Lines 3–4:** We establish our two-pointer search space covering the full index range `[0, len(nums) - 1]`.

```python
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
```
- **Lines 5–8:** Standard binary search loop. Using `mid = l + (r - l) // 2` prevents potential 32-bit integer overflow (best practice, even though Python dynamically handles arbitrarily large integers). If `nums[mid]` matches `target`, we immediately terminate and return the index.

```python
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
```
- **Line 10 (`nums[l] <= nums[mid]`):** Determines if the left segment `nums[l...mid]` is monotonically increasing. The `<=` equality check is crucial to handle the edge case where `l == mid` (subarrays of size 1 or 2).
- **Line 11 (`nums[l] <= target < nums[mid]`):** If the left segment is sorted, we perform a straightforward range check. If the target falls between `nums[l]` (inclusive) and `nums[mid]` (exclusive), we discard the right half by contracting the upper bound: `r = mid - 1`.
- **Lines 13–14:** If the target does not lie in this sorted left range, it must be in the unsorted right segment; hence, `l = mid + 1`.

```python
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
```
- **Line 15:** If `nums[l] > nums[mid]`, the pivot exists in the left half, which means the right segment `nums[mid...r]` is guaranteed to be sorted.
- **Line 16 (`nums[mid] < target <= nums[r]`):** We verify whether `target` falls within the boundary of this sorted right segment.
- **Lines 17–19:** If it falls in the right segment, move `l = mid + 1`. Otherwise, search the left segment by moving `r = mid - 1`.

```python
        return -1
```
- **Line 20:** If the search window collapses (`l > r`) without a match, the target is not present in the array.

### Code
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
```

### Complexity
- **Time: $O(\log n)$** — At each iteration of the `while` loop, we eliminate exactly half of the remaining search space, matching the time complexity of classical binary search.
- **Space: $O(1)$** — The algorithm operates purely iteratively using constant auxiliary memory (`l`, `r`, `mid`).

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **What happens if the array contains duplicates (LeetCode 81)?**
   - If duplicates are introduced, the condition `nums[l] <= nums[mid]` no longer guarantees that the left half is sorted. For instance, in `[3, 1, 2, 3, 3, 3, 3]`, `nums[l] == nums[mid] == nums[r]`. In this scenario, we cannot deduce which side is sorted and must increment `l` (or decrement `r`) by 1 to skip duplicates, which degrades the worst-case time complexity to **$O(n)$**.

2. **Can this problem be solved using a two-pass binary search?**
   - Yes. Pass 1 finds the index of the minimum element (the rotation pivot) in $O(\log n)$ time. Pass 2 performs a standard binary search on either the left or right sorted subarray depending on which range `target` falls into. While asymptotically identical ($O(\log n)$), your one-pass approach is cleaner and requires fewer comparisons.