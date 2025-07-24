---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Array
    - Binary Search
---

# [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

## Description

You are given an array `nums` of length **n** that was originally sorted in ascending order but then rotated between 1 and **n** times. For example:

* `[0,1,2,4,5,6,7]` rotated 4 times becomes `[4,5,6,7,0,1,2]`.
* `[0,1,2,4,5,6,7]` rotated 7 times remains `[0,1,2,4,5,6,7]`.

A single rotation moves the last element to the front:
`[a[0], a[1], …, a[n-1]]` → `[a[n-1], a[0], a[1], …, a[n-2]]`.

Given such a rotated, sorted array of unique elements, return the **minimum element**.

The solution must run in **O(log n)** time complexity.

**Example 1:**
```
Input: nums = [10, 11 ,12 8, 9]
Output: 8
```

**Example 2:**
```
Input: nums = [4, 0, 1, 2, 3]
Output: 0
```

**Constraints:**

* `n == nums.length`
* `1 <= n <= 5000`
* `-5000 <= nums[i] <= 5000`
* All the integers of `nums` are unique.
* `nums` is sorted and rotated between `1` and `n` times.

## Solution


```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(nums[mid] > nums[right]){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        return nums[left];
    }
}
```

```python
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

## Complexity

- Time complexity: $$O(logn)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

