<h2><a href="https://leetcode.com/problems/longest-common-prefix">14. Longest Common Prefix</a></h2>

<p>Write a function to find the longest common prefix string amongst an array of strings.</p>

<p>If there is no common prefix, return an empty string <code>""</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> strs = ["flower","flow","flight"]
<strong>Output:</strong> "fl"
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> strs = ["dog","racecar","car"]
<strong>Output:</strong> ""
<strong>Explanation:</strong> There is no common prefix among the input strings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 200</code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 200</code></li>
	<li><code>strs[i]</code> consists of only lowercase English letters if it is non-empty.</li>
</ul>


---

# 🛍️ Longest-Common-Prefix | Explained

## Approach 1: Lexicographical Sorting and Boundary Comparison
### Intuition
Imagine organizing a physical dictionary of words alphabetically. Words that share the same starting characters will naturally cluster together. More importantly, the word at the very beginning of the sorted list and the word at the very end will have the maximum possible dissimilarity among all pairs in the list. 

Because the array is sorted lexicographically, if the first string and the last string share a prefix, every single string between them in the sorted array must also share that exact same prefix. Thus, instead of comparing all strings against each other, we only need to sort the list and compare the first string (`strs[0]`) with the last string (`strs[-1]`).

### Algorithm Visualized
```mermaid
flowchart TD
    A[Input: strs = ['flower', 'flow', 'flight']] --> B[Sort Array Lexicographically]
    B --> C["Sorted: ['flight', 'flow', 'flower']"]
    C --> D["Set s1 = strs[0] ('flight')<br/>Set s2 = strs[-1] ('flower')"]
    D --> E[Iterate index i from 0 to min len s1, s2]
    E --> F{s1[i] == s2[i]?}
    F -- Yes --> G[Append character to common]
    G --> E
    F -- No --> H[Break Loop]
    H --> I[Return common prefix: 'fl']
```

### Approach
1. Initialize an empty string variable `common` to accumulate the result.
2. Sort the array of strings `strs` in-place using standard lexicographical ordering.
3. Identify the first string `s1` (`strs[0]`) and the last string `s2` (`strs[-1]`).
4. Find the minimum length `x` between `s1` and `s2` to prevent index out-of-bounds errors.
5. Iterate through characters from index `0` up to `x - 1`:
   - If `s1[i]` matches `s2[i]`, append the character to `common`.
   - If a mismatch is encountered, break out of the loop immediately.
6. Return `common`.

### Detailed Code Analysis
- **Line 3 (`common = ""`):** Initializes the string accumulator. *(Note: Fixes the missing empty string literal from the submission).*
- **Line 4 (`strs.sort()`):** Sorts the list of strings in lexicographical (alphabetical) order in-place using Python's Timsort algorithm.
- **Line 5 (`n = len(strs)`):** Stores the length of the string array (unused in the remaining loop, but safe).
- **Line 6-7 (`s1 = strs[0]`, `s2 = strs[-1]`):** Selects the boundary elements after sorting.
- **Line 8 (`x = min(len(s1), len(s2))`):** Determines the maximum possible loop iterations by finding the shorter of the two boundary strings.
- **Line 9-13 (`for i in range(0, x): ...`):** Performs character-by-character comparison. Appends matching characters to `common` and terminates execution upon encountering the first mismatch.
- **Line 14 (`return common`):** Returns the accumulated common prefix.

### Code
```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        strs.sort()
        n = len(strs)
        s1 = strs[0]
        s2 = strs[-1]
        x = min(len(s1), len(s2))
        for i in range(0, x):
            if s1[i] == s2[i]:
                common = common + s1[i]
            else:
                break
        return common
```

### Complexity
- **Time:** $\mathcal{O}(N \cdot K \log N)$, where $N$ is the number of strings in the list and $K$ is the maximum length of a string. Sorting $N$ strings takes $\mathcal{O}(N \log N)$ string comparisons, and each comparison takes up to $\mathcal{O}(K)$ character checks. The subsequent loop takes $\mathcal{O}(K)$ time.
- **Space:** $\mathcal{O}(N)$ or $\mathcal{O}(\log N)$ auxiliary space, depending on Python's Timsort implementation memory footprint for sorting pointers in-place.

---

## 🕵️‍♂️ Follow-up Questions (Optional)

1. **How can this problem be solved in $\mathcal{O}(N \cdot K)$ time without sorting?**
   - **Vertical Scanning:** Compare character by character at each index across all strings simultaneously. Stop as soon as a mismatch or the end of any string is reached. This avoids the overhead of sorting entirely.

2. **What if the input array is read-only and memory allocation must be $\mathcal{O}(1)$?**
   - Use Horizontal Scanning or Vertical Scanning without mutating the input array or building intermediate strings until slicing the final output string.