---
comments: true
difficulty: hard
# Follow `Topics` tags
tags:
    - Array
    - Stack
    - Monotonic Stack
---

# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

## Description

You are given an array of integers heights, where each element represents the height of a bar in a histogram. Each bar has a width of 1.
Your task is to compute and return the area of the largest rectangle that can be formed within the bounds of the histogram.

**Example 1:**
```
Input: heights = [2,5,3,3]
Output: 9
Explanation: he above is a histogram where width of each bar is 1.
The largest rectangle is [5, 3, 3] area, which has an area = 9 units.
```

**Example 2:**
```
Input: heights = [3,4]
Output: 6
```

**Constraints:**

* `1 <= heights.length <= 10^5`
* `0 <= heights[i] <= 10^4`

## Solution

The key idea is using a monotonic stack to track bar indices. For each bar, we pop taller bars from stack to calculate rectangles, as they can't extend further. The stack maintains increasing heights, making it efficient to find the largest possible rectangle at each position.

```java
class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        stack.push(-1);

        for (int i = 0; i < heights.length; i++) {
            while (!stack.isEmpty() && stack.peek() != -1 && heights[stack.peek()] >= heights[i]) {
                int height = heights[stack.pop()];
                int width = i - stack.peek() - 1;
                maxArea = Math.max(maxArea, height * width);
            }
            stack.push(i);
        }

        while (stack.peek() != -1) {
            int height = heights[stack.pop()];
            int width = heights.length - stack.peek() - 1;
            maxArea = Math.max(maxArea, height * width);
        }
        return maxArea;
    }
}
```

```python
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        stack = [-1]
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
