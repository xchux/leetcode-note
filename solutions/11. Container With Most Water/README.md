---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - Array
    - Two Pointers
    - Greedy
---

# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

## Description

Given an integer array `height` of length `n`, where each element represents the height of a vertical line drawn at position `i`, with endpoints at `(i, 0)` and `(i, height[i])`, your task is to determine the maximum amount of water that can be contained between any two lines and the x-axis.

Return the maximum water volume that the container can store.

**Example 1:**
```
Input: height = [1,6,5,5,4,1,7,1]
Output: 36
Explanation: In this case, the max area of water ([6,5,5,4,1,7]) the container can contain is 36.
```

**Example 2:**
```
Input: nums = [2,2]
Output: 2
```


**Constraints:**
`n == height.length`
`2 <= n <= 10^5`
`0 <= height[i] <= 10^4`

## Solution

Simply put, we calculate the maximum area of ​​the rectangle and return it. The formula shrinks inward, with the highest point as the side.

```java
class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int maxArea = 0;
        while (left < right) {
            int area = (right - left) * Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, area);
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }
}
```

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
```


## Complexity

- Time complexity: $$O(n^2)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->

