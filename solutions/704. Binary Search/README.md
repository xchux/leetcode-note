---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - Array
    - Binary Search
---

# [704. Binary Search](https://leetcode.com/problems/binary-search/description/)

## Description

You are given a sorted array of integers `nums` (in ascending order) and an integer `target`.
Write a function to find the `target` in the array. If it exists, return its index; otherwise, return `-1`.

Your solution must have a time complexity of **O(log n)**.

**Example 1:**
```
Input: nums = [-1,1,4,6,9,15], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

**Example 2:**
```
Input: nums = [-1,1,4,6,9,15], target = 3
Output: -1
Explanation: 3 does not exist in nums so return -1
```

**Constraints:**

* `1 <= nums.length <= 10^4`
* `-10^4 < nums[i], target < 10^4`
* All the integers in `nums` are unique.
* `nums` is sorted in ascending order.

## Solution


```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}
```

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```

## Complexity

- Time complexity: $$O(log n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

