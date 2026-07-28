<h2><a href="https://leetcode.com/problems/search-insert-position">35. Search Insert Position</a></h2>

<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Search-Insert-Position | Explained

## Approach 1: Binary Search with Post-Loop Boundary Check
### Intuition
Searching through a sorted array efficiently is analogous to searching for a word in a physical dictionary. Rather than scanning page-by-page from the beginning (Linear Search), you open to the middle page. If the target word comes before the current page alphabetically, you eliminate the entire right half of the book. If it comes after, you eliminate the left half. 

By repeatedly cutting the remaining search space in half, you can locate the target—or determine exact insertion point if it does not exist—in logarithmic time. When the target is missing, the search pointers converge right at the spot where the value belongs.

### Algorithm Visualized

```mermaid
flowchart TD
    Start([Start: searchInsert]) --> Init[Initialize left = 0, right = n - 1]
    Init --> LoopCond{Is left <= right?}
    
    LoopCond -- Yes --> CalcMid["Calculate mid = (left + right) // 2"]
    CalcMid --> CheckEqual{Is target == nums[mid]?}
    
    CheckEqual -- Yes --> ReturnMid[Return mid]
    CheckEqual -- No --> CheckLess{Is target < nums[mid]?}
    
    CheckLess -- Yes --> MoveRight["right = mid - 1"]
    CheckLess -- No --> MoveLeft["left = mid + 1"]
    
    MoveRight --> LoopCond
    MoveLeft --> LoopCond
    
    LoopCond -- No --> PostCheck{Is target > nums[mid]?}
    PostCheck -- Yes --> ReturnMidPlusOne[Return mid + 1]
    PostCheck -- No --> ReturnMidPost[Return mid]
```

### Approach
1. **Initialize Pointers**: Set the search boundary using `left = 0` and `right = len(nums) - 1`.
2. **Binary Search Iteration**: Loop while `left <= right`:
   - Compute `mid` as the floor division of `(left + right) // 2`.
   - **Target Found**: If `nums[mid] == target`, immediately return `mid`.
   - **Target in Left Half**: If `target < nums[mid]`, narrow the search space to the left by updating `right = mid - 1`.
   - **Target in Right Half**: If `target > nums[mid]`, narrow the search space to the right by updating `left = mid + 1`.
3. **Post-Loop Insertion Resolution**: If the target was not found in the loop, `mid` retains the index of the last element examined (leveraging Python's function-level variable scoping). Compare `target` with `nums[mid]`:
   - If `target > nums[mid]`, the insertion spot is immediately after `mid` (`mid + 1`).
   - Otherwise, the target belongs at index `mid`.

### Detailed Code Analysis

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
```
- **Lines 3–5**: We calculate `n`, the size of the array, and initialize our search boundary variables `left` and `right` to point to the first (`0`) and last (`n - 1`) indices, respectively.

```python
        while left <=right:
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid] :
                right=mid-1
            elif target > nums[mid]:
                left=mid+1
```
- **Line 7**: The `while left <= right` condition ensures we search as long as there is a valid range of elements to inspect.
- **Line 8**: `mid = (left+right)//2` computes the middle index.
- **Lines 9–10**: Checks for an exact match. If found, returns `mid` immediately.
- **Lines 11–12**: If the target is smaller than the middle element, the target must reside in the left sub-array. We adjust `right = mid - 1`.
- **Lines 13–14**: If the target is larger than the middle element, it must reside in the right sub-array. We adjust `left = mid + 1`.

```python
        if target > nums[mid]:
            return mid+1
        else:
            return mid
```
- **Lines 16–19**: After the loop terminates (`left > right`), `target` was not present in `nums`. Because Python does not have block scope for loop variables, `mid` remains accessible. 
- The code compares `target` against `nums[mid]` (the last evaluated mid-point element) to decide whether to insert at `mid + 1` or `mid`.

> 💡 **Engineering Note**: While the post-loop `if target > nums[mid]` check produces correct results, in standard binary search, when the loop terminates without finding `target`, `left` **always** points to the correct insertion index. You can simplify lines 16–19 down to simply `return left`.

### Code

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        if target > nums[mid]:
            return mid + 1
        else:
            return mid
```

### Complexity
- **Time Complexity:** $\mathcal{O}(\log n)$ — In each iteration of the `while` loop, the search range $[left, right]$ is divided in half. For an array of size $n$, the maximum number of iterations required is $\lfloor\log_2 n\rfloor + 1$.
- **Space Complexity:** $\mathcal{O}(1)$ — Memory usage is constant as the algorithm only uses integer variables (`n`, `left`, `right`, `mid`) regardless of input array size.

---

## 🕵️‍♂️ Follow-up Questions

### 1. Why is returning `left` directly after the loop considered cleaner than comparing `target > nums[mid]`?
When a classic binary search loop `while left <= right` terminates naturally without finding the target, the pointers cross such that `left = right + 1`. 
- `left` represents the count of elements strictly smaller than `target` in the array.
- Consequently, `left` naturally points to the exact zero-based index where `target` should be inserted to maintain sorted order. Replacing lines 16–19 with `return left` eliminates the need to rely on post-loop variable state.

### 2. How do you prevent integer overflow in languages like C++ or Java when calculating `mid`?
In languages with fixed-size integers (e.g., 32-bit signed integers in C++ or Java), `left + right` can exceed $2^{31} - 1$ if the array is extremely large, causing an integer overflow. To fix this, calculate `mid` using:
$$\text{mid} = \text{left} + \frac{\text{right} - \text{left}}{2}$$
In Python 3, integers have arbitrary precision and automatically grow to fit large values, so overflow isn't an issue, but using this formula is considered industry best practice across all languages.