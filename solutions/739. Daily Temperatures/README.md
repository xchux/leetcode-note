---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Array
    - Stack
    - Monotonic Stack
---

# [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description/)

## Description

You're given an array of integers `temperatures`, where each element represents the temperature of a specific day.
Return a new array `answer` such that `answer[i]` indicates how many days you must wait after the i-th day to experience a warmer temperature.
If there’s no future day with a warmer temperature, set `answer[i]` to `0`.

**Example 1:**
```
Input: temperatures = [71,73,77,61,73,75,73]
Output:  [1,1,3,1,1,0,0]
```

**Example 2:**
```
Input: temperatures = [10,20,30]
Output: [1,1,0]
```

**Constraints:**

* `1 <= n <= 8`

## Solution

We use a monotonic stack to track temperatures:
1. Stack stores indices of temperatures in decreasing order
2. When we find a warmer temperature, we pop indices from stack and calculate waiting days
3. The waiting days are the difference between current index and popped index
4. Any temperatures without a warmer day ahead remain in stack (result stays 0)

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] result = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int index = stack.pop();
                result[index] = i - index;
            }
            stack.push(i);
        }

        return result;
    }
}
```

```python
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res
```

## Complexity

- Time complexity: $$O(n)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
