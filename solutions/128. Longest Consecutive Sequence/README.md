---
comments: true
difficulty: mediuum
# Follow `Topics` tags
tags:
    - Array
    - Hash Table
    - Union Find
---

# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)

## Description
Input is unsorted array integers, return the longest consecutive elements count.

**Example 1:**
```
Input: nums = [9,2,41,3,5,4]
Output: 4
```
The longest consecutive elements is `[2, 3, 4, 5]`. Therefore its count is 4.

**Constraints:**

`0 <= nums.length <= 10^5`

`-10^9 <= nums[i] <= 10^9`


## Solution
For efficiency check num exist, conver nums to set.

Then loop and check the consecutive count. 

Avoid duplicate checking num which in the middle of consecutive sqeuence, skip the check when `num - 1` exist.

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        int longest = 0;
        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
```

## Complexity

- Time complexity: $O(n)$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $O(n)$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

