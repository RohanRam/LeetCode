<h2><a href="https://leetcode.com/problems/set-mismatch">0000. Set Mismatch</a></h2>

<p>You have a set of integers <code>s</code>, which originally contains all the numbers from <code>1</code> to <code>n</code>. Unfortunately, due to some error, one of the numbers in <code>s</code> got duplicated to another number in the set, which results in <strong>repetition of one</strong> number and <strong>loss of another</strong> number.</p>

<p>You are given an integer array <code>nums</code> representing the data status of this set after the error.</p>

<p>Find the number that occurs twice and the number that is missing and return <em>them in the form of an array</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,2,4]
<strong>Output:</strong> [2,3]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,1]
<strong>Output:</strong> [1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


---

# 🛍️ Set-Mismatch | Explained

## Approach 1: Hash Map Frequency Tracking with Sorting
### Intuition
Imagine a classroom roll call where every student is assigned a unique locker number from $1$ to $n$. On this day, one student accidentally shouts out their locker number twice, causing another student's locker number to be left out entirely. 

To resolve the confusion, you keep a master sign-in sheet (`seen`). As you inspect each locker number, you check if it has already been checked off on your sheet. If it has, you immediately catch the duplicate student. Once you finish reviewing the entries, you cross-reference your sign-in sheet against the complete roster of expected numbers from $1$ to $n$ to identify who never answered.

### Algorithm Visualized
```mermaid
flowchart TD
    Start([Input: nums]) --> Sort[nums.sort]
    Sort --> Init[Initialize seen = {}, dup = 0, missing = 0]
    
    subgraph Pass1 [Pass 1: Find Duplicate]
        Init --> Loop1{For each num in nums}
        Loop1 -->|num in seen| FoundDup[dup = num]
        Loop1 -->|num not in seen| AddSeen[seen[num] = index]
        FoundDup --> Loop1
        AddSeen --> Loop1
    end

    Loop1 -->|Exhausted| Pass2
    
    subgraph Pass2 [Pass 2: Find Missing]
        Pass2[Loop i from 0 to len nums] --> CheckSeen{i in seen?}
        CheckSeen -->|No| SetMissing[missing = i]
        CheckSeen -->|Yes| NextI[Continue]
        SetMissing --> CheckLoop{i <= len nums?}
        NextI --> CheckLoop
        CheckLoop -->|Next i| CheckSeen
    end
    
    CheckLoop -->|Done| ReturnResult([Return dup, missing])
```

### Approach
1. **Sort the Input Array**: Sort `nums` in ascending order using Python's built-in Timsort.
2. **Track Seen Elements**: Traverse through the sorted array using a dictionary `seen`. For every number:
   - If the number is already present as a key in `seen`, it is the duplicate (`dup`).
   - Otherwise, insert the number into `seen` with its index as the value.
3. **Identify the Missing Number**: Iterate through all integers from `0` to `len(nums)`. Check whether each integer exists in `seen`. The integer absent from `seen` within the expected range $[1, n]$ is recorded as `missing`.
4. **Return Result**: Return the pair `[dup, missing]`.

### Detailed Code Analysis
- **Line 3 (`nums.sort()`):** Sorts `nums` in-place. While sorting arranges numbers in non-decreasing order, it is functionally redundant here because the subsequent lookup relies entirely on hash map key lookups rather than adjacent element comparisons.
- **Lines 4–6 (`seen = {}`, `dup=0`, `missing=0`):** Initializes the hash table `seen` to store previously encountered numbers alongside default sentinel values for `dup` and `missing`.
- **Lines 7–11 (`for i, num in enumerate(nums): ...`):**
  - Iterates over each item along with its index.
  - `if num in seen:` executes in average $O(1)$ time. If true, `dup` is assigned to `num`.
  - `else: seen[num] = i` records the number as seen, mapping it to its index in the array.
- **Lines 13–15 (`for i in range(len(nums)+1): ...`):**
  - Runs a loop from `0` to `n` inclusive.
  - Note on the loop range: Because the problem defines valid numbers in the range $[1, n]$, `i = 0` will trigger `0 not in seen`, temporarily setting `missing = 0`. However, as the loop proceeds, the true missing number $k \in [1, n]$ is also absent from `seen` and will overwrite `missing = k`. Because all other numbers from $1$ to $n$ exist in `seen`, `missing` correctly retains $k$.
- **Line 17 (`return [dup, missing]`):** Packs the duplicate and missing values into a list and returns it.

### Code
```python
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        nums.sort()
        seen = {}
        dup = 0
        missing = 0
        for i, num in enumerate(nums):
            if num in seen:
                dup = num
            else:
                seen[num] = i
        
        for i in range(len(nums) + 1):
            if i not in seen:
                missing = i
        
        return [dup, missing]
```

### Complexity
- **Time:** $O(N \log N)$
  - `nums.sort()` takes $O(N \log N)$ time using Timsort.
  - The first loop iterates $N$ times with $O(1)$ dictionary operations, taking $O(N)$.
  - The second loop iterates $N + 1$ times with $O(1)$ dictionary lookups, taking $O(N)$.
  - Total time complexity is dominated by the sort: $O(N \log N) + O(N) + O(N) = O(N \log N)$.
- **Space:** $O(N)$
  - The dictionary `seen` stores $N - 1$ unique values, requiring $O(N)$ auxiliary space.
  - In Python, `nums.sort()` can also require up to $O(N)$ working memory for Timsort.

## 🕵️‍♂️ Follow-up Questions (Optional)
1. **Can this be solved in $O(N)$ time without sorting?**
   - Yes. You can remove `nums.sort()` completely. A frequency array, hash set, or count array of size $N + 1$ identifies both the duplicate and the missing values in linear $O(N)$ time.
2. **Can this problem be solved in $O(1)$ auxiliary space?**
   - Yes. By utilizing the array elements as indices and negating the values at those indices (in-place sign marking), you can identify the duplicate when encountering an already negative value. A second scan identifies the missing number where the value remains positive. Alternatively, mathematical formulas (sum and sum of squares) or XOR bit manipulation can solve it in $O(N)$ time and $O(1)$ space.