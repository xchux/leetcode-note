---
comments: true
difficulty: medium
# Follow `Topics` tags
tags:
    - Stack
    - Design
---

# [155. Min Stack](https://leetcode.com/problems/min-stack/description/)

## Description

Create a special type of stack called MinStack that, in addition to the usual stack operations, can also return the minimum element currently in the stack — all in constant time (O(1)).

The MinStack class should support the following operations:

1. `MinStack()`: Initializes a new instance of the stack.

2. `void push(int val)`: Adds the given value `val` to the top of the stack.

3. `void pop()`: Removes the top element from the stack.

4. `int top()`: Returns the element currently at the top of the stack.

5. `int getMin()`: Returns the smallest element in the stack at any given time.

Make sure that all these methods run in constant time.


**Example 1:**
```
Input:
["MinStack","push","push","top","push","getMin","pop","top","getMin"]
[[],[-1],[3],[],[-2],[],[],[],[]]

Output: [null,null,3,null,-2,null,3,-1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(-1);
minStack.push(3);
minStack.top();    // return 3
minStack.push(-2);
minStack.getMin(); // return -2
minStack.pop();
minStack.top();    // return 3
minStack.getMin(); // return -1
```

**Constraints:**

* `-231 <= val <= 231 - 1`
* Methods `pop`, `top` and `getMin` operations will always be called on non-empty stacks.
* At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.

## Solution

Intuitively remove non-alphanumeric and change others to lowercase.

```java
```

```python
```

## Complexity

- Time complexity: $$O(1)$$
<!-- Add time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(n)$$
<!-- Add space complexity here, e.g. $$O(n)$$ -->
