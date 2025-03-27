---
comments: true
difficulty: easy
# Follow `Topics` tags
tags:
    - Array
    - Two Pointers
    - Dynamic Programming
    - Stack
    - Monotonic Stack
---

# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)

## Description

Given an elevation map with width of 1 which representing by `n` non-negative integers. Calculate amount of water that can be trapped after rainfall.

**Example 1:**
```
Input: height = [0,1,0,0,1,0,1,3,2,0,1]
Output: 4
Explanation: [1,0,0,1] can trapped 2 units, [1,0,1] can trapped 1 units, [2,0,1] can trapped 1 units.
```

**Example 2:**
```
Input: height = [4,1,2,4,5]
Output: 5
Explanation: [4,1,2,4] can trapped 5 units.
```


**Constraints:**
`n == height.length`
`1 <= n <= 2 * 10^4`
`0 <= height[i] <= 10^5`

## Solution

Shrink from the border. If the outside is higher than the inside, rain will accumulate. Therefore, the difference between the higher and lower bars represents the amount of retained rainwater.


```java
class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = height[left], rightMax = height[right];
        int water = 0;

        while (left < right) {
            if (leftMax < rightMax) {
                left++;
                leftMax = Math.max(leftMax, height[left]);
                water += leftMax - height[left];
            } else {
                right--;
                rightMax = Math.max(rightMax, height[right]);
                water += rightMax - height[right];
            }
        }
        return water;
    }
}
```

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
